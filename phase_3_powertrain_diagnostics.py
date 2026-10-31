vehicle = {
    "vehicle_id": "PT-012",
    "engine_temp": 112,
    "rpm": 2500,
    "mileage": 45200
}

def check_engine_temp(vehicle):
    if vehicle["engine_temp"] <= 110:
        print("Engine Temperature PASS")

    else:
        print("Engine Temperature FAIL")



def check_rpm(vehicle):
    if vehicle["rpm"] >= 700 and vehicle["rpm"] <= 6000:
        print("RPM PASS")

    else:
        print("RPM FAIL")


def check_powertrain_status(vehicle):
    if vehicle["engine_temp"] <= 110 and vehicle["rpm"] >= 700 and vehicle["rpm"] <= 6000:
        print("Powertrain PASS")

    else:
        print("Powertrain FAIL")


check_engine_temp(vehicle)
check_rpm(vehicle)
check_powertrain_status(vehicle)
