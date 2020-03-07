#Code by Raustone (25.02.2020)

import time
Nmb_Zero = 0
Nmbs = []
test = 0
Nmb_Test = 0

print("I am a prime number detector, I can say if your number is prime or no. What number you want try ?")
Nmb_test = int(input())

if Nmb_test <= 1 :
    print("You can't write this number ...")
    time.sleep(3.0)
    exit()
else :
    for i in range(Nmb_test//2 + 5):
        test += 1
        Nmbs.insert(test, Nmb_test%test)
    if Nmbs.count(0) > 2 :
        print("Your number is not a prime number.")
        time.sleep(5.0)
        exit()
    else :
        print("Your number is a prime number.")
        time.sleep(5.0)
        exit()
