#!/usr/bin/python3.6
import requests
import getpass

link = 'https://adc.luxoft.com/confluence/login.action'
destination = 'https://adc.luxoft.com/confluence/display/HNAVSTD/Home'
LOGIN = 'dkicha'
PASSWORD = getpass.getpass('Enter your password: ')

with requests.Session() as session:
    session.get(link)
    login_data = dict(os_username=LOGIN, os_password=PASSWORD, login='Log in')
    session.post(link, data=login_data)
    response = session.get(destination)

    print(response.status_code)
