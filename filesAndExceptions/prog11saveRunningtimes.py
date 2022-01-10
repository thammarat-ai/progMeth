# This program saves a sequence of video running times
# to the videoRunningTimes.txt file.
def main():
    # Get the number of videos in the project.
    numVideos = int(input("How many videos are in the project? "))

    # Open the videoRunningTimes.txt file for writing.
    videoFile = open("videoRunningTimes.txt", "w")

    # Get each video's running time.
    # and write the running times to the file.
    print("Enter the running times for each video.")
    for count in range(1, numVideos + 1):
        # Get the running time for a video.
        runningTime = float(input(f"Video #{count}: "))

        # Write the running time to the file.
        videoFile.write(f"{runningTime:.2f}\n")

    # Close the file.
    videoFile.close()
    print("Data written to videoRunningTimes.txt")

# Call the main function.
if __name__ == "__main__":
    main()

