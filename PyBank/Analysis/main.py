# Import Modules
import os
import csv

# Set path for the file
#csvpath = "../Resourses/budget_data.csv"
csvpath = os.path.join("..", "Resources", "budget_data.csv")


# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)