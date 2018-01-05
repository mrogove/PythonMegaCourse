import datetime
"""
Use script to create empty file using now()
"""
#variable for now time
now = datetime.datetime.now()
#use strftime

#function to create empty file
def create_file():
    with open(now.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("")
#create an identical dummy log for "tomorrow"
def create_tomorrow_file():
    now = datetime.datetime.now()
    after = now + datetime.timedelta(days=1)

    with open(after.strftime("%Y-%m-%d-%H-%M")+".txt","w") as file:
        file.write("")

create_file()
create_tomorrow_file()

#note that this does not give exact time differential
#this is because of calling datetime.datetime.now() twice
#rather than reusing the initial call. Leaving as example.
