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


# Main routine goes here
while True:
    to_factor = num_check("To Factor: ")
    print("You chose to factor ", to_factor )

    if to_factor == "xxx":
        break