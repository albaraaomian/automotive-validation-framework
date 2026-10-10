
battery_voltages = [12.4, 11.8, 10.5, 13.2, 9.8]

passed = 0 
failed = 0

for voltages in battery_voltages:
    if voltages >= 11.5:
        passed += 1
        
    else:
        failed += 1

print("Passed tests: ",passed)        
print("Failed tests: ",failed)
