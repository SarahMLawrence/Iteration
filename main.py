# COUNTING IN A LOOP
# to count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop
zork = 0
print('Berfore', zork)
for thing in [9, 23, 4, 5, 6, 7]:
  zork  = zork + 1
  print(zork, thing)
print('After', zork)


# SUMMING IN A LOOP
# To add up a value we encounter in a loop, we introduce a sum variable that starts at 0 and we add the value to the sum each time through the loop
zork = 0
print('Before', zork)
for thing in [9, 23, 4, 5, 6, 7]:
  zork = zork + thing
  print(zork, thing)
print("After", zork)


# FINDING AVERAGE IN A LOOP
# An average just combines the counting and sum patterns and divides when the loop is done
count = 0
sum = 0
print('Before', count, sum)
for value in [9, 23, 4, 5, 6, 7]:
  count = count + 1
  sum = sum + value
  print(count, sum, value)
print('After', count, sum, sum / count)


# FILTERING IN A LOOP
# we use an if statemnt in the loop to catch / filter the values we are looking for.
print('Before')
for value in [9, 23, 4, 5, 6, 7]:
  if value > 20:
    print('Large number', value)
print('After')


# SEARCH USING BOOLEAN VARIABLE
# If we just want to search an dknow if a value was found, we use a variable that starts at False and is set to True as soon as we find what we are looking for
found = False # havent found anything yet
print('Before', found)
for value in [9, 23, 3, 4, 5, 6, 7]:
  if value == 3:
    found = True
  elif value !=3:
    found = False
  print(found, value)
print('After', found)


# How to find the smallest value
# we still have a variable that is the smallest so far. The first time through the loop smallest is None, so we take the first value to be the smallest
# None - type - only has one value - it is a constant
smallest_so_far = None
print('Before')
for value in [9, 23, 3, 4, 5, 6]:
  if smallest_so_far is None:
    smallest_so_far = value
  elif value < smallest_so_far:
    smallest_so_far = value
  print(smallest_so_far, value)
print('After', smallest_so_far)

# The "is" and "is not" Operators
# -Python has an is operator that can be used in logical expression
# -Implies "is the same as"
# -Similar to, but stronger than ==
# -is not also is a logical operator
# -use is on boolean or None

# 0 == 0.0 = True
# 0 is 0.0 = False