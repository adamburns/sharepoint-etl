import json
import os
import requests
from dotenv import load_dotenv


SELECT_PARAMS = [
    'ID',
    'BaseName',
    'Sponsor',
    'ReportStatus1',
    'SPW',
    'WFProgress',
    'DateInitialStage',
    'DateInProgressRFI',
    'DateInProgressDrafting',
    'DateSponsorReview',
    'DateFinalizeProject',
    'DateCompleted1',
    'ProjectLead/Title',
    'ReportType',
    'ProgramType',
    'LinkToOpportunity',
    'First_x0020_Draft_x003f_',
    'QC',
    'Editor0',
    'DraftSentDate',
    'Final'
]



def auth_token():
    load_dotenv()
    url = 'https://accounts.accesscontrol.windows.net/' + os.getenv('SP_TENANT_ID') + '/tokens/OAuth/2'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    body = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('SP_CLIENT_ID') + '@' + os.getenv('SP_TENANT_ID'),
        'client_secret': os.getenv('SP_CLIENT_SECRET'),
        'resource': os.getenv('SP_RESOURCE') + '/' + os.getenv('SP_DOMAIN') + '@' + os.getenv('SP_TENANT_ID')
    }

    return requests.get(url=url, headers=headers, data=body).json()['access_token']


def projects_url():
    load_dotenv()
    return os.getenv('SP_PROJECTS_URL')


def tasks_url():
    load_dotenv()
    return os.getenv('SP_TASKS_URL')


def headers():
    return {'Accept':'application/json;odata=verbose',
           'Authorization':'Bearer ' + auth_token()}


def download_data(url, headers):
    data = requests.get(url=url, headers=headers)
    return data


def extract_projects():
    return download_data(projects_url(), headers())


def extract_tasks():
    return download_data(tasks_url(), headers())

