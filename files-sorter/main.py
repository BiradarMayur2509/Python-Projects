import os 
import shutil

# step1 : select folder

folder_path = r"C:/Users/Mayur/Downloads"  # change this according to u

# step 2: file type categories
extensions = {
    "Images" : [".jpg", ".png", ".jpeg"],
    "Videos": [".mp4", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"]
}

#step3 crete folder 

for folder in extensions.keys():
    folder_full_path = os.path.join(folder_path, folder)
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)
        
# step 4: sort files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        for folder, ext_list in extensions.items():
            for ext in ext_list:
                if file.endswith(ext):
                    destination = os.path.join(folder_path, folder, file)
                    
                    # fixed : move file
                    shutil.move(file_path, destination)
                    print(f"Moved: {file} -> {folder}")
                    break