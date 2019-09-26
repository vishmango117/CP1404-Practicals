
import os


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]
        # We could maintain a list/set of extensions we've made folders for (LBYL)
        # Or we could just "try" making folders again and ignore errors (EAFP)
        try:
            os.mkdir(extension)
        except FileExistsError:
            pass
        print("{}/{}".format(extension, filename))
        os.rename(filename, "{}/{}".format(extension, filename))


main()