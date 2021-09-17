secret = 42
guess = 0
print(0 == int('0')) # casting (turning string into num)
# indented blocks are called code suites
# while will run until conditions are met (this is the more elegant way to write it)
while secret != guess:
    # reassignment to guess
    # problem because str is not equel to num (read above note)
    guess = int(input('guess a number\n> ')) # tells python to create a new line
    if guess < secret:
        print('You guessed too low.')
    elif guess > secret:
        print('You guessed too high!')

print('Good job you got it!')

'''
Conditionals:
if.. elif ...else
elif (else if)

comparison ops
>
<
>= ... <=
==
!=
These result in a boolean (true or false)
'''