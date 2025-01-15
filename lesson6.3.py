number = input('enter a number')

while len(str(number)) > 1:
    product = 1
    for num in str(number):
        product *= int(num)
        number = product
print(number)