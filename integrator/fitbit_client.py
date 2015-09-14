__author__ = 'Tauren'

import os
import requests
import base64

class FitbitClient:

    def __init__(self):
        pass

    def exchange_refresh_token(self, current_refresh_token):
        """ Exchange a refresh token for new access and refresh token
        :return: refresh_token, access_token
        """
        decoded_string = os.getenv('CLIENT_ID') + ':' + os.getenv('CLIENT_SECRET')
        auth_header = b'Basic ' + base64.urlsafe_b64encode( decoded_string.encode('utf-8'))

        payload = {'grant_type': 'refresh_token',
                   'refresh_token': current_refresh_token}

        headers = {'Authorization': auth_header, 'Content-Type': 'application/x-www-form-urlencoded'}

        r = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=payload)
        request_json = r.json()
        print('Results: %s' % request_json)
        return request_json.get('refresh_token', ''), request_json.get('access_token', '')

    def query_hr_time_series(self, access_token, date):
        """ Query heart rate intra-day time series endpoint
        :param access_token:
        :param date:
        :return: json
        """
        headers = {'Authorization': 'Bearer %s' % access_token}
        hr_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/%s/1d/1min.json' % date
        result = requests.get(hr_url, headers=headers)
        return result.json()
