import textwrap
import os
import sys
import subprocess

# Bottom three modules are imported for technicalities.
# For all intents and purposes, they are not really *useful* to this script's purpose
# Ask someone who understands python. They'll agree.

def makewrappedtext(filename, maxcharsinsingleline):
    CHARTEST = True
    while CHARTEST == True:
        if (maxcharinsingleline.is_integer() == True and maxcharinsingleline >= 1):
            CHARTEST = False
        else:
            maxcharinsingleline = input("The amount of chars per line you chose is not an integer.\nPlease select a positive integer again:\n")
    EXISTTEST = True
    while EXISTTEST == True:
        if (os.path.exists(filename) and os.path.isfile(filename) and filename != __file__):
            EXISTTEST = False
        else: 
            filename = input("The file you chose either does not exist, or you chose this script itself.\nRemember to include the appropriate file extension.\nPlease select a file again:\n")
    unwrappedfile = open(filename, "r").read()
    writer = textwrap.fill(unwrappedfile, maxcharsinsingleline)
    WANTTOTRUNCATE = input("Would you like to overwrite the existing file (Y/n)?")
    positive_answer = ['yes', 'ye', 'y']
    negative_answer = ['no', 'n']
    answers = ['yes', 'ye', 'y', 'no', 'n']
    while WANTTOTRUNCATE.lower() not in answers: 
        WANTTOTRUNCATE = input("You did not input a valid answer.\nPlease choose 'Y' for yes or 'n' for no.\n")
    if WANTTOTRUNCATE.lower() in positive_answer:
        print("Okay, the original file will be overwritten.")
        wrappedname = filename
    if WANTTOTRUNCATE.lower() in negative_answer:
        print("Okay, a new file will be made in the same folder as the file you have selected, named TEXTWRAP{0}".format(filename))
        wrappedname = "TEXTWRAP{0}".format(filename)
        if (os.path.exists(wrappedname) and os.path.isfile(wrappedname)):
            WEIRDERROR = input("Warning. The file \"TEXTWRAP{0}\" already exists.\nContinuing would overwrite it.\nIs this okay? If the answer is no, the script shall pause so you can check the file,\nand when you commit whatever action necessary so that you feel safe continuing,\n(such as backing it up), you may continue the script.\nIs this okay (Y/n)?\n")
            while WEIRDERROR.lower() not in answers:
                WEIRDERROR = input("You did not input a valid answer.\nPlease choose 'Y' for yes or 'n' for no.\n")
            if WEIRDERROR.lower() in positive_answer:
                print("Okay, continuing as normal.")
            if WEIRDERROR.lower() in negative_answer:
                DUMMYINPUT = input("The script shall conntinue once you press enter.")
    unwrappedfile.close()
    wrappedfile = open(wrappedname, "w")
    wrappedfile.write(writer)
    wrappedfile.close()
    print("Operation Complete.")
    VIEW = input("Would you like to view {0}(Y/n)?".format(wrappedname))
    while VIEW.lower() not in answers:
        VIEW = input("You did not input a valid answer.\nPlease choose 'Y' for yes or 'n' for no.\n")
    if VIEW.lower() in positive_answer:
            print("Opening file in user default program.")
        if sys.platform == "win32":
            os.startfile(wrappedname)
        elif sys.platform == "darwin":
            subprocess.call(["open", wrappedname])
        else:
            subprocess.call(["xdg-open", wrappedname])
    if VIEW.lower() in negative_answer:
        pass
if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    filename = input("What file would you like to have \"text-wrapped\"?\n")
    maxcharsinsingleline = input("What is the maximum amount of characters you want in a line of the \"text-wrapped\" file?\nNote: Spaces count.\n")
    makewrappedtext(filename, maxcharsinsingleline)
    print("The script is complete.")
    print("The script shall now close. If you would like to \"text-wrap\" again, please restart the script.")
    sys.exit()
