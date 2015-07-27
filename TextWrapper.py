import textwrap
import os
import sys
import subprocess

try:
    import Tkinter
    import tkMessageBox
    import tkFileDialog
    import ttk
except ImportError:
    import tkinter as Tkinter
    import tkinter.messagebox as tkMessageBox
    import tkinter.filedialog as tkFileDialog
    import tkinter.ttk as ttk

def makewrappedtext(filename, maxcharsinsingleline):
    unwrappedfile = open(filename, "r").read()
    writer = textwrap.fill(unwrappedfile, maxcharsinsingleline)
    WANTTOTRUNCATE = input("Would you like to overwrite the existing file (Y/n)?")
    positive_answer = ['yes', 'ye', 'y']
    negative_answer = ['no', 'n']
    answers = ['yes', 'ye', 'y', 'no', 'n']

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
    
def main()
    
    def startprocess():
        start.pack_forget()
        mainlabel.pack_forget()
        choosefile = ttk.Button(root, text="Choose File to TextWrap", command=openfile())
    
    root = Tkinter.Tk()
    root.title("TextWrapper")
    root.resizable(width=False, height=False)
    root.geometry('%dx%d+%d+%d' % (600, 500, ((root.winfo_screenwidth()/2)-(600/2)), ((root.winfo_screenheight()/2)-(500/2))))
    mainlabel = ttk.Label(root, text="TextWrapper", font=("Helevetica", 24))
    mainlabel.pack()
    mainlabel.place(x=205, rely=.25)
    copyrightlabel = Tkinter.Label(root, text="Copyright (c) 2015 Jonathan M. Stein", font=("Helevetica", 10))
    copyrightlabel.pack()
    copyrightlabel.place(relx=.63, rely=.96)
    start = ttk.Button(root, text="Start TextWrapper", command=startprocess())
    start.pack()
    start.place(x=249, rely=.35)
    
if __name__ == "__main__":

    A = tkFileDialog()
    B = int(input("What is the maximum amount of characters you want in a line of the \"text-wrapped\" file?\nNote: Spaces count.\n"))
    makewrappedtext(A, B)
    print("The script is complete.")
    print("The script shall now close. If you would like to \"text-wrap\" again, please restart the script.")
    sys.exit()
