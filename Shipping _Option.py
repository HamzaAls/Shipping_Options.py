
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
