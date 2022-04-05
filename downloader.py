import json
import time
from pathlib import Path
import requests
import logging
log = logging.getLogger(__name__)

class Webex_Reports():

    def __init__(self, access_token: str, refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.base_url = 'https://webexapis.com/v1'

    def _get_templates(self):
        url = f'{self.base_url}/report/templates'
        response = requests.get(url=url, headers={'Authorization': f'Bearer {self.access_token}'})
        if response.status_code != 401:
            log.info(f'Gathered Templates')
            templates = json.loads(response.text)
            for template in templates['items']:
                print(f"Template Title: {template['title']}, Template ID: {template['Id']}")
            
            template_user_input = input("Which Template ID would you like to run? ")
            logging.info(f'User template selection: {template_user_input}')
            return template_user_input
        else:
            log.warning('Access Token was Expired')

    def _report_creation(self, template: str):
        url = f'{self.base_url}/reports'
        data = {
            "templateId": int(template),
            "startDate": "2022-03-01",
            "endDate": "2022-03-31",
            "siteList": "jhaefner-gasandbox.webex.com"
        }
        response = requests.post(url=url, headers={'Authorization': f'Bearer {self.access_token}'}, json=data)
        if response.status_code != 401:
            json_response = json.loads(response.text)
            log.info(f"Created Report ID: {json_response['items']['Id']}")
            return json_response['items']['Id']
        else:
            log.warning('Access Token was Expired')

    def _check_on_report(self, id: str):
        url = f'{self.base_url}/reports/{id}'
        report_status = 'not done'
        download_url = ""
        while report_status != 'done':
            response = requests.get(url=url, headers={'Authorization': f'Bearer {self.access_token}'})
            json_response = json.loads(response.text)
            download_url = json_response['items'][0]['downloadURL']
            report_status = json_response['items'][0]['status']
            print(f"Report status: {json_response['items'][0]['status']}, checking in 30 seconds...")
            time.sleep(30)
        log.info(f'Report Download URL: {download_url}')
        return download_url

    def _download_report(self, url: str):
        try:
            response = requests.get(url=url, headers={'Authorization': f'Bearer {self.access_token}'})
            with open(Path('./files/test_download.csv'), 'wb') as writefile:
                writefile.write(response.content)
            log.info(f'Downloaded Report...')
            return True
        except Exception as e:
            print(f'Error: {e}')

    def _delete_report(self, id: str):
        url = f'{self.base_url}/reports/{id}'
        response = requests.delete(url=url, headers={'Authorization': f'Bearer {self.access_token}'})
        if response.status_code == 204:
            log.info(f'Deleted Report ID: {id}')
            return response.status_code
        else:
            log.error(f'Deleted Report ID: {id}, status code: {response.status_code}')
            return response.status_code

    def main(self):
        template_response = self._get_templates()
        report_creation_response = self._report_creation(template=template_response)
        report_created = self._check_on_report(id=report_creation_response)
        report_downloaded = self._download_report(url=report_created)
        if report_downloaded:
            result = self._delete_report(id=report_creation_response)
            return result
        else:
            log.error(f'Unable to download Report ID: {report_creation_response} from URL: {report_created}')