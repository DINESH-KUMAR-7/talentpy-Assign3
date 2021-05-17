"""
    Oh! That’s the difference!
    Create a func,on difference which takes a string S and character K. Find the difference between
    first occurrence of K and last occurrence of K in string S. Convert the input to lower case before
    processing.
    Check for following condi,ons :
    1. If K not occurred in S, return “K not found in S”.
    2. If K occurred only once in S, return “Difference can’t be calculated”.
    3. If K occurs more than once, return count of difference.
"""
def difference(S,K):
    #count will increase if char is present in string
    count = 0
    for _ in range(len(S)):
        if(K in S[_]):
            count = count+1
    return count

S=input("ENter a String:")
K = input("Enter a Char:")

S.lower()#string will be converted to lower case
count_diff = int(difference(S,K))
if(count_diff == 0):
    print("K not found in S")
elif(count_diff== 1):
    print("Difference can’t be calculated")
else:
    print("count of difference: ",count_diff)