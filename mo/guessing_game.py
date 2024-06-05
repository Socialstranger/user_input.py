my_list =list(range(1000))
print(my_list)

for i in my_list:
    i += 0
    if i % 2 == 1:
        print(i)
print(i)
