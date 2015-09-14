__author__ = 'Tauren'

import base64
import requests
import os

from integrator.models import User, HeartRate
from integrator import db
from sqlalchemy.orm import sessionmaker

def run():
    Session = sessionmaker(bind=db)
    session = Session()
    data = session.query(User).all()
    print('1. Users: %s' % data)
    data = session.query(HeartRate).all()
    print('2. HR Data: %s' % data)
    session.close()

def exchange_refresh_token(current_refresh_token):
    """ Exchange a refresh token for new access and refresh token
    :return: refresh_token, access_token
    """
    # Todo; need to update database with new token.
    decoded_string = os.getenv('CLIENT_ID') + ':' + os.getenv('CLIENT_SECRET')
    auth_header = b'Basic ' + base64.urlsafe_b64encode( decoded_string.encode('utf-8'))

    payload = {'grant_type': 'refresh_token',
               'refresh_token': current_refresh_token}

    headers = {'Authorization': auth_header, 'Content-Type': 'application/x-www-form-urlencoded'}

    r = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, data=payload)
    request_json = r.json()
    print('Results: %s' % request_json)
    return request_json.get('refresh_token', ''), request_json.get('access_token', '')

def query_hr_time_series(access_token, date):
    """ Query heart rate intra-day time series endpoint
    :param access_token:
    :param date:
    :return: json
    """
    headers = {'Authorization': 'Bearer %s' % access_token}
    hr_url = 'https://api.fitbit.com/1/user/-/activities/heart/date/%s/1d/1min.json' % date
    result = requests.get(hr_url, headers=headers)
    return result.json()


if __name__ == '__main__':
    run()
    # exchange_refresh_token()