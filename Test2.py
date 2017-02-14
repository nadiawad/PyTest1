import os;

def rename_files():
    # Get file names in a folder
    mypath = r"/Users/Nadi/PycharmProjects/PyTest1/prank"
    file_list=os.listdir(mypath)
    print(file_list)
    current_location=os.getcwd();
    print(current_location)
    os.chdir(mypath)
    current_location = os.getcwd();
    print(current_location)
    # For each file rename filename
    for file_name in file_list:
        new_file_name=file_name.translate(None,"0123456789")
        os.rename(file_name,new_file_name)
        print(file_name+"---->"+new_file_name)
    print("RENAMING IS DONE SUCCESSFULLY!!!")
rename_files()