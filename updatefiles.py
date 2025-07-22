import os
import shutil

source_folder = r"C:\Users\ADMIN\Desktop\Source"
target_folder = r"C:\Users\ADMIN\Desktop\Target"

def move_text_files(src, dst):
    try:
        os.makedirs(dst, exist_ok=True)  # create target folder if missing
        files = os.listdir(src)  # get list of files
    except Exception as e:
        print(f"Error accessing folders: {e}")
        return

    moved_count = 0
    for filename in files:
        if filename.endswith(".txt"):
            src_path = os.path.join(src, filename)
            dst_path = os.path.join(dst, filename)
            try:
                shutil.move(src_path, dst_path)
                print(f"Moved: {filename}")
                moved_count += 1
            except Exception as e:
                print(f"Failed to move '{filename}': {e}")

    if moved_count == 0:
        print("No .txt files found to move.")
    else:
        print(f"Total files moved: {moved_count}")

if __name__ == "__main__":
    move_text_files(source_folder, target_folder)