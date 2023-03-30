import sys
import os


def generate_files(folder_name, number_files):
    try:
        os.makedirs(folder_name)
    except Exception:
        print('Folder already exist!')
        return

    for i in range(number_files):
        try:
            open(f'{folder_name}/{chr(97+i)}.cpp', 'w')
        except Exception:pass

if __name__ == "__main__":
    folder_name = (sys.argv[1]).upper()
    number_files = 5
    if len(sys.argv) > 2:
        number_files = int(sys.argv[2])
    generate_files(folder_name, number_files)