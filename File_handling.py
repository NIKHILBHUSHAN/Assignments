'''file=open("filehandling.txt","a")
file.write("Nikhil\n")
file.close()'''

'''file=open("filehandling.txt","r")
content=file.read()
print(content)
file.close()'''


'''with open("filehandling.txt","w") as file:
    file.write("My name is Yeddu Nikhil Bhushan\n")
    file.write("My father name is Appaiah\n")
    file.write("My Mother name is Padma\n")
    file.write("My brother name is Mourya Bhushan\n")'''

'''with open("filehandling.txt","a") as file:
    file.write("I am studying btech in SRM University")'''

'''with open("filehandling.txt", "r+") as file:
    # First, read the current count
    content = file.read()
    # Move cursor back to beginning
    #file.seek(0)
    
    # Write new count (overwrites old)
    #file.write("My family details:")
    print(content)
    
    # Remove any leftover characters
    #file.truncate()
    print(content)'''

'''with open("filehandling.txt","w+") as file:
    file.write("10+5=15\n")
    file.write("15*3=45\n")
    file.seek(0)
    for line in file:
        print(f"verified: {line.strip()}")'''

'''with open("filehandling.txt","r+") as file:
    file.write("11+5=16\n")
    file.write("15*3=45\n")
    file.seek(0)
    for line in file:
        print(f"verified: {line.strip()}")'''

'''with open("filehandling.txt","a+") as file:
    file.write("11*5=55")
    file.seek(0)
    for line in file:
        print(f"Verified: {line.strip()}")'''

'''try:
    with open("unique_log.txt", "x") as file:
        file.write("This file was just created!\n")
    print("File created successfully!")
except FileExistsError:
    print("Oops! File already exists. Not overwriting.")'''

'''import datetime
date=datetime.date.today()
filename=f"log_{date}"

try:
    with open(filename,"x") as file:
        file.write(f"log started on {date}")
    print(f"created new log {filename}")
except FileExistsError:
    print(f"Log for {date} already exist!")
    with open(filename,"a") as file:
        file.write("Additional entry\n")'''

'''with open("photo.jpg","rb") as file:
    image_data=file.read()
    #print(f"Image size: {len(image_data)} bytes")
with open("copy.jpg","wb") as duplicate:
    duplicate.write(image_data)'''

import struct

numbers = [10, 20, 30, 40, 50]

with open("data.bin", "wb") as file:
    for num in numbers:
        # Pack as 4-byte integer
        file.write(struct.pack('i', num))

    


