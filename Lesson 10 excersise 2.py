def get_float_from_user(msg):
    while(True):
        try:
            user_input = float(input(msg))
            return user_input
        except ValueError:
            print("Enter a number, please!")
        except EOFError:
            print("Oops, something went wrong! Try again!")
        except KeyboardInterrupt:
            print("Oops, something went wrong! Try again!")

user_height = get_float_from_user("I need to know your height in centimetres: ")
user_weight = get_float_from_user("And your weight in kilograms: ")
print("Your height is: {:5.2f}cm. and you weight {:.2f}kg.".format(user_height, user_weight))
