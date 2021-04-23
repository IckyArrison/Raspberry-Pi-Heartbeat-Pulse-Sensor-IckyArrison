from pulsesensor import Pulsesensor
import time
import datetime

# Init sensor
p = Pulsesensor()
# Start measuring Heartbeat
p.startAsyncBPM()

# Try to run code
try:
    # Run forever
    while True:
        # Prompt user for input and store key pressed
        input = input("\n\nReady to measure Heartbeat (y/n)?")
        # If user pressed 'y'
        if input == 'y':
            # Get current date & time
            now = datetime.datetime.now()
            filename = now.strftime("%b-%d-%Y-%H-%M-%S.txt")
            print("Saving to file name %s" % filename)
            # Open a file to append lines
            with open(filename, 'a') as file:
                # Run forever
                while True:
                    # Get BPM
                    bpm = p.BPM
                    # Init line variable
                    line = ""
                    # If bpm found
                    if bpm > 0:
                        # Format BPM save in line variable
                        line = "BPM: %d" % bpm
                    else:
                        # Not found message
                        line = "No Heartbeat found"
                    # Print line to console
                    print(line)
                    # Append line to file
                    file.write(line)
                    # Wait a second
                    time.sleep(1)
        else:
            print("Not ready")

# If error
except:
    # Stop measuring Heartbeat
    p.stopAsyncBPM()
