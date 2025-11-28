#WAP to Stop scanning temperature sensors on dangerous reading
temperatures = [25, 40, 10, 70, 15]
for temp in temperatures:
    if temp > 50:
        print("Alert!!! Temperature has crossed 50!")
        break
    print(f"Current temperature is {temp}")