def digui():
    day=9
    n=1
    while day>0:
        n=(n+1)*2
        day=day-1
    return n
def digui2():
    day=9
    n=1
    for i in range(0,9):
       n=(n+1)*2
    return n
if __name__=='__main__':
   print(digui())
   print(digui2())
