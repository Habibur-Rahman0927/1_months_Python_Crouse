num = int(input())
if (1<num and num<100 or num>0):
    if (num%2)!= 0:
        print(num,"Weird")
    elif (num%2) == 0 :
        if (2<num and num<5):
            print(num,"Not Weird")
        elif (6<num and num<20):
            print(num,"Weird")
        elif num>20:
            print(num,"Not Weird")
elif num>0:
    print(num,"Not Weird")

else:
    print("Not weird")
