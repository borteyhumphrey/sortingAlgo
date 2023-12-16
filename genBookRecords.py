import random
import string
import argparse

parser = argparse.ArgumentParser(description='Generates a list of random  fictitious book records')

parser.add_argument('count', type=int, help='number of random book records to generate')

args = parser.parse_args()



def gen_book(count): 
    length = random.randint(2, 6)
    result = []  
    for j in range(count): 
        result.append(random.randint(pow(10, 5), pow(10, 6)))
        result.append(''.join(random.choices(string.ascii_lowercase, k=length)) + ' ' +''.join(random.choices(string.ascii_lowercase, k=length)))
        result.append(''.join(random.choices(string.ascii_lowercase, k=6)))
        result.append(random.randrange(1, 999999))
        result.append(random.randint(pow(10, 9), pow(10, 10)))
                   
    return result

res = []
res = gen_book(args.count)

c = 5
for i in range(len(res)):
    if i % c == 0:
        print()
    if isinstance(res[i], str):
        print(res[i], end='')
    else:
        print(res[i], end='')
    if i % c != c - 1 and i != len(res) - 1:
        print(', ', end='')
    
