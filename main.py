################################################################
# Project: Weight on the moon
# File: main.py
# Description: This program asks user to input their body weight, which then
#does a calculation based on moon gravity to get the number of pounds a user
#would weigh on the moon.
# Author: Steven Halla
# Version: 1.0
# Date: April 19th 2023
################################################################

# These Constants define the gravitational pull for earth and the moon
EARTH_GRAVITY: float = 32.17  # feet/second/second
MOON_GRAVITY: float = 5.3  # feet/second/second

# This variable gets the users weight on earth
userWeightOnEarth: float = float(input("Enter your weight on Earth (in pounds): "))

# This variable gets the users weight on earth
userWeightOnMoon: float = (userWeightOnEarth / EARTH_GRAVITY) * MOON_GRAVITY

# display the results
print(f"Your weight on Earth is: {userWeightOnEarth}")
print(f"Your weight on moon is: {userWeightOnMoon}")
