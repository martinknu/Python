
lst = [1,2,3,4]

def my_generator():
    for num in range(50):
        yield num ** num
  


all_numbers = list(my_generator())
print(all_numbers)


for big_num in my_generator():
    print(big_num)

# total = list(range(50))
# print(total)
