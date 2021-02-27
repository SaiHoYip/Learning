from pathlib import Path #or enter pathlib.Path everywhere if no from
# print(Path('Soup','Meat','Eggs')) #for Windows /
# print(str(Path('spam','ham','veal'))) #for Linux \
Files = ['money.txt','name.csv','id.docx']
for files in Files:
    print(Path(r'C:\Users\Sai',files))
#You can join Path objects using the / operator
#Sai = r'C:\Users\Sai'
#S = 'Stuff'
#Sai + '\\' + S
#print('\\'.join([Sai,S]))
Main = Path('C:/Users/S')
Child = Path('Ss')
print(Main/Child)
