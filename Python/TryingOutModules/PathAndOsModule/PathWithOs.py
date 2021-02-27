from pathlib import Path
import os
#Note: all this can be done on a command prompt
print(Path.cwd()) #Current working directory...
print(os.chdir('C:\\Windows\\System32')) #Change directory
print(Path.cwd()) #Current working dir
print(Path.home()) # gives you the home directory
#os.makedirs('C:\\delicious\\pie\\pancakes') #Creates folder in C:\\
#Path(r'C:\Users\Sai\S').mkdir() #will create a folder in specified path
