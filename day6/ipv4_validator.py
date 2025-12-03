
"""ipv4 address validator
192.168.1.1
It must contain 4 fields only
Only numbers
0 to 255"""

ipv4 = input("Enter one IPV4 address: ")
ipv4_arr = ipv4.split(".")
is_valid = True
if len(ipv4_arr) == 4:
    for i in ipv4_arr:
        if not (i.isdigit() and int(i)>=0 and int(i)<=255):
            is_valid = False
            break
else:
    is_valid = False
if is_valid:
    print("Valid IPV4: ", ipv4)
else:
    print("InValid IPV4: ", ipv4)
