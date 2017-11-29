def increment_string(strng):
    numstr=''
    strstr=''
    str2=strstr[:len(numstr)]
    print(str2)
    for cha in strng:
        if cha.isdigit():
            numstr+=cha
        else:
            strstr+=cha
    if numstr=='':
        print(strstr+'1')
        return 1
    num=int(numstr)
    str2=strstr[:len(numstr)+1]
    print(str2)
    # print(numstr)
    
    if len(str(num))==len(numstr):
        print(strstr+str(num+1))
    else:
        zeros=len(numstr)-len(str(num+1))
        print(zeros)
        res=('0'*zeros)+str(num+1)
        print(strstr+res)
        return strng

increment_string("foo09")