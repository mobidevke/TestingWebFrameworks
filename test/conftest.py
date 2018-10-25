import socket
import subprocess
import time

import pytest
import requests


@pytest.fixture(scope='session')
def server():
    timeout = 5
    subprocess.call(['docker-compose', '-f', 'counter-app/docker-compose.yml', 'up', '-d'])
    count = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while count < timeout:
        print('Checking server...')
        result = sock.connect_ex(('0.0.0.0', 5000))
        if result == 0:
            print('Ready...')
            break

        time.sleep(1)
        count += 1

    if count == timeout:
        raise pytest.exit('Unable to connect to running app')
    yield

    subprocess.call(['docker-compose', '-f', 'counter-app/docker-compose.yml', 'down'])


@pytest.fixture(scope='module')
def base():
    return 'http://0.0.0.0:5000'


@pytest.fixture(scope='module')
def client(server):
    yield requests
