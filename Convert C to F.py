
your_number = input("Enter a whole number in Celsius ")

def convert(number):
    try:
        value = int(number)
        if value >= -273:
            new_number = value * 9/5 + 32
            return "C:" + str(value) + "\nF:" + str(new_number)
        else:
            return "Your number " + str(value) + " is under absolute zero!"
    
    except ValueError:
        return "You have to enter the number in numeric form!"
    
print(convert(your_number))



