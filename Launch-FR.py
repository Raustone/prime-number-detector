#Code by Raustone (25.02.2020)

import time
Nmb_Zero = 0
Nmbs = []
test = 0
Nmb_Test = 0

print("Je suis un testeur de nombres premier, je suis capable de déterminer si un nombre est premier ou non. Quel nombre voulez-vous tester ?")
Nmb_test = int(input())

if Nmb_test <= 1 :
    print("Zéro et un ne sont pas compatible avec ce test ...")
    time.sleep(3.0)
    exit()
else :
    for i in range(Nmb_test// 2 + 5):
        test += 1
        Nmbs.insert(test, Nmb_test%test)
    if Nmbs.count(0) > 2 :
        print("Votre nombre n'est pas premier.")
        time.sleep(5.0)
        exit()
    else :
        print("Votre nombre est premier.")
        time.sleep(5.0)
        exit()
