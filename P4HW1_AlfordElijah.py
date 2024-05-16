# Elijah Alford
# 5/15/2024
# P4HW1_AlfordElijah
# Collect scores using a loop and display answers

# Ask the user to enter the number of scores they want to enter
num_scores = int(input("How many scores do you want to enter? "))

# Create an empty list to store the scores
scores = []


for i in range(num_scores):
    # Ask the user to enter a score
    score = float(input("Enter score #" + str(i+1) + ": "))
    
    # Validate the score
    while score < 0 or score > 100:
        print("INVALID score entered! Score should be between 0 and 100")
        score = float(input("Enter score #" + str(i+1) + " again: "))
    
    # Add the score to the list
    scores.append(score)

# Calculate the lowest score
lowest_score = min(scores)

# Remove the lowest score from the list
scores.remove(lowest_score)

# Calculate the average score
average_score = sum(scores) / len(scores)

# Determine the letter grade for the average score
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Display the results
print("-----------------Results------------------")
print("Lowest score: " + str(lowest_score))
print("Modified List: ", scores)
print("Average score: %.2f" % average_score)
print("Grade: " + grade)
