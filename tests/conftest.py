import copy

from fastapi.testclient import TestClient
import pytest

from src.app import activities, app

_original_activities = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    activities.clear()
    activities.update(copy.deepcopy(_original_activities))
    yield


@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client
