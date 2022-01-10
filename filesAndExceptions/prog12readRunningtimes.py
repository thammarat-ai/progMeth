# This program read the values in the videoRunningTimes.txt file.
# and calculates the total running time of all the videos.

def main():
    # Open the videoRunningTimes.txt file for reading.
    videoFile = open("videoRunningTimes.txt", "r")

    # Initialize the accumulator to 0.0
    total = 0.0

    # Initialize a variable to hold count of the number of videos.
    count = 0

    print('Here are the video running times for each:')

    # Get the values from the file and accumulate them.
    for line in videoFile:
        # Convert the line to a float.
        runningTime = float(line)

        # Add the running time to the total.
        total += runningTime

        # Increment the count.
        count += 1

        # Display the running time.
        print(f"{runningTime:.2f}")

        # Add the time to total.
        total += runningTime

    # Close the file.
    videoFile.close()

    # Display the total running time.
    print(f"\nThe total running time is {total:.2f}.")

    # Display the average running time.
    print(f"The average running time is {total / count:.2f}.")

# Call the main function.
if __name__ == "__main__":
    main()

    