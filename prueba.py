from grafana_client import GrafanaApi
import os
# import uuid


from dotenv import load_dotenv

load_dotenv(".env")
print("sadfsadasfsaf" + os.getenv("GRAFANA_URL"))
grafana_api = GrafanaApi.from_url(
    url=os.getenv("GRAFANA_URL"), credential=(os.getenv("GRAFANA_USER_API"), os.getenv("GRAFANA_PASS_API"))
)
print(dir(grafana_api.admin))

###ACA es lo que necesito
# user=grafana_api.admin.create_system_account({"name": "pepedcito", "role": "Viewer"})
# print(user['login'])
# # Generar un UUID aleatorio
# uuid_aleatorio = uuid.uuid4()
# token="%s-%s" % (user['login'], uuid_aleatorio)

# token=grafana_api.admin.create_system_account_token(user['id'],{'name':token})

# uid_folder="da7c5fdd-8df6-4008-a986-8efc8715bed4"
# permissions={"permission": "View"}
# id_user=(user['id'])
# grafana_api.folder.update_folder_permissions_for_user(uid_folder, id_user, permissions)

# print(token)
### HASTA ACA es lo que necesito

# https://grafana.csirtamericas.org/api/access-control/dashboards/tEDfUqmIk/users/209
# https://grafana.csirtamericas.org/api/access-control/dashboards/tEDfUqmIk/users/203

# print(grafana_api.serviceaccounts.search_service_accounts(query="juan"))
sa = grafana_api.serviceaccounts.find_service_account(service_account_name="rjuan")

print(grafana_api.serviceaccount.get_actual_service_account(sa["id"]))
tokens = grafana_api.serviceaccount.get_actual_service_account_tokens(sa["id"])
# print(tokens[0]['id'])
# print(sa['id'])
# print(grafana_api.admin.delete_service_account_token(sa['id'],(tokens[0]['id'])))
