"""
This script creates an empty file.
"""

filename = "example1.txt"

#create empty file
def create_file():
    """This function creates an empty file
        using the filename variable."""
    with open(filename,"w") as file:
        file.write("") #empty str

create_file():
