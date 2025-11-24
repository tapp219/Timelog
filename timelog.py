from datetime import datetime
import os

options = ['new', 'open']

choice = input("Open a file or create a new one (new/open):\n")
while choice.lower() not in options:
    choice = input("Invalid option, try again (new/open):\n")
if choice.lower() == 'new':
    file = input("Type a name for your file. Please specify the file type by typing it at the end of the name (.txt, .rtf, .log, etc.)\n")
    while os.path.exists(file):
        file = input("File already exists, try again.\n")
elif choice.lower() == 'open':
    file = input("Type file name:\n")
    while os.path.exists(file) == False:
        file = input("File not found, try again.\n")
    

print("Logger ready! Type 'exit' to quit")

while True:
    log = input()
    if log == 'exit':
        break
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"[{now}]   {log}\n")
