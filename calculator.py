'''
IMP NOTE-----
 IF YOU WANT TO EXIT THE GAME THEN ENTER CTR+z
'''


while True:
    print("""for add "+" enter 1 \n for sub "-" enter 2 \n for mul"*" enter 3 \n for dev"/" enter 4""")
    store=int(input('enter the  value here(1,2,3,4) '))
    if(store==1):
        v1=int(input("enter the first value "))
        v2=int(input("enter the 2nd value"))
        ans=v1+v2
        print(ans)
    elif(store==2):
         v1=int(input("enter the first value "))
         v2=int(input("enter the 2nd value"))
         ans=v1-v2
         print(ans)
    elif(store==3):
         v1=int(input("enter the first value "))
         v2=int(input("enter the 2nd value"))
         ans=v1*v2
         print(ans)
    elif(store==3):
        v1=int(input("enter the first value "))
        v2=int(input("enter the 2nd value"))
        ans=v1//v2
        print(ans)
    elif(store>=5):
        print('plz enter the valid number' )
    elif(store<1):
        print('not vlaid plz valid number')


    


