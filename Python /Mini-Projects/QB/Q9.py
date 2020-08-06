import os
class fileHandler():
    try:
        os.chdir("/Users/girishsalunke/Desktop/work")
    except OSError:
        print("Could not locate the directory....")
    def createNewFile(self,f1):
        try:
            file=open(f1,"a")
            file.close()
        except:
            print("Something went wrong couldnt create the file.")
    def saveData(self,f1):
        try:
            file=open(f1,"a")
            string=input("Enter the String u wish to Save...")
            file.write(string)
        except FileNotFoundError:
            print("The file u specified does not exist.")

    def searchData(self,word,f1):
        count=0
        try:
            f1=open(f1,"r")
            for wrd in f1.read().split(" "):
                if wrd==word:
                    count=count+1
        except:
            print("File not found...")
        return count

    def makedirectory(self,dir):
        try:
            os.mkdir(dir)
        except OSError:
            print("A problem occured directory making failed...")
    def renamefile(self,oldfilename,newfilename):
        try:
            os.rename(oldfilename,newfilename)
        except OSError:
            print("A problem occured could not rename file...")

    def movefile(self,f1,newdir):
        try:
            os.rename(f1,os.path.join(newdir,f1))
        except OSError:
            print("A problem occured....")
    def deletefile(self,f1):
        try:
            os.remove(f1)
        except FileNotFoundError:
            print("File doesnt exist...")


h=fileHandler()

#h.createNewFile("Write.txt")
#h.saveData("Write.txt")
#print(str(h.searchData(f1="Write.txt",word="hello")))
#h.deletefile("Write.txt")
#h.makedirectory("super")
#h.renamefile("Write.txt","read.txt")
#h.movefile("read.txt","super")

