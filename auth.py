import os
import requests

class IAuthorizationInfo:
    def __init__(self, accesstoken: str, organizationids: [str]):
        self.accessToken = accesstoken
        self.organizationIds = organizationids


# Test .env file setup
print(os.getenv("EMAIL"))

URL = 'https://rest.gatsby.events/login'

# .env file that looks like this
# EMAIL=michael@gatsby.events
# PASSWORD=thisisntmypassword

LOGIN_PARAMS = {
    'email': os.getenv("EMAIL"),
    'password': os.getenv("PASSWORD")
}


def login_with_email_password():
    """Get Login Credentials using username password

    Retruns:
        accessToken: Authorization: Bearer header
        organizationIds: [string] of the accessible organizationIds

    Examples:

        >>> logininfo = login_with_email_password(EMAIL, PASSWORD)
        >>> print(logininfo)
         { 'accessToken': <string>, organizationIds: [<uuid-string>] }
    """
    if LOGIN_PARAMS['email'] == '':
        raise Exception('Missing Email, please ensure your .env is configured with EMAIL and PASSWORD')
    r = requests.post(URL, LOGIN_PARAMS)
    login_data = r.json()
    print('LOGIN RESPONSE', login_data)
    return login_data
