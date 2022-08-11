import json


# reading in the json data
def readFile(file_name):
    with open(file_name) as file:
        json_data = json.load(file)
    return json_data


# extracting the uuid for each device from the "Info" field
def getUuid(device):
    info = (device["Info"])
    tokens = info.split(" ")
    uuid_token = tokens[3]
    uuid = uuid_token[5:-1]
    return uuid


# calculating the total payload for each device's sensors
def calcTotalPayload(device):
    total = 0
    sensors = device["Sensors"]
    for sensor in sensors:
        total += sensor["Payload"]
    return total


# reformatting the data to match schema
def extract(json_data):
    reformatted_data_array = []
    devices = json_data["Devices"]
    for device in devices:
        reformatted_data = {"Name": "",
                            "Type": "",
                            "Info": "",
                            "Uuid": "",
                            "PayloadTotal": 0}
        payload_total = calcTotalPayload(device)
        uuid = getUuid(device)

        reformatted_data["Name"] = device["Name"]
        reformatted_data["Type"] = device["Type"]
        reformatted_data["Info"] = device["Info"]
        reformatted_data["Uuid"] = uuid
        reformatted_data["PayloadTotal"] = payload_total

        reformatted_data_array.append(reformatted_data)

    return reformatted_data_array


# ordering reformatted data in ascending order by "Name"
def orderData(data_array):
    for i in range(0, len(data_array) - 1):
        for k in range(i + 1, len(data_array)):
            device1 = ((data_array[i])["Name"]).lower()
            device2 = ((data_array[k])["Name"]).lower()
            if device1 > device2:
                temp = data_array[i]
                data_array[i] = data_array[k]
                data_array[k] = temp
    return data_array


# writing reformatted data to json file
def writeFile(data):
    json_format_data = {"Devices": data}
    json_string = json.dumps(json_format_data)
    json_file = open("newDevices.json", "w")
    json_file.write(json_string)
    json_file.close()


def main():
    json_data = readFile('data\devices.json')
    reformatted_data_array = extract(json_data)
    ordered_data_array = orderData(reformatted_data_array)
    writeFile(ordered_data_array)


main()
