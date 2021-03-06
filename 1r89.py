"""
    Mr.Talentpy would like to create a func,on one_or_eight which takes an integer input (no) and
    performs following opera,on.
    1. Square the number if it is single digit. (Eg: 3, then 3 * 3 = 9)
    2. If it is not single digit, square each digits and add. (Eg: 12, then (1*1) + (2*2) = 1+4 = 5
    You have to repeat step (1) and (2) until you reach 1 or 89. Note that, always your result will reach
    1 or 89 for sure. Input must be a posi,ve number.
    If the operation reaches at the end, 89 return True, if opera,on reaches 1 at the end return False.

"""

def one_or_eight(no):
    sum_val=0
    if(no==1):
        return False
    elif(no==89):
        return True
    elif(no<10):
        no = no*no
        return one_or_eight(no)
    else:
        while(no!=0):
            sum_val = sum_val+((no%10)**2)
            no = no//10
        no = sum_val
        return one_or_eight(no)


no=int(input("INPUT:"))
result = one_or_eight(no)
print(result)