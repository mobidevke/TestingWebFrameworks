import pytest
import requests


@pytest.fixture(scope='module')
def base():
    return 'http://0.0.0.0:5000'


@pytest.fixture(scope='module')
def client():
    yield requests
