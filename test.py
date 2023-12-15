
from grafana_client import GrafanaApi
import os
import uuid


from dotenv import load_dotenv
load_dotenv(".env")
print("sadfsadasfsaf"+os.getenv("GRAFANA_URL"))
grafana_api = GrafanaApi.from_url(url=os.getenv("GRAFANA_URL"),credential=(os.getenv("GRAFANA_USER_API"),os.getenv("GRAFANA_PASS_API")))
print(dir(grafana_api.admin))
user=grafana_api.admin.create_system_account({"name": "pepedcito", "role": "Viewer"})
print(user['login'])
# Generar un UUID aleatorio
uuid_aleatorio = uuid.uuid4()
token="%s-%s" % (user['login'], uuid_aleatorio)

token=grafana_api.admin.create_system_account_token(user['id'],{'name':token})

uid_folder="da7c5fdd-8df6-4008-a986-8efc8715bed4"
permissions={"permission": "View"}
id_user=(user['id'])
grafana_api.folder.update_folder_permissions_for_user(uid_folder, id_user, permissions)

print(token)

# grafana_api.admin.
# {permission: "View"}

# https://grafana.csirtamericas.org/api/access-control/dashboards/tEDfUqmIk/users/209
# https://grafana.csirtamericas.org/api/access-control/dashboards/tEDfUqmIk/users/203

# print(grafana_api.systemaccounts.search_system_accounts())
