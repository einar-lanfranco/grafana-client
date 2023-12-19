from .base import Base


class Admin(Base):
    def __init__(self, client):
        super(Admin, self).__init__(client)
        self.client = client

    def settings(self):
        """

        :return:
        """
        path = "/admin/settings"
        r = self.client.GET(path)
        return r

    def stats(self):
        """

        :return:
        """
        path = "/admin/stats"
        r = self.client.GET(path)
        return r

    def create_user(self, user):
        """

        :param user:
        :return:
        """
        create_user_path = "/admin/users"
        r = self.client.POST(create_user_path, json=user)
        return r

    def change_user_password(self, user_id, password):
        """

        :param user_id:
        :param password:
        :return:
        """
        change_user_password_path = "/admin/users/%s/password" % user_id
        r = self.client.PUT(change_user_password_path, json={"password": password})
        return r

    def change_user_permissions(self, user_id, is_grafana_admin):
        """

        :param user_id:
        :param is_grafana_admin:
        :return:
        """
        change_user_permissions = "/admin/users/%s/permissions" % user_id
        r = self.client.PUT(change_user_permissions, json={"isGrafanaAdmin": is_grafana_admin})
        return r

    def delete_user(self, user_id):
        """

        :param user_id:
        :return:
        """
        delete_user_path = "/admin/users/%s" % user_id
        r = self.client.DELETE(delete_user_path)
        return r

    def pause_all_alerts(self, pause):
        """

        :param pause:
        :return:
        """
        change_user_permissions = "/admin/pause-all-alerts"
        r = self.client.POST(change_user_permissions, json={"paused": pause})
        return r

    def set_user_enabled(self, user_id, enabled: bool):
        """

        :param user_id:
        :param enabled:
        :return:
        """
        action = "enable" if enabled else "disable"
        set_user_enabled = "/admin/users/%s/%s" % (user_id, action)
        r = self.client.POST(set_user_enabled)
        return r

    def create_service_account(self, service_account):
        """

        :param service_account:
        :return:
        """
        create_service_account_path = "/serviceaccounts/"
        r = self.client.POST(create_service_account_path, json=service_account)
        return r

    def delete_service_account(self, service_account_id):
        """

        :param service_account:
        :return:
        """

        delete_service_account_path = "/serviceaccounts//%s" % (service_account_id)
        r = self.client.DELETE(delete_service_account_path)
        return r

    def create_service_account_token(self, service_account_id, uuid4):
        """

        :param service_account_id:
        :param uuid4:
        :return:
        """
        create_service_account_token_path = "/serviceaccounts/%s/tokens" % (service_account_id)
        r = self.client.POST(create_service_account_token_path, json=uuid4)
        return r

    def delete_service_account_token(self, service_account_id, service_account_token_id):
        """
        :param service_account_id:
        :param service_account_token_id:
        :return:
        """
        delete_service_account_token_path = "/serviceaccounts/%s/tokens/%s" % (
            service_account_id,
            service_account_token_id,
        )
        r = self.client.DELETE(delete_service_account_token_path)
        return r
