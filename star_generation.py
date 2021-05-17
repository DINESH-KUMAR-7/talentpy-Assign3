"""
 Star Generation: Create a python func,on which takes a number N and generates following star
 pacern accordingly. N ranges from 1 to any posi,ve number. Make sure if N is not passed as
 argument while calling func,on, it should take 3 as it’s default value.
"""
def  Star_gene(N=3):
    if(N>=1):
        #executes for 1 to N times. on N+1 time it get fail
        for _ in range(N+1):
            # If _ is even : @ will be printed / odd : * will be printed
            if(_%2 == 0):
                print("@"*_)
            else:
                print("*"*_)

N = int(input("Input:"))
Star_gene(N)