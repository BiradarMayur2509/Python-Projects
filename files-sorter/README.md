# 📂 File Sorter using Python

## 🚀 Project Overview

This project is a simple Python automation script that organizes files in a folder based on their file types.

It scans a directory and automatically moves files into categorized folders like Images, Videos, Documents, and Music.

---

## 🎯 Features

* Automatically sorts files into categories
* Creates folders if they don’t exist
* Supports multiple file types
* Easy to customize

---

## 🛠 Technologies Used

* Python
* Built-in libraries:

  * os
  * shutil

---

## 📁 Project Structure

files-sorter/
│── main.py
│── README.md

---

## ⚙️ How It Works

1. Reads all files from a selected folder
2. Checks file extensions (.jpg, .mp4, .pdf, etc.)
3. Moves files into their respective folders

---

## ▶️ How to Run

1. Open the project folder
2. Update the folder path in `main.py`:

```python
folder_path = r"D:\Your\Folder\Path"
```

3. Run the script:

```bash
python main.py
```

---

## 📌 Example

Before:
Downloads/
photo.jpg
video.mp4
file.pdf

After:
Downloads/
Images/photo.jpg
Videos/video.mp4
Documents/file.pdf

---

## 🔥 Future Improvements

* Add GUI using Tkinter
* Add "Others" folder
* Show total files moved
* Improve UI/UX

---

## 🙌 Author

Mayur Biradar

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
