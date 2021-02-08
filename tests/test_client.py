import pytest

from orbit import Orbit, OrbitException


def test_client_workspaces_request(requests_mock):

    expected_json = {
        "data": [
            {"id": "650", "type": "workspace", "attributes": {}, "relationships": {}}
        ]
    }
    requests_mock.get("https://app.orbit.love/api/v1/workspaces", json=expected_json)

    client = Orbit(auth="f4k3")
    workspaces = client.get_workspaces()

    assert workspaces[0]["id"] == "650"


def test_errors(requests_mock):

    client = Orbit(auth="f4k3")
    requests_mock.get("https://app.orbit.love/api/v1/workspaces", status_code=400)
    with pytest.raises(OrbitException):
        location = client.get_workspaces()
