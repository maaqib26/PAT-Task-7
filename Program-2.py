def text_file(file_name):
    # Created a function named "text_file()"
    
    f = open(file_name,"r")
    # Reading the content of the text file
    file_content=f.read()
    f.close()
    # Closing the text file
    print("The content of the text file is", file_content)
    # Printing the content of the file into the console
    

# Calling the Function
file_name = r"C:\Users\moham\Downloads\PAT-Task-7\Task7.txt"
text_file(file_name)