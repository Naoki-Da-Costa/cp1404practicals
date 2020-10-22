import os


def main():
    extension_to_category = {}
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        file_extension = filename.split('.')[-1]
        if file_extension not in extension_to_category:
            category = input("What category would you like to sort {} files into? ".format(file_extension))
            extension_to_category[file_extension] = category
            try:
                os.mkdir(category)
            except FileExistsError:
                pass
        os.rename(filename, "{}/{}".format(extension_to_category[file_extension], filename))


main()
