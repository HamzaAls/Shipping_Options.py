'''
from datetime import date
import json
from multiprocessing.sharedctypes import Value
import re
import requests

server = "https://178.74.59.186:4434"
nbox_manufacturers = "/api/dcim/manufacturers"
myheaders = {'Authorization':'Token a6582fd99e88413997670f5c9c3e29c2d8115089'}
response = requests.get(server + nbox_manufacturers + "?", headers=myheaders, verify=False)
if response.status_code == 200:
    data=json.loads(response.text)
    data2=(json.dumps(data,indent=4))
    data2=data['results']

    #last inn response-dataen fra json til en 
    #python-liste kalt data.
    for value in data2:
        if value['name']=='Cisco':
            print('OK')''' 
       
            
    

'''test=[{
            "id": 20,
            "url": "https://178.74.59.186:4434/api/dcim/manufacturers/20/",
            "display": "AKCP",
            "name": "AKCP",
            "slug": "akcp",
            "description": "",
            "tags": [],
            "custom_fields": {},
            "created": "2021-09-06",
            "last_updated": "2021-09-06T06:40:42.131599Z",
            "devicetype_count": 2,
            "inventoryitem_count": 0,
            "platform_count": 0
        },
        {
            "id": 48,
            "url": "https://178.74.59.186:4434/api/dcim/manufacturers/48/",
            "display": "Alcatel-Lucent",
            "name": "Alcatel-Lucent",
            "slug": "alcatel-lucent",
            "description": "",
            "tags": [],
            "custom_fields": {},
            "created": "2021-11-08",
            "last_updated": "2021-12-01T11:24:23.479751Z",
            "devicetype_count": 1,
            "inventoryitem_count": 0,
            "platform_count": 0
        }

]
for value in test:
  
    if value['name']=="Alcatel-Lucent": 
            print('OK')
            break
else:
    print('NOT EXIST')
    
cabinet = { "scores":(98,76,95), "name":"Chris","company":"Cisco"}   #dictionary

numbs = {1, 2, 4, 5, 6, 8, 10} #set

        


type(numbs)

Age=int(input('How old are you? '))
if  Age >=18:
    print('GO GO ')
else:
    print('IF YOU ARE 'f'{Age}','YOU ARE IN, \nBUT you have to Bring your parents with you')'''

Choose = int(input('''Which offer du You want from the Avilable :
- Ground_Shipping enter 1
- Ground_Shipping_Premium enter 2
- Drone_Shipping enter 3
Waiting for your input '''))
if Choose==1:
    class Ground_Shipping:
        Weight_of_Package = int(input('What is the Weight'))
        Price_per_Pound = float
        Flat_Charge= 20.00
        if Weight_of_Package <=2:
            Price_per_Pound=1.50
            Total=(Price_per_Pound+Flat_Charge)
            print('YOUR PRICE IS ',Total,'$')        
        elif Weight_of_Package >2 and Weight_of_Package<= 6:
            Price_per_Pound =3.00 
            Total=(Price_per_Pound+Flat_Charge)
            print('YOUR PRICE IS ',Total,'$')       
        elif Weight_of_Package >6 and Weight_of_Package <=10:
            Price_per_Pound =4.00
            Total=(Price_per_Pound+Flat_Charge)
            print('YOUR PRICE IS ',Total,'$')       
        elif Weight_of_Package > 10:
            Price_per_Pound =4.75
            Total=(Price_per_Pound+Flat_Charge)
            print('YOUR PRICE IS ',Total,'$')
elif Choose==2:
    class Ground_Shipping_Premium:
        Flat_Charge= 125.00
        Total =Flat_Charge
        print('YOUR PRICE IS ',Total,'$')
elif Choose==3:
    class Drone_Shipping:
        Weight_of_Package = int(input('What is the Weight'))
        if Weight_of_Package <=2:
            Price_per_Pound = (1.50*3)      
        elif Weight_of_Package >2 and Weight_of_Package<= 6:
            Price_per_Pound = (3.00*3)     
        elif Weight_of_Package >6 and Weight_of_Package <=10:
            Price_per_Pound = (4.00*3)        
        elif Weight_of_Package > 10:
            Price_per_Pound = (4.75*3)
        Total=(Price_per_Pound)
        print('YOUR PRICE IS ',Total,'$')
else:
    print('ERROR')
