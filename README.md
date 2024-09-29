Overview of the Code
Imports:

os: For interacting with the operating system, such as listing files and creating directories.
shutil: For file operations, specifically moving files.
Define Paths:

The source directory is set as path, which points to C:/Users/venka/OneDrive/Desktop/python_practice/.
It lists all files in the specified directory using os.listdir(path).
Folder Creation:

A list of folder names (folder_name) is defined to categorize the files.
The script checks if each folder exists and creates it if it doesn't.
File Moving:

The script iterates over each file in the directory:
If the file has a .jpg extension, it moves it to the "Image_file" folder.
If the file has a .doc extension, it moves it to the "Wrod_doc" folder (note the typo).
If the file has a .pdf extension, it moves it to the "PDF_Doc" folder.
If the file has a .mp4 extension, it moves it to the "Vedio_files" folder (also a typo).
If the file doesn't match any of these extensions, it prints a message indicating an invalid format.
