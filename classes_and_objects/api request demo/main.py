import requests
project_list = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
print(project_list.json())
print(type(project_list.json()))
print(project_list.text)
f= open("response.txt","w+")
f.write(str(project_list.json()))


required_dict = {}

for required_data in project_list.json():
    if required_data["name"]:
     required_dict["name"] = required_data["name"]
    print(required_dict)  



