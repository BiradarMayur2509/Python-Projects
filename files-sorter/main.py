import os      # lets Python interact with your operating system (files, folders, paths)
import shutil  # used for high-level file operations like moving files

# step1 : select folder

folder_path = r"C:/Users/Mayur/Downloads"  # r"" → raw string (prevents issues with \ in Windows paths) 
                                           # You can change this to any folder you want

# step 2: file type categories
extensions = {
    "Images" : [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}

# Add other folder
extensions["Others"] = []
    
#step3 crete folder 

for folder in extensions.keys():
    folder_full_path = os.path.join(folder_path, folder)  # ex. C:/Users/Mayur/Downloads/Images
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)
        

 
# step 4: sort files

file_count = 0        # New 

for file in os.listdir(folder_path):   # os.listdir() → gets all items in the folder
    file_path = os.path.join(folder_path, file)   #ex. Downloads/photo.jpg
    
    if not os.path.exists(file_path):
        continue
    
    if os.path.isfile(file_path):    # Only processes actual files , Skips folders
        moved = False  # new
        
        for folder, ext_list in extensions.items():
            if folder == "Others":
                continue
            for ext in ext_list:
                if file.endswith(ext):
                    destination = os.path.join(folder_path, folder, file)
                    shutil.move(file_path, destination)
                    print(f"Moved: {file} -> {folder}")
                    file_count += 1
                    break
                
                if moved:
                    break

        # Moves unknown files

        if not moved:
            destination = os.path.join(folder_path, "Others", file)
            shutil.move(file_path, destination)
            file_count += 1  # New
            
# Final summary 
print("\nTotal files moved:", file_count)
