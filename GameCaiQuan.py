from random import*
a=eval(input("请输入一个数:(0剪刀1石头2布)"))
computer=randint(0,3)
if((a==0 and computer==2)or(a==1 and computer==0 )or(a==2 and computer==1)):
    print("YOU are Winner")
elif((a==0 and computer==0)or(a==1 and computer==1 )or(a==2 and computer==2)):
    print("equal")
else:
    print("You are loser")
#print("电脑输出的是{}".format(computer))