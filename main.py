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
# These Constants define the gravitational pull for earth and the moon
EARTH_GRAVITY: float = 32.17  # feet/second/second
MOON_GRAVITY: float = 5.3  # feet/second/second

# Get the user's weight on Earth
valid_input = False
while not valid_input:
    try:
        userWeightOnEarth = float(input("Enter your weight on Earth (in pounds): "))
        valid_input = True
    except ValueError:
        print("Please enter a valid integer weight in pounds.")

# Calculate the user's weight on the Moon
userWeightOnMoon: float = (userWeightOnEarth / EARTH_GRAVITY) * MOON_GRAVITY

# Display the results
print(f"Your weight on Earth is: {userWeightOnEarth}")
print(f"Your weight on the moon is: {userWeightOnMoon:.2f}")
