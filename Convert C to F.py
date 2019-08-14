
your_number = input("enter a whole number in celsius ")

def convert(number):
    try:
        value = int(number)
        if value >= -273:
            new_number = value * 9/5 + 32
            return "C:" + str(value) + "\nF:" + str(new_number)
        else:
            return str(value) + " is under absolute zero!"
    
    except ValueError:
        return "You have to enter the number in numeric form!"
    
print(convert(your_number))



