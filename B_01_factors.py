#Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# Displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
 To use this program simply enter an integer between 
 1 and 200. The program will show the factors of your 
 chosen integer.

 It will also tell you if your chosen number...
 - is a prime number (ie: it has two factors)
 - is a perfect square

 To exit the program, please type 'xxx'.
    ''')


# Ask user for an integer between 1 and 200
def num_check(question):
    error = "Please enter a number that is between 1 and 200 inclusive\n"
    while True:

        response = input(question).lower()
        if response == "xxx":
            return response

        try:
            # ask the user for a number
            response = int(response)

            # check that the number is between 1 and 200
            if 1<= response <= 200:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Works out factors, returns sorted list
def get_factors(to_factor):
    factors_list = []

    # square root the number to work out when looping
    stop = to_factor ** 0.5
    stop = int(stop)

    for item in range(1, stop + 1):
        # check to see if the item is a factor
        if to_factor % item == 0:
            # Add first factor to list
            factors_list.append(item)

            # find second factor by dividing ' to factor ' by the first factor
            partner = to_factor // item

            # check second factor is not in list and add it
            if partner not in factors_list:
                factors_list.append(partner)

    # output
    factors_list.sort()
    return factors_list


# Main routine goes here

statement_generator("The Ultimate Factor Finder", "-")

# Display instructions if requested
want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue ")

if want_instructions == "":
    instructions()

while True:
    user_num = num_check("\nEnter an integer between 1 and 200: ")

    if user_num == "xxx":
        break

    factors = get_factors(user_num)

    print(f"\nFactors of {user_num} are: {factors}")

    # Check for Unity (1)
    if user_num == 1:
        print("1 is unity and only has one factor.")

    # 2. Check for Prime numbers
    elif len(factors) == 2:
        print(f"{user_num} is a prime number because it has exactly two factors.")

    # Check for Perfect Squares
    # A perfect square always has an odd number of unique factors
    if len(factors) % 2 == 1:
        print(f"{user_num} is a perfect square.")

statement_generator("Thank you for using the program", "*")