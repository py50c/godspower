import time # It import the time module from time relating functios

print("Stopwatch") # This will print the title of the program
print("-----------") # Print horizontal divdier
start_time = time.time() # Record the start time
input("Press Enter to start. Afterwards, press Ctrl+C to stop.") 
# Tells the user to press enter to start the stopwatch\ and to press Ctrl+C to stop
print("started.") # It prints a reply to tell the stop watch has started

try: # Enter an infinite loop to countinously update the elasped time
   while True: # Helps to calculate the elasped time since the start time
      elasped_time = time.time() - start_time 
      # Converts the elasped time into minutes, seconds and hundreths
      minutes = int(elasped_time / 60)
      seconds = int(elasped_time % 60)
      hundreths = int((elasped_time % 1) *100)

      print(f"{minutes:02d}:{seconds:02d}:{hundreths:02d}", end="\r") # Prints the elasped time
   time.sleep(0.01) # Pause for 0.01 second to update the display

except KeyboardInterrupt: # Calculate the elasped time since the start time
    elasped_time = time.time() - start_time # Does the same thing as the one above
    minutes = int(elasped_time / 60)
    seconds = int(elasped_time % 60)
    hundreths = int((elasped_time % 1) * 100)
    print(f"\nStopped. Total time: {minutes:02d}:{seconds:02d}:{hundreths:02d}") # Prints the final elasped time 
