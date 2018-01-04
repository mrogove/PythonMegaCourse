import datetime
"""
Use script to create empty file using now()
"""

filename = datetime.datetime.now()
#use strftime

#function to create empty file
def create_file():
    with open(filename.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file: #must cast as str
        file.write("")

create_file()
