def is_leap(year):
    
    leap = False
    # x=year/4
    # r=range(1900,100000)
    # y=year/(100*2)
    # if x==int(year/4):
    #    print('false')
    # elif y==int(y):``
    #     print('true')
    # return leap
    
    if year%4 ==0:
        leap = True
    elif year%100 == 0:
        leap = False
    return leap
year = int(input())
print(is_leap(year))