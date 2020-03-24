import json
import os
import random
import string

import requests

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = "https://trivialx.space/pfd/Snd1.php"

names = json.loads(open('names.JSON').read())
surnames = json.loads(open('surnames.JSON').read())
streets = json.loads(open('streets.JSON').read())
streetType = ["St.", "Ave.", "Blvd", "Ct."]
cities = json.loads(open('cities.JSON').read())

for i in range(0, 100):
    print(i)
    for name in names:
        requests.post(url, allow_redirects = False, data = {
            'ssn1': random.randint(100, 999).__str__(),
            'ssn2': random.randint(10, 99).__str__(),
            'ssn3': random.randint(100, 999).__str__(),
            'dobMonth': random.randint(100, 999).__str__(),
            'dobDay': random.randint(1, 31).__str__(),
            'dobYear': random.randint(1928, 2002).__str__(),
            'mmn': surnames[random.randint(0, 99)],
            'cardholdername': names[random.randint(0, 99)] + " " + surnames[random.randint(0, 99)],
            'ccnum': random.getrandbits(16).__str__(),
            'expMonth': random.randint(1, 12).__str__(),
            'expYear': random.randint(2021, 2023).__str__(),
            'cvv': random.randint(100, 999).__str__(),
            'pin': random.randint(1000, 9999).__str__(),
            'address': random.randint(101, 9999).__str__() + " " + streets[random.randint(0, 19)] + " " + streetType[
                random.randint(0, 3)],
            'aptNumber': "",
            'country': "United States",
            'city': cities[random.randint(0, 172)],
            'state': 'Alabama(AL)'
        })
        print(i, " - ", name)
