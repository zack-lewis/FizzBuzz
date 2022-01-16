# FIZZBUZZ Challenge
# Language: Python

# define list NUMS
nums = []

# iterate through range of numbers
for i in range(1,100):
    # pre-define the bool values of FIZZ and BUZZ
    FIZZ = False
    BUZZ = False
    
    #check if I is divisible by 3 with no remainder
    if i%3 == 0:
        FIZZ = True
    
    # check if I is divisible by 5 with no remainder
    if i%5 == 0:
        BUZZ = True
    
    # if FIZZ = false, 2 options remain: BUZZ and neither
    if FIZZ == False:
        # if BUZZ is false, then the number with neither FIZZ nor BUZZ
        if BUZZ == False:
            nums.append(i)
        # Otherwise, BUZZ is true, so append BUZZ
        else:
            nums.append("BUZZ")
    # FIZZ is true, so its either FIZZ or FIZZBUZZ
    else:
        # If Buzz is false here, use FIZZ
        if BUZZ == False:
            nums.append("FIZZ")
        # Otherwise, append FIZZBUZZ
        else:
            nums.append("FIZZBUZZ")

# Print out the final result      
print(nums)
