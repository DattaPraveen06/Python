#1) You need to print a string in the following format ..
    # The Order is:
    # Apples : 30
    # Oranges : 10
    # Total : 40 Units

Apples = 30
Oranges = 10
c = Apples + Oranges
print(f'Apples : {Apples}', f'Oranges : {Oranges}', f'Total :{c} Units')
#-------------------------------------------------------------------------------

# 2)I have a string "hello world" I need the following output "world hello"

d ="hello world"
f = d.split(' ')
fst = f[0]
snd = f[1]
print(snd + ' ' + fst)

#-------------------------------------------------------------------------------

# 3)In the string "Hello world" print the following - "Hd" "el"

#d ="hello world"    --> has already declared  above
print((d[0] + d[10]) +' ' +d[1] + d[9])

# ------------------------------------------------------------------------------
# 4)In the string "Hello world" for the 2 words Hello and World get the length
#    separately and print the difference of the lengths

# d ="hello world"
# f = d.split(' ')
# fst = f[0]
# snd = f[1]        --> this has been declared above

l1 = len(fst)
l2 = len(snd)
print('length of first word is : ' + str(l1))
print(f'length of 2nd word is : {l2}')
print('difference of two word is:' + str(l1-l2))

#--------------------------------------------------------------------------------
# 5) Write a program to evaluate the following expression.  (2/3*100 + 23/4)

print(2/3*100 + 23/4)

# -------------------------------------------------------------------------------

# 6)what is the output of 1/0.0

print(1/0.0)  # ZeroDivisionError: float division by zero
#
# -------------------------------------------------------------------------------
# 7)what would be the output of x * y where  x = 100 ; y = None
# x = 100
# y = None
# print(x * y)  #TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

# -------------------------------------------------------------------------------
# 8)what would be the result of the following bool(100) > bool([])

print(bool(100) > bool([]))  #True

# -------------------------------------------------------------------------------
# 9)write a program to convert centigrade to fahrenheit. The formula is (0°C × 9/5) + 32 = 32°F

F = (0 * 9/5) + 32
print(f'{int(F)}°F')

# -------------------------------------------------------------------------------
#10) write a program to convert miles to kilometer

miles = 10
km = miles * 1.60934
print(km)
