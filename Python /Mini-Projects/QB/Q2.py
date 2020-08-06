import string
def count_word():
    with open("olivertwist.txt", 'r') as f:
        wcount=0
        lines=0
        chars=0
        while True:
            line = f.readline()
            if line =="":
                break
            lines=lines+1
            for word in line.split():
                LEN = 0
                for ch in string.punctuation:
                    word=word.replace(ch,"")
                for c in word.upper():
                    chars=chars+1
                    asci=ord(c)
                    if asci>=65 and asci<=90:
                       LEN=LEN+1
                    if LEN==len(word):
                        wcount=wcount+1
        f.seek(0)
        print("The laat 3 lines of the file are:")
        for line in (f.readlines()[-3:]):
            print(line, end=" ")
        print("\n")

    print ("Number of words are : "+str(wcount))
    print("Number of lines are : " + str(lines))
    print("Number of characters are : " + str(chars))

def word_frequency():
    wfreq=dict()
    with open("olivertwist.txt",'r') as f:
        while True:
            line = f.readline()
            if line =="":
                break
            for word in line.split():
                for ch in string.punctuation:
                    word=word.replace(ch,"")
                    word=word.upper()
                if word in wfreq.keys():
                    wfreq[word]=wfreq[word]+1
                else:
                    if word!="":
                        wfreq.update({word:1})
    dsort=sorted(wfreq.items(),key=lambda x:x[1],reverse=True)
    print("Dictionary in sorted format is:")
    print(dsort)
    print("The 3 most frequent words are:",end=" ")
    count=3
    for word,freq in dsort:
        print(word+"(f="+str(freq)+")",end=", ")
        count=count-1
        if count==0:
            break
    print("\n")
    for word,freq in dsort:
        if freq>1000:
            print(word+ " has frequency above 1000.")

count_word()
word_frequency()

