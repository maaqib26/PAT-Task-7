from datetime import datetime
# Importing datetime for displaying current timestamp

def text_file_write():
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

def text_file_read(file_name):
    # Created a function named "text_file()"
    
    f = open(file_name,"r")
    # Reading the content of the text file
    file_content=f.read()
    f.close()
    # Closing the text file
    print("The content of the text file is", file_content)
    # Printing the content of the file into the console
    
# Calling the Function
text_file_write()
# Calling the Function
file_name = r"C:\Users\moham\Downloads\PAT-Task-7\Task7.txt"
text_file_read(file_name)


