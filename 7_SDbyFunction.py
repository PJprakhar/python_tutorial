import statistics, math

def my_sd(input):
    print(f'input : {input}')
    length = len(input)
    sum = 0
    mean = statistics.mean(input)
    print(f'Mean : {mean}')
    for x in input:
        sum +=(int(x) - mean)**2

    sum = sum / length
    output = math.sqrt(sum)
    return output

input = [20,23,18]
Answer = my_sd(input)
Answer = round(Answer, 3)
print(f'Answer: {Answer}')


