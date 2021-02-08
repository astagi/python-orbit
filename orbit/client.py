import requests
from urllib.parse import urljoin
from functools import reduce
from .errors import OrbitException

API_ENDPOINT = "https://app.orbit.love/api/v1/"


class Orbit:
    def __init__(self, auth: str):
        self._auth = auth

    def _execute_query(self, request_type: str, url_elements: list, **params: dict):
        headers = {"Authorization": f"Bearer {self._auth}"}
        url = reduce(lambda a, b: urljoin(a + "/", b), [API_ENDPOINT] + url_elements)
        if request_type == "GET":
            r = requests.get(url, headers=headers, params=params)
            if not r.status_code == requests.codes.ok:
                raise OrbitException("Error")
            return r.json()
        raise OrbitException("Only GET requests are supported at the moment")

    def _is_request_autopaginated(self, params):
        return "auto_paginated" in params and params["auto_paginated"]

    def get_workspaces(self):
        return self._execute_query("GET", ["workspaces"])["data"]

    def get_workspace(self, workspace_id: str):
        return self._execute_query("GET", ["workspaces", workspace_id])

    def get_activities(self, workspace_id: str, **params: dict):
        page = 1
        while True:
            params["page"] = page
            data = self._execute_query("GET", [workspace_id, "activities"], **params)[
                "data"
            ]
            for activity in data:
                yield activity
            if not data or not self._is_request_autopaginated(params):
                break
            page += 1
