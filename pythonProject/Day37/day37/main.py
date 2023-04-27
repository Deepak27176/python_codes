import requests
username = "deepakammu"
token = "mytokenisdeepakammu27176"
pixel_api = " https://pixe.la/v1/users"
user_params = {
    "token": "mytokenisdeepakammu27176",
    "username": "deepakammu",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# after creating user comment the code
# response = requests.post(url=pixel_api, json=user_params)
# print(response.text)
## To creat graph
graph_api = f"{pixel_api}/{username}/graphs"
graph_profile = {
    "id": "test-graph",
    "name": "workout",
    "unit": "pushups",
    "type": "int",
    "color": "ajisai"
}
header ={
"X-USER-TOKEN": token
}

# response = requests.post(url=graph_api, json=graph_profile, headers=header)
# print(response.text)
pixel_api = "https://pixe.la/v1/users/deepakammu/graphs/test-graph/20220420"
pixel_params = {
    "date": "20220420",
    "quantity": "4507"
}
response = requests.delete(url=pixel_api,  headers=header)
# response = requests
print(response.text)