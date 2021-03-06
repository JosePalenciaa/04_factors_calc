import math
# Functions go here

# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    #Makes string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# displays intructions / information 
def instructions():

    print()
    print("• Please choose an integer greater than 0 but is equal / less than 200.")
    print()
    print("• This calculator states the factors of an integer, and whether it is a UNITY, perfect square or prime number.")
    print()
    print("• A list of the integer's factors will be displayed for convenience.")
    print()
    print("• If you wish to continue with more calculations, input <enter> after each calculation or 'any key' to end.")
    print() 
    return""

# Checks input is a number more than a given value
def num_check(question):

    valid = False
    while not valid:
        
        error = "Please enter a number greater than 0 but equal to / less than 200: "
        try:
        
            # ask user to enter a number from (1-200)
            response = int(input(question))
            
            # checks number is more than zero and is less than / equal to 200
            if 0 < response < 201:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
               
                    
        except ValueError:
            print(error)

# Getting the factors and returns a sorted list
def find_factors(num):

    factors=[]
    
    for i in range(1, num+1):
        if num % i ==0:

            factors.append(i)

    return factors

# Main routine goes here

# Heading
statement_generator("Welcome - Factors Calculator","~")

# Display instructions if user has not used the programme before
first_time = input("Press <enter> to see the instructions or any key to continue: ")
print()

if first_time == "":
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # asks the user for a number to factorise
    var_to_factor = num_check("Please input a number: ")
   
      
    # Generate heading
    if var_to_factor ==1:
        heading = "One is special. . ."
    else:
        heading = "Factors of {}".format(var_to_factor)

    if var_to_factor != 1:
        factor_list = find_factors(var_to_factor)
    else:
        comment = "One is a UNITY! Its only factor is itself."
        factor_list= ""

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number - it's only divisible by '1' and itself.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square.".format(var_to_factor)

    # Output factor and comment
    statement_generator(heading,"*")
    print(factor_list)
    print(comment)

    print()
    keep_going = input("Press <enter> to continue or any key to quit: ")
    print()

print()
print("Thank you for using 'Factors Calculator")
print()