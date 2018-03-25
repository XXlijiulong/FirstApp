'''统计并输出这行字符中的英文字符，数字，空格，和其他字符的个数'''
user=input("请输入一行字符:")
eng=digit=block=other=0
for i in user:
    if i.isalpha():
        eng+=1
    elif i.isdigit():
        digit+=1
    elif i==' ':
        block+=1
    else:
        other+=1
print("英文字符{}".format(eng))
print("数字{}".format(digit))
print("空格{}".format(block))
print("其他{}".format(other))
