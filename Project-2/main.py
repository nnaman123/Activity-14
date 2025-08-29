#define function to calculate cube
def cube(num):
    return num*num*num

#define a function which will execute cube function if the number entered by the user is divisible by 3
def by_three(num):
    if num%3==0:
       return(cube(num))
    else:
        return False
#present the output to the user
print(by_three(9))
print(by_three(4))
