import re
import pytest

from src.Xray.XrayClient import Client
pytest_plugins = 'pytester'

@pytest.fixture()
def XrayAPIClient():
    client = Client(api_token = "35d22edc556e5b88f1e1bcf8fd3c90da7c0056c2")
    return client
