from datetime import datetime
import os

choice = input(f"Open a file or create a new file (new/open):\n")
while choice == '':
    choice = input(f"Please input a valid choice (new/open)\n")
if choice == 'new':
    choosefile = input(f"Type a name for your file.\n")
    file = f"{choosefile}.txt"
elif choice == 'open':
    file = input(f"Type file name:\n")
    while os.path.isfile(file) == False and file.endswith('.txt') == False:
        print(f"File not found, try again.")
        file = input()
    

print("Logger ready! Type 'exit' to quit")

while True:
    log = input()
    if log == 'exit':
        break
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"[{now}]   {log}\n")