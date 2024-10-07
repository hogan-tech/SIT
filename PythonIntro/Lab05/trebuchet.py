# Author: Hogan Lin
# Date: Oct 6th 2024
# Github: https://github.com/hogan-tech/SIT/tree/main/PythonIntro
# Description: This program simulates the recording of trebuchet trial distances. 
#              It allows the user to input distances for multiple trials and keeps track of the top three distances.
#              The results are displayed with the corresponding trial numbers.

"""
This function records trebuchet launch distances, tracks the top three longest distances, and prints the results.

:param None: The function does not take any parameters.
:return: Prints out the top three distances with their respective trial numbers.
"""



def trebuchet():

    topDistances = [0, 0, 0]

    topTrials = [0, 0, 0]

    continueInput = "Y"
    trialNumber = 1

    while continueInput.upper() == "Y":

        distance = int(
            input(f"Please enter your distance for trial {trialNumber}: "))

        if distance > topDistances[0]:

            topDistances[2] = topDistances[1]
            topTrials[2] = topTrials[1]
            topDistances[1] = topDistances[0]
            topTrials[1] = topTrials[0]

            topDistances[0] = distance
            topTrials[0] = trialNumber
        elif distance > topDistances[1]:

            topDistances[2] = topDistances[1]
            topTrials[2] = topTrials[1]

            topDistances[1] = distance
            topTrials[1] = trialNumber
        elif distance > topDistances[2]:

            topDistances[2] = distance
            topTrials[2] = trialNumber

        continueInput = input(
            "Would you like to input another trial? (Y/N): ")

        trialNumber += 1

    print("The top three distances for the trebuchet are:")
    print(f"{'Trial':<6} {'Distance':<8}")
    for i in range(3):
        print(f"{topTrials[i]:<6} {topDistances[i]:<8}")


trebuchet()
