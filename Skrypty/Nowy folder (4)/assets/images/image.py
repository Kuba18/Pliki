import os

# Bieżący folder
folder_path = "."

# Pobranie listy wszystkich plików w folderze
files = os.listdir(folder_path)

# Filtrowanie tylko plików .jpg (małe i wielkie litery)
jpg_files = [f for f in files if f.lower().endswith(".jpg")]

# Zmienianie nazw
for i, filename in enumerate(jpg_files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_name = f"zdjecie{i}.jpg"
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)

print("Zmieniono nazwy wszystkich plików JPG w bieżącym folderze.")
