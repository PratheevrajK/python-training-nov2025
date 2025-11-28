## Fuel Consumption Simulator
#### Scenario: A vehicle burns 5 litres of fuel per loop.
#### Task
#### •	Start with fuel = 40 litres
#### •	Reduce fuel by 5 in each loop
#### •	Show "Fuel left:" every cycle
#### •	Stop when fuel is 0
#### •	Print "Refuel needed!"
fuel_left = 40
while fuel_left > 0:
    fuel_left -= 5
    print(f"Fuel left: {fuel_left}")
print("Refuel needed!")