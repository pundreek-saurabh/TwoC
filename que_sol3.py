def find_days(m,y):
    if(m==1 or 3 or 5 or 7 or 8 or 10 or 12 ):
        p=31
    elif(m== 4 or 6 or 9 or 11):
        p=30
    elif(y%100==0 or y%4==0 and y%100!=0 and m==2):
        p= 29
    else :
        p = 28
    return p
p=find_days(4,9)
print("days in the month provided is" , find_days (4,9) )
