"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        for filename in filenames:
            file_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print("Renaming {} to {}".format(filename, get_fixed_filename(filename)))
            os.rename(file_name, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    filename = filename.replace(" ", "_").replace(".TXT", ".txt")
    previous_char = ""
    new_name = ""
    for char in filename:
        if char.isupper() and previous_char.isalpha():
            new_name += "_"
        if not previous_char.isalpha() and previous_char != "'":
            char = char.upper()
        new_name += char
        previous_char = char
    return new_name.replace(".Txt", ".txt")


main()
