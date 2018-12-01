#Problem Statement: https://www.hackerrank.com/challenges/30-dictionaries-and-maps/submissions

n = input() # number of input data
no_dict = dict() # dictionary to store name and number
for _ in range(int(n)):
    name, number = (input().split())
    no_dict[name] = number
for _ in range(int(n)):
    new_input = input() 
    #print(new_input)
    if new_input in no_dict:
        print('%s=%s'%(new_input,no_dict[new_input]))
    else:
        print('Not found')