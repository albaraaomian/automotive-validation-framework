
battery_voltage = [12.4, 11.8, 10.5, 13.2, 9.8]

passed = 0 
failed = 0

for voltage in battery_voltage:
    if voltage >= 11.5:
        passed += 1
        
    else:
        failed += 1


total_tests = len(battery_voltage)

if total_tests > 0:
    pass_rate = (passed / total_tests) * 100
else:
    pass_rate = 0

print("Total tests: " ,total_tests)
print("Pass Rate: " ,pass_rate)


print("Passed tests: ",passed)        
print("Failed tests: ",failed)
