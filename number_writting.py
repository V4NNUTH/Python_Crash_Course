#input data to json
# import json

# numbers =[2,3,5,7,11,13]

# filename = 'number.json'
# with open(filename,'w') as f:
#     json.dump(numbers,f)

#read data from json


import json
filename = 'number.json'
with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)
