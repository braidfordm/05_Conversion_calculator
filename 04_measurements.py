# Checks user choice is 'weight', 'distance' or 'time'
def user_choice():

    valid = False
    while not valid:
        
        # Ask user for choice and change response to lowercase
        response = input("measurement (weight / distance / time): ").lower()

        # Checks for valid response and returns time, distance, weight

        # If they choose "wt" or "w" or "weight", return "weight"
        weight_ok = ["weight", "w", "wt"]
        if response in weight_ok:
            return "weight"

         # If they choose "distance" or "length" or "d" or "dist", return "distance"
        distance_ok = ["distance", "length", "d", "dist", "l"]
        if response in distance_ok:
            return "distance"

         # If they choose "time" or "t" return "time"
        time_ok = ["time", "t"]
        if response in time_ok:
            return "time"


        else: 
            print("Please choose a valid measurement!")
            print()


 # Main routine goes here
keep_going = ""
while keep_going == "": 
    data_type = user_choice() 
    print("You chose",  data_type)
    print()
    