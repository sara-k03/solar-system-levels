"""
This is level 1 of Python-learning repository. 

DIRECTIONS:

In order to calculate weight, you have to calculate the amount of force that each of these
planets will exert on you. 

You can get this from Newton's Second Law of Motion: Force = Mass * Acceleration. 

Or in this case, weight = mass * acceleration of gravity. 

Weight is in Newtons (N), mass is kilograms (kg), and acceleration of gravity is in m/s^2.

The acceleration of gravity (also called the gravitational field) varies from planet to planet.

To complete this level, complete the tasks below (the things you need to type in are marked with TODO). 

And one last thing, make sure everything is being run from the solar-system-levels/level-1 directory!
"""

import pandas

# TASK 1: Use pandas to read gravitational-fields.csv and return a dictionary with the gravitational fields of all the planets. 
# The parameter file will be the CSV (comma-separated values) file that you are reading the gravitational fields from.
# The CSV file will be in the following format: 
# planetName, gravitationalField 
# planetName will be a string and gravitationalField will be a float. 
def determine_gravitational_fields(file):
    # Dictionary of gravitational fields (I created this variable for you)
    gravitational_fields = {}

    # TODO: Use the pandas library to read the CSV file that is in the format planetName, gravitationalField into the dictionary gravitational_fields.
    # Hint: Look into pandas.read_csv() and DataFrame.to_dict().
    # Type here

    return gravitational_fields

# TASK 2: Now, it's time to determine the weight! 
# The parameter planet represents the name of the planet.
# The parameter mass represents the astronaut's mass in kilograms.
def determine_weight(planet, mass):

    # This calls determine_gravitational_fields so that you have the values stored in a dictionary.
    gravitational_fields = determine_gravitational_fields("gravitational-fields.csv")
    
    # TODO: Figure out the gravitational field of the planet using the dictionary
    planet_gravitational_field = ...

    # TODO: Use planet_gravitational_field and the mass parameter to calculate the weight. 
    weight = ...

    return weight

# Run the determine_weight function here to see if you did it right!
# Here are some sample values you can use to check if your code is correct: 
# - Earth, 50 kg -> 490.5 N
# - Mars, 50 kg -> 185.5 N
# - Jupiter, 50 kg -> 1239.5 N
# - Venus, 70 kg -> 620.9 N
# - Neptune, 60 kg -> 669.0 N
def main():
    mass = 0 # add whatever mass you want here
    planet = "" # add whatever planet you want here 

    print(determine_weight(planet, mass))

if __name__ == "__main__":
    main()