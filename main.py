import os
import re
from gui import *
from tkinter import filedialog


def get_new_index(num: int, offset: int) -> str:
    new_num = str(num + offset)
    while len(new_num) < 3:
        new_num = "0" + new_num

    return new_num


def ch_folder() -> str:
    return filedialog.askdirectory()


def merge(old_folder: str, new_folder: str) -> None:
    os.chdir(old_folder)

    ss_regex = re.compile(r"screenshot(\d{3,}).(jpg|png)")

    highest_num = 0
    for file in os.listdir():
        match = ss_regex.match(file)
        if match:
            highest_num = max(int(match.group(1)), highest_num)

    os.chdir(new_folder)

    count = 0
    for file in os.listdir():
        match = ss_regex.match(file)
        if match:
            count += 1
            os.rename(
                file,
                old_folder
                + "/screenshot"
                + get_new_index(int(match.group(1)), highest_num)
                + "."
                + match.group(2),
            )


if __name__ == "__main__":
    initModules()
    while isRunning():
        run()
