#!/usr/bin/python3

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import os
import re
import sys
sys.path.append('/home/matheus/OpenFOAM/resources')
import tools

case_path = os.getcwd()

# Extract the variables
p = tools.extract_initial_conditions(os.path.join(case_path, "system/initialConditions"))

# Reference power coefficient
reference_cp = 0.24

data_dir = "./postProcessing/forces"
time = []
power_coefficient = []

# Iterate through each directory in data_dir
for directory in os.listdir(data_dir):
    # Get the path to the current directory
    directory_path = os.path.join(data_dir, directory)
    if os.path.isdir(directory_path):
        # Read the "moment.dat" file in the current directory
        data_path = os.path.join(directory_path, "moment.dat")
        t, cp = tools.extract_power_coefficient(os.path.join(case_path, data_path), p['rotation_speed_rads'], p['power_available'])
        
        # Append the extracted values to the existing lists
        time.extend(t)
        power_coefficient.extend(cp)

sorted_data = sorted(zip(time, power_coefficient))
time, power_coefficient = zip(*sorted_data)

# Function to update the plot
def update_plot(num, reference_cp, time, power_coefficient):
    # Clear the previous plot
    plt.cla()

    # Plotting the torque values against time
    plt.plot(time, power_coefficient)
    plt.xlabel('Time')
    plt.ylabel('Power coefficient')
    plt.grid(True)
    plt.ylim(0, 0.6)  # Set the y-axis limit

    # Adding the horizontal dashed line
    plt.axhline(y=reference_cp, color='black', linestyle='--')
    plt.text(max(time) / 2, reference_cp+0.01, 'Reference measurement', color='black', fontsize=10, ha='center')
    plt.title(f"{power_coefficient[-1]:.3f} - Power coefficient")

    # Get the current directory
    current_directory = os.getcwd()
    files = os.listdir(current_directory)

    filename_fig = f"{power_coefficient[-1]:.3f} - Power coefficient.png"

    # Iterate over the files and delete those matching the criteria
    for file in files:
        if file.endswith(".png") and "- Power coefficient" in file:
            file_todelete = os.path.join(current_directory, file)
            os.remove(file_todelete)

    plt.savefig(filename_fig)

# Create the animation
ani = animation.FuncAnimation(plt.gcf(), update_plot, fargs=(reference_cp, time, power_coefficient), interval=60000)  # Update every minute (60000 milliseconds)

# Display the plot
plt.show()
