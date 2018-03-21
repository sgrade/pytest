s = 'String'
length = len(s)
#print(length)
for item in range(length-1, -1, -1):
    print(s[item])


# Generator expression
print('\n###################')
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
#print([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: <generator object <genexpr> at 0x0000000002EBDAF8>

gen_expr = (x**2 for x in my_list)

for i in range(len(my_list)):
    print(next(gen_expr))