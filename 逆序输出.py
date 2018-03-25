def reverse(s):
    if s=="":
        return s
    else:
        return reverse(s[1:])+s[0]
if __name__ =='__main__':
    str=input("请输入一个字符串:")
    print(reverse(str))