vehicle = {
    "vehicle_id": "PT-009",
    "battery_voltage": 12.8,
    "dtc_count": 2
}

def check_battery(vehicle):
    if vehicle["battery_voltage"] >= 11.5:
        print("Battery PASS")
    else:
        print("Battery FAIL")




def check_dtcs(vehicle):
    if vehicle["dtc_count"] == 0:
        print("DTC PASS")
    else:
        print("DTC FAIL")


def check_vehicle_readiness(vehicle):
    if vehicle["battery_voltage"] >= 11.5 and vehicle["dtc_count"] == 0:
        print("vehicle READY")

    else:
        print("vehicle NOT READY")


check_battery(vehicle)
check_dtcs(vehicle)
check_vehicle_readiness(vehicle)

