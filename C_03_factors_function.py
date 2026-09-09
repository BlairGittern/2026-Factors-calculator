
# Works out factors, returns sorted list
def get_factors(to_factor):
    factors_list = []
    # square root the number to work out when looping stop
    stop = int(to_factor ** 0.5)

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

# main routine goes here
while True:
    # Use input() to get the string from the user first
    user_input = input("\nEnter an integer between 1 and 200 (or 'xxx' to exit): ")

    # Check for exit condition immediately before converting to an integer
    if user_input.lower() == "xxx":
        print("Thank you for using the program")
        break

    # Ensure the user actually entered a valid number
    if not user_input.isdigit():
        print("Please enter a valid positive integer.")
        continue

    user_num = int(user_input)

    # Ensure it fits the 1 to 200 range
    if not (1 <= user_num <= 200):
        print("Please enter a number between 1 and 200.")
        continue

    # Call get_factors only once using the integer variable
    factors = get_factors(user_num)
    print(f"\nFactors of {user_num} are: {factors}")

    # Check for Unity (1)
    if user_num == 1:
        print("1 is unity and only has one factor.")
    # Check for Prime numbers
    elif len(factors) == 2:
        print(f"{user_num} is a prime number because it has exactly two factors.")
    # Check for composite numbers
    else:
        print(f"{user_num} is a composite number.")

    # Check for Perfect Squares
    # A perfect square always has an odd number of unique factors
    if len(factors) % 2 == 1:
        print(f"{user_num} is a perfect square.")