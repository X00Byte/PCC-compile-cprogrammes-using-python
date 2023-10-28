import os
import subprocess

#Functions Declaration
def Intro():
    print("Where is the c Source code PATH ?")
    print("-> In the same directory with this script : '[*.c]       => Exemple : main.c'")
    print("-> Outside the directory                  : '/PATH/[*.c] => Exemple : /home/{user}/Documents/main.c'")
    programPATH=input()
    return programPATH

  
def compile(c_file_path, output_file_path):
    try:
        # Compile the C program using gcc (we will check later for gcc if installed)
        subprocess.check_output(['gcc', c_file_path, '-o', output_file_path])
        print(f"Compiled {c_file_path} successfully! Executable saved as {output_file_path}")
    except subprocess.CalledProcessError as e:
        #Print the error message (If compilation failed)
        print(f"Compilation failed:( :  {e}")
def File_Exist_Check_Extension(file_exists, file_extension):
    if not file_exists:
        #Check If File Exists
        print("FIle is not exesit \nCheck the PATH")
        quit()
    if file_extension != '.c' or file_extension == '':
        print("This is not a c programme -__- \nC programme Must have a '.c 'extension !")
        quit()
def getOutputName(file_name):
    print("Enter the output programme name \nNote :Type Enter To use Default name")
    outputName=input()
    if outputName == "" :
        outputName=file_name
    return outputName
#End Functions Declaration
programPATH=Intro()
#Get  extention & name
file_name, file_extension = os.path.splitext(programPATH)
file_exists = os.path.exists(programPATH)
File_Exist_Check_Extension(file_exists,file_extension)
outputName=getOutputName(file_name)
compile(programPATH,outputName)
