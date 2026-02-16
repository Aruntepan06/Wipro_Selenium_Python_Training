a=range(5)
print(a[1])


for attempt in range(3):
    pin=input("enter the pin: ")
    if pin=="1234":
        print("Access granted")
        break
    else:
        print("access denied")


prices=[100,200,300,400,500]

for i in range(len(prices)):
    if i%2==0:
        print("Discount applied on item{1}")

import time
for second in range(10):
    print("checking the status of {Second} Sec")
    time.sleep(1)

