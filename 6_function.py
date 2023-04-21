def my_add(input):
    sum = 1
    for x in input:
        sum *= int(x)
    return sum
    
input = [10,20,30]
Answer = my_add(input)
print(f'Answer: {Answer}')

input = [23,45,63,75,83,92]
Answer = my_add(input)
print(f'Answer: {Answer}')

input = [874,345,623,6345,13423,6434]
Answer = my_add(input)
print(f'Answer: {Answer}')

