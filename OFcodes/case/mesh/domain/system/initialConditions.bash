#!/bin/bash

diameter=7 #m
radius=3.5 #m
rotating_speed=60 #rpm
rotor="turbine_rotor"

xMin=$(echo "-22.000" | bc)
yMin=$(echo "-22.000" | bc)
zMin=$(echo "-40.300" | bc)

xMax=$(echo "70.000" | bc)
yMax=$(echo "25.000" | bc)
zMax=$(echo "25.000" | bc)

