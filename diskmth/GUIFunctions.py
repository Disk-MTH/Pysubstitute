from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import webbrowser
import threading
import Utils
import os

global old_string
global new_string
global target_folder


def browse_to_github():
    webbrowser.open("https://github.com/Disk-MTH/Pysubstitute")


def browse_target_folder(entry_target_folder):
    entry_target_folder.delete(0, END)
    entry_target_folder.insert(0, filedialog.askdirectory(initialdir=os.environ["USERPROFILE"] + "\\Desktop",
                                                          title="Choose your target folder"))


def proceed(entry_old_string, entry_new_string, entry_target_folder):
    Utils.get_entries(entries_to_get={"entry_old_string": entry_old_string,
                                      "entry_new_string": entry_new_string,
                                      "entry_target_folder": entry_target_folder})

    if Utils.check_empty_entry(entries_to_check={"entry_old_string": old_string,
                                                 "entry_new_string": new_string,
                                                 "entry_target_folder": target_folder}):
        Utils.change_string(target_folder, old_string, new_string)