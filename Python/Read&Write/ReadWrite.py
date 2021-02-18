#r+ r w a
#File = open("ReadFile", "r")
#File = open("ReadFile1", "a")
#File = open("ReadFile", "w")
#print(File.readable())
#print(File.readlines()[1])
#print(File.read())
File = open("HtmlFile.html", "w")
File.write("<p>This is a HTML file </p>")
File.close()

