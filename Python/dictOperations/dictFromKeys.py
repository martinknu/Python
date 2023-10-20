#Copy one dict values to another dict with different keys
#Problem is 'y' or value is only read once ??

x = ('key1', 'key2', 'key3')
y = [1,2,3]

thisdict = dict.fromkeys(x, y)

print(thisdict)