device_status = "active"
temperature = 30

if device_status == "active":
    if temperature > 35:
        print("High Temperature")
    else:
        print("Normal Temperature")
else: 
    print("Device is offline")
