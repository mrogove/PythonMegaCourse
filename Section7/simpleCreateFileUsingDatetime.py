import datetime
"""
Use script to create empty file using now()
"""

filename = datetime.datetime.now()
#use strftime
filename = filename.strftime("%Y-%m-%d-%H-%M")
#function to create empty file
def create_file():
    with open(str(filename),"w") as file: #must cast as str
        file.write("")

create_file()
