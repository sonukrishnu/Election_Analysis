The data we need to retrieve.
1. The total number of votes cast
2. A complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candiate won
5. The winner of the elction based on popular vote. 
Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)
# Assign a variable for the file to load and the path.
file_to_load = "C:/Users/Swati Goyal/Desktop/Analysis Projects/Election_Analysis/Resources/election_results.csv"
# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Dependencies

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# file to save

# Intialize a total vote counter

# Candidate list and candidate vote dict.


# Creat county list and county votes dict


# Track winning candidate, vote count and percentage

# Track the largest county and voter turnout

# Read CSV 

     # Read header

     # For each row in CSV file:

          # Add total count

          # Get candidate name from each row

          # Extract county name from each row

          # IF candidate does not match any existing candidate add it to the candidate list

               # Add name to list

               #begin tracking voter count

          # Add vote to that candidate's count

          # IF statement to do the same for county

               # Add county to list

               # Begin tracking county's vote count

          # Add vote to county's vote count

     # FOR loop to get the county with the most votes

          # retrive county vote

          # calculate percentage of votes for county

          # print county results to terminal

          # same county votes to txt file.

          # # IF statement to determine winning county 

     
     # FOR loop to get thecandidate votes

          # retrive vote and calculate percent

          # print candidate results to terminal

          # save candidate votes to txt file.

          # # IF statement to determine winning county 

#Print statement (terminal)

# Save to txt file. 

