type=input()
quantity=int(input())
distance=int(input("In kilometers:"))
if(quantity>0 and distance>0):
    if(type=='N'):
        if(distance<=3):
            bill=150*quantity+(distance*0)
        elif(distance<=6):
            bill=150*quantity+((distance-3)*3)
        else:
            bill=150*quantity+(3*3)+(distance-6)*6
        print(bill) 
    elif(type=='V'):
        if(distance<=3):
            bill=120*quantity+(distance*0)
        elif(distance<=6):
            bill=120*quantity+((distance-3)*3)
        else:
            bill=120*quantity+(3*3)+(distance-6)*6
        print(bill)
    else:
        print("-1")
else:
    print("-1")