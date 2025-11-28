## Shopping Cart Total
 
#### Scenario: User keeps adding item prices until they type 0.
 
#### Task
 
#### Keep asking: "Enter item price:"
 
#### Add price to total.
 
#### Stop the loop when input is 0.
 
#### Print the final total.
i = 1
total = 0
while i != 0:
    value = int(input("Enter item price: "))
    total += value
    if value == 0:
        i = 0
print(f"Total price is {total}")
