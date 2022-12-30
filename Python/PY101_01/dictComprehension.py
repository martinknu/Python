#Dictionaries and dictcomprehension
#


#This is a list containing 2 touples
names = [("name","Martin"), ("Occupation","Full stack")]
print(f'type of name: {type(names)}')
print(f'type of name index 0: {type(names[0])}')

# Create a dictionary the long way
d = {}
for key, value in names:
    d[key] = value
print(d)
print(f'the type is:{type(d)}')

#Create with dictoinary comprehension
d = {key: value for key, value in names}
print(d)

#Create with dict constructor
d = dict(names)
print(d)