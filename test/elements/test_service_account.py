import unittest

import requests_mock

from grafana_client import GrafanaApi


class ServiceAccountsTestCase(unittest.TestCase):
    def setUp(self):
        self.grafana = GrafanaApi(("admin", "admin"), host="localhost", url_path_prefix="", protocol="http")



class ServiceAccountTestCase(unittest.TestCase):
    def setUp(self):
        self.grafana = GrafanaApi(("admin", "admin"), host="localhost", url_path_prefix="", protocol="http")

    @requests_mock.Mocker()
    def test_get_actual_service_account(self,m):
        get_actual_service_account_path = "http://localhost/api/serviceaccounts/201?accesscontrol=true"
        m.get(get_actual_service_account_path, json={'id': 201, 'name': 'rjuan', 'login': 'sa-juan', 'orgId': 1, 'isDisabled': False, 'createdAt': '2023-12-15T21:38:59Z', 'updatedAt': '2023-12-19T12:46:06Z', 'avatarUrl': '/avatar/06b4d9db72de4d293813135da09fd736', 'role': 'Viewer', 'teams': None, 'accessControl': {'serviceaccounts.permissions:read': True, 'serviceaccounts.permissions:write': True, 'serviceaccounts:delete': True, 'serviceaccounts:read': True, 'serviceaccounts:write': True}})
        result = self.grafana.serviceaccount.get_actual_service_account(201)
        self.assertEqual(result, {'id': 201, 'name': 'rjuan', 'login': 'sa-juan', 'orgId': 1, 'isDisabled': False, 'createdAt': '2023-12-15T21:38:59Z', 'updatedAt': '2023-12-19T12:46:06Z', 'avatarUrl': '/avatar/06b4d9db72de4d293813135da09fd736', 'role': 'Viewer', 'teams': None, 'accessControl': {'serviceaccounts.permissions:read': True, 'serviceaccounts.permissions:write': True, 'serviceaccounts:delete': True, 'serviceaccounts:read': True, 'serviceaccounts:write': True}})

    @requests_mock.Mocker()
    def test_get_actual_service_account_tokens(self, m):
        get_actual_service_account_path = "http://localhost/api/serviceaccounts/201/tokens"
        m.get(get_actual_service_account_path, json=[])
        result = self.grafana.serviceaccount.get_actual_service_account_tokens(201)
        self.assertEqual(len(result), 0)
