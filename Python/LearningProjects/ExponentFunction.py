#This function should take the user input and do exponents
def ExponentFunc(Value,power):
    Result = 1
    for a in range(power):
        Result = Value * Result

    return Result

Value = int(input("What value do you want as the base?: "))
power = int(input("What do you want as the power?: "))
print(ExponentFunc(Value,power))