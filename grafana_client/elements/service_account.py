from .base import Base


class ServiceAccounts(Base):
    def __init__(self, client):
        super(ServiceAccounts, self).__init__(client)
        self.client = client

    def search_service_accounts(self, query=None, page=1, perpage=None):
        """

        :return:
        """
        list_of_sa = []
        sa_on_page = None
        show_sa_path = "/serviceaccounts/search"
        params = []
        if query:
            params.append("query=%s" % query)

        if page:
            iterate = False
            params.append("page=%s" % page)
        else:
            iterate = True
            params.append("page=%s")
            page = 1

        if perpage:
            params.append("perpage=%s" % perpage)
        
        show_sa_path += "?"
        show_sa_path += "&".join(params)
        if iterate:
            while True:
                url = show_sa_path % page
                sa_on_page = self.client.GET(url)
                if not sa_on_page:
                    break
                list_of_sa.append(sa_on_page)
                page += 1
        else:
            sa_on_page = self.client.GET(show_sa_path)
            list_of_sa.append(sa_on_page)

        return list_of_sa

    # def get_service_account(self, service_account_id):
    #     """

    #     :param service_account_id:
    #     :return:
    #     """
    #     get_actual_user_path = "/serviceaccounts/%s?accesscontrol=true" %(service_account_id)
    #     r = self.client.GET(get_actual_user_path)
    #     return r

    def find_service_account(self, service_account_name=''):
        """

        :param service_account_name:
        :return:
        """
        s = self.search_service_accounts(query=service_account_name)[0]
        if s['totalCount'] == 1:
            return s['serviceAccounts'][0]
        elif s['totalCount'] > 1:
            return 'More than one service account matched'
        else:
            return 'No service account matched'        

    # def update_user(self, user_id, user):
    #     """

    #     :param user_id:
    #     :param user:
    #     :return:
    #     """
    #     update_user_path = "/users/%s" % user_id
    #     r = self.client.PUT(update_user_path, json=user)
    #     return r

    # def get_user_organisations(self, user_id):
    #     """

    #     :param user_id:
    #     :return:
    #     """
    #     get_user_organisations_path = "/users/%s/orgs" % user_id
    #     r = self.client.GET(get_user_organisations_path)
    #     return r


class ServiceAccount(Base):
    def __init__(self, client):
        super(ServiceAccount, self).__init__(client)
        self.client = client
        self.path = "/serviceaccounts"

    def get_actual_service_account(self, service_account_id):
        """
        :return:
        """
        get_actual_service_account_path = "/serviceaccounts/%s?accesscontrol=true" %(service_account_id)
        r = self.client.GET(get_actual_service_account_path)
        return r
    
    def get_actual_service_account_tokens(self, service_account_id):
        """
        :return:
        """
        get_actual_service_account_tokens_path = "/serviceaccounts/%s/tokens" %(service_account_id)
        r = self.client.GET(get_actual_service_account_tokens_path)
        return r
