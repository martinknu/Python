



names = [("name","Martin"), ("Occupation","Full stack")]

# Create a dictionary the long way
d = {}
for key, value in names:
    d[key] = value
print(d)

#Create with dictoinary comprehension
d = {key: value for key, value in names}
print(d)

#Create whit function :-)
d = dict(names)
print(d)