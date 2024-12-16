#!/bin/bash

LINE="---------------------------------------------------------------"

echo "Starting at: $(date)"
echo "$LINE" 

echo "UPTIME"
uptime 
echo "$LINE" 

echo "FREE"
free 
echo "$LINE" 

echo "WHO"
who 
echo "$LINE" 

echo "Finishing at: $(date)"
echo "$LINE" 
echo