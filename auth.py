import os
from requests_oauthlib import OAuth2Session
from dotenv import load_dotenv
load_dotenv()

import logging
log = logging.getLogger(__name__)


class Auth():
    def __init__(self):
        self.client_id = os.getenv("APP_CLIENTID")
        self.client_secret = os.getenv("APP_SECRETID")
        self.redirect_uri = "https://localhost:8080/webex-teams-auth.html"

        self.authorization_base_url = 'https://webexapis.com/v1/authorize'
        self.token_url = 'https://webexapis.com/v1/access_token/'

        self.scope = [
            "analytics:read_all"
            ]

    def kickoff(self):
        webex = OAuth2Session(self.client_id, scope=self.scope, redirect_uri=self.redirect_uri)

        authorization_url, state = webex.authorization_url(self.authorization_base_url)
        print(f'Please go here and authorize: {authorization_url}')

        redirect_response = input('Paste the full redirect URL here:')

        response = webex.fetch_token(
            self.token_url,
            client_secret=self.client_secret,
            include_client_id=True,
            authorization_response=redirect_response
            )
        
        log.info(f'Access and Refresh tokens obtained.')
        log.debug(f"Access Token: {response['access_token']}")
        log.debug(f"Refresh Token: {response['refresh_token']}")

        return {
            "access_token": response['access_token'],
            "refresh_token": response['refresh_token']
        }
