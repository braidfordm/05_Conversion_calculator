def conversion_checker():
    
    error = "Please chose valid measurement"

# loop starts here
while True:
    response = input ("What are you convering from? ").lower()

    if response == "mg" or  response == "g" or  response == "kg" or response == "t":
        return ("weight")

    elif response == "sec" or response =="min" or response == "hour":
        return ("time")

    elif 




