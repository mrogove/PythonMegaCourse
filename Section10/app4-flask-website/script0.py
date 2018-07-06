from flask import Flask #import Flask class from flask library.

app=Flask(__name__) #instantiate Flask class. 

@app.route('/')
def home():
	return("Website content goes here!")

if __name__=="__main__": #when you execute a python script, it executes the name __main__.
	app.run(debug=True)

#case 1: script executed: __name__ = "__main__"
#case 2: script imported: __name__ = "script0"