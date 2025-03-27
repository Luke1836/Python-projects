import math

def transform_number(n):
    s = str(n)
    length = len(s)
    
    half_length = math.ceil(length / 2)
    first_half = s[:half_length]
    
    incremented = str(int(first_half) + 1)
    
    if len(incremented) > len(first_half):
        incremented = incremented[:-1]
    
    second_half = incremented[:length - half_length][::-1]
    
    return incremented + second_half

n1 = input("Enter a number: ").strip()
if int(n1) < 10:
    exit()
print(transform_number(n1))


