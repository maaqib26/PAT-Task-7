from datetime import datetime
# Importing datetime for displaying current timestamp

def text_file():
    # Created a function named "text_file()"
    
    current_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Getting the current date and time and saving to a variable
    print("Current Timestamp is", current_timestamp)
    # Printing the Current Timestamp
    f = open(r"C:\Users\moham\Downloads\PAT-Task-7\Task7.txt","x")
    # Creating a new text file
    f.write("Current Timestamp is:" + current_timestamp)
    # Adding Current Timestamp as content to the created text file
    f.close()
    # Closing the text file

# Calling the Function
text_file()


