# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
    
# print(contents)


#filename = 'pi_digits.txt'

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

#if file has alot of digit like 1000000000 digit

filename = 'pi_digits.txt'

with open(filename) as fileObj:
    lines = fileObj.readlines()
pi_string =''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:12]}.....")
print(len(pi_string))
