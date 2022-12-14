# Puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{} {} {}" .format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# Displays instructions/information
def instructions():

    statement_generator("Instructions/information", "-")
    print()
    print("Please choose a unit to convert from and a unit to convert to")
    print()
    print("This program converts measurements of mass, time, and distance")
    print()
    print("Complete as many calculations as necessary by pressing <enter> at the end of each calculation or any key to quit")
    print()
    return ""

# Main routine
instructions()

