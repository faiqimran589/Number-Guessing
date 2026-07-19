import random
d=random.randint(1,100)
while True:
 number=int((input('Enter the number between 1 and 100:')))


 if number > d :
   print('Try lower number')
 
 elif number < d:
   print('Try greater number')
  
 elif number == d :
   print('Congratulations')
   break
 else :
    print('Number not recognized')
    