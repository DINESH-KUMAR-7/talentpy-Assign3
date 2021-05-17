"""
 Be Posi?ve! Create a func,on to sum up all posi,ve argument inputs. Inputs ranges from 0 to N,
 where N can be any posi,ve number.
"""
def sum_up_all(N):
    sum=0
    for _ in range(N):
        if(_>=0):
            sum = sum+_
        else:
            print("Integer not positive!")
    return sum

N = int(input("INput:"))
result = sum_up_all(N)
print(result)