from tkinter import messagebox
import GUIFunctions
import sys
import os


def get_resources_path(relative_path):
    try:
        file_name = relative_path.split("\\")[-1]
        base_path = sys._MEIPASS
        return os.path.join(base_path + "\\" + file_name)
    except Exception:
        base_path = os.path.realpath(__file__)
        base_path = base_path.replace("\\Utils.py", "")
        return os.path.join(base_path + "\\" + relative_path)


def get_entries(entries_to_get):
    for key, value in entries_to_get.items():
        if key == "entry_old_string":
            GUIFunctions.old_string = value.get()
        elif key == "entry_new_string":
            GUIFunctions.new_string = value.get()
        elif key == "entry_target_folder":
            GUIFunctions.target_folder = value.get()


def check_empty_entry(entries_to_check):
    for key, value in entries_to_check.items():
        if (key == "entry_old_string" and value == "") or (key == "entry_new_string" and value == ""):
            messagebox.showerror("Error", "Error: One or more entries is empty!")
            break

        elif key == "entry_target_folder":
            if value == "":
                messagebox.showerror("Error", "Error: One or more entries is empty!")
                break
            else:
                try:
                    os.chdir(value)
                    return True
                except FileNotFoundError:
                    messagebox.showerror("Error", "Error: The given path does not exist!")
                    break
    return False


def change_string(target_folder, old_string, new_string):
    for folders, subfolders, files in os.walk(target_folder):
        for file in files:
            try:
                with open(os.path.join(folders, file), mode="r") as old_file:
                    lines = old_file.readlines()
                    index = 0
                    for line in lines:
                        if old_string in line:
                            lines[index] = line.replace(old_string, new_string)
                        index += 1
                    old_file.close()
                with open(os.path.join(folders, file), mode="w") as new_file:
                    for line in lines:
                        new_file.write(line)
                    new_file.close()
            except UnicodeDecodeError:
                pass
            except PermissionError:
                messagebox.showerror("Error", "Error: You do not have permission to modify this folder. If in the "
                                              "target folder you have a git bash folder, this error is normal. "
                                              "Remove the folder, restart the program then put the folder back.")
                return False
        try:
            if old_string in folders:
                os.rename(folders, folders.replace(old_string, new_string))
                return True
        except PermissionError:
            messagebox.showerror("Error", "Error: The folder is opened in a file explorer. Close it and try again")
            return False
