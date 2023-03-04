import pytest
import requests
from main import UsersYD

def test_correct_folder_creation():
    resp = UsersYD(token='').create_folder('new_folder')
    assert resp.status_code in [200, 201]
    return resp

def test_fail_folder_creation():
    resp = UsersYD(token='').create_folder('new_folder')
    assert resp.status_code in [400, 401, 403, 404, 406, 409, 413, 423, 429, 503, 507]