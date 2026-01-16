def average(values):
    """ Calculates the average of the given list. """
    total = 0
    for n in values:            # total the given values
        total += float(n)
    return total / len(values)  # return calculated average


# initialisation statement
print("Welcome, utils module has been imported and initialised!")


# Detect if running as a script
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        # Skip program name, convert extras to floats
        values = [float(x) for x in sys.argv[1:]]
        print("Average of arguments is", average(values))
    else:
        print("No arguments provided.")
