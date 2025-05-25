class InvalidAgeError(Exception):
    pass


def check_age(age:int):
    try:
        if age <= 0:
            raise InvalidAgeError("Negative or 0 is not allowed")
        elif age < 18:                                  
            print("you are not an adult")
        else:
            print("you are an adult")
    except InvalidAgeError as e:
        print("Custom Error:",e )


check_age(0)
