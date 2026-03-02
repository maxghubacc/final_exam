import random
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))
# continue here
# go through the list via indexing so numberes can be modified
for i in range(len(random_numbers)):
    # checks if the number is odd via comparison opperator - takes the remainer of a number when divided by 2, if this value is anything other than 0, the number is odd.
    if random_numbers[i] % 2 != 0:
        # replace it with itself, but with a - in front
        random_numbers[i] = -random_numbers[i]
    else:
        # if the number is even, replace it with itself * 2
        random_numbers[i] = random_numbers[i] * 2
# print the modified list of random numbers
print(random_numbers)