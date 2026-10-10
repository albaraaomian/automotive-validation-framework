
battery_voltages = [12.4, 11.8, 10.5, 13.2, 9.8]

for voltages in battery_voltages:
    if voltages >= 11.5:
        print("PASS - Voltage normal")
    else:
        print("FAIL - Low voltage")
