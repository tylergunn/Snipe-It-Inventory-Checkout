import requests
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiMDVlM2Y5ODZhNjFlYzU3ODdmNzQ5YjkzYzgyMGJjZmI0YzllNjY0NGZhOTdlZTgyYTY3NDNiM2FkMTEyNzA4NGJkOGFjYmU5ODNlZDE4ODUiLCJpYXQiOjE2NjgyMDIzMzEuNDMzNTQsIm5iZiI6MTY2ODIwMjMzMS40MzM1NDQsImV4cCI6MjE0MTU4NzkzMS40MDUwNTMsInN1YiI6IjUiLCJzY29wZXMiOltdfQ.n6LmJF65JbL-iUnkFIYhe7Pa3e2W6_ld-HKLEZHBYTdL7rQ67QTL7kgS0GaFIreLyIKQYX_Ifq2gn3MyfJAn67VNZ_0kcTfsMjpQFav8knckS0F47v45xIJMdLvzASJGqz6BD_CZUfpOJ-Peb9nUsvWJ9VTq64zmJ40CsfBldKI6ZjKkkMbukNGVB-746k4m-LxcWZgIPZhIDey4yMo9pabuVS5-PEGXePLnnDOTrxm1v1qcbDA4mRRk-E2L4SZwssQLsbYOWhuUs97ikrzMVNVSpYC91_YeMCV1gwfazaT6W-fj9ERUsDIX4fv6PPboDKY_xiyzYzIwa6EzmQYJu4zjwcMLcJlvDpJY0odT5tmuSOMddZKLw2rJ0Ty96m25fpJAI1dNXf8cuV4Wh7gQak8NjlPkLUlRBpOlidfmj11R293V9icTHgSGcu7VGTVF7FlgHVj67F1Wr7UFZ4Lad_t8kvqUFiWwP2QwhMsMR1uBJkeHA55iVWJfJ1Cxay0ZIUtm-_VondaFBE8pjBa1sdwemYJLZIPOKyuf1NgRrPiWQW6fQNv-GOIlEVCI3dpPamypgVPyIPItcOTRefQW-OhbgcTbuMN139GlmxNizMIbdcTavDArrlzRBRED3THBIPC1arMuRkQ6QhaVzMrdhMVQhg57ExSiw3PjlomV6DI"
}
def get_asset(asset):
    # try:
    url = f"http://192.168.0.52/api/v1/hardware/bytag/{asset}"
    response = requests.get(url, headers=headers)
    data = response.json()
    try:
        if data['status']=='error':
            return None,None
        else:
            id = data['id']
            print(data)
            return id
    except:
        id = data['id']
        return id
# except:
    return False
    print("error")

def check_out(asset_id,location_id):
    try: 
        url = f"http://192.168.0.52/api/v1/hardware/{asset_id}/checkout"
        payload = {
        "checkout_to_type": "location",
        "status_id": 2,
        "assigned_location": location_id
        }

        response = requests.post(url, json=payload, headers=headers)
        response = response.json()
        print(response)
        if response['status'] == 'success':
            return True
        else:
            return False
    except:
        return False
def check_in(asset_id):
    url = f"http://192.168.0.52/api/v1/hardware/{asset_id}/checkin"
    response = requests.post(url, headers=headers)
    response = response.json()
    if response['status'] == 'success':
        return True
    else:
        return False
def get_locations():
    # try:
    locations = []
    url = f"http://192.168.0.52/api/v1/locations?sort=name&order=asc"
    response = requests.get(url, headers=headers)
    response = response.json()
    # print(response)
    for i in response['rows']:
        locations.append({"name":i['name'],
                    "id":i['id']})
    return locations
# except:
    return "Error"
def set_hardware_note(id,name):
    url = f"http://192.168.0.52/api/v1/hardware/{id}"
    payload = {
        "notes" : name
        }
    requests.put(url, headers=headers, json=payload)
def get_location_data(locations, location_name):
    for location in locations:
        if location['name'] == location_name:
            return location['id']
