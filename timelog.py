from datetime import datetime
import os

choice = input("Open a file or create a new file (new/open):\n")
while choice == '':
    choice = input("Please input a valid choice (new/open)\n")
if choice == 'new':
    choosefile = input("Type a name for your file.\n")
    file = f"{choosefile}.txt"
elif choice == 'open':
    file = input("Type file name:\n")
    while os.path.isfile(file) == False and file.endswith('.txt') == False:
        print("File not found, try again.\n")
        file = input()
    

print("Logger ready! Type 'exit' to quit")

while True:
    log = input()
    if log == 'exit':
        break
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"[{now}]   {log}\n")
