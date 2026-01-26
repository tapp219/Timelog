# Update: I added comments! Don't know why I didn't do this in the first place but here they are

from datetime import datetime
import os

# Options for choice function (self explanatory): 'new' to create a new file, 'open' to open an existing file
options = ['new', 'open']

# Prompts user to select option
choice = input("Open a file or create a new one (open/new):\n")

#If input is not in options, prompt user to try again
while choice.lower() not in options:
    choice = input("Invalid option, try again (new/open):\n")

# When user selects 'new'
if choice.lower() == 'new':
    file = input("Type a name for your file. Please specify the file type by typing it at the end of the name (.txt, .rtf, .log, etc.)\n")
    while os.path.exists(file):
        file = input("File already exists, try again.\n")

# When user selects 'open'
elif choice.lower() == 'open':
    file = input("Type file name:\n")
    while os.path.exists(file) == False:
        file = input("File not found, try again.\n")
    
# If all goes well and the program is ready to log user input
print("Logger ready! Type 'exit' to quit")

# Function that logs the user input along with the date and time
while True:
    log = input()
    if log == 'exit':
        break
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"[{now}]   {log}\n")

# And god help you if the program breaks because there is no error handling
