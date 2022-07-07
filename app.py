import auth
import downloader
from pathlib import Path
import logging

logging.basicConfig(
    filename=Path('app.log'), 
    level=logging.INFO,
    format='%(name)s - %(levelname)s - %(message)s'
    )

def download(access_token, refresh_token):
    """ Here we call our downloader.py file which will handle all
        activities needed to get our report. 
    """
    wbx_download = downloader.Webex_Reports(access_token=access_token, refresh_token=refresh_token)
    response = wbx_download.main()
    return response

def main():
    """ Main entry point into the application.
        First we will authenticate to Webex and gather our tokens.
        Second we will start our downloading process.
    """
    webex_oauth = auth.Auth()
    tokens = webex_oauth.kickoff()
    logging.debug(f"Access Token:{tokens['access_token']} Refresh Token:{tokens['refresh_token']}")
    response = download(access_token=tokens['access_token'], refresh_token=tokens['refresh_token'])
    print(f'Done: {response}')

if __name__ == "__main__":
    main()
