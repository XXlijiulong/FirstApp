a = []
def LeapYear(A,B):
    for i in range(A,B):
        if((i%4==0 and i%100!=0)or (i%400==0)):
            a.append(i)
    return a
if __name__=='__main__':
    print("1000年到2000以内的闰年为:{}".format(LeapYear(2000,2018)))
    for i in range(1,10,3):
        print(i)
