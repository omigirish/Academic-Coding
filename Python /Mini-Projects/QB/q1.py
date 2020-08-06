from tkinter import *
def interpret():
    with open(e1.get(),'r') as f:
        contents=f.readlines()
        readings=dict()
        temp_sum=0
        for index,record in enumerate(contents):
            contents[index]=record.strip()
            time,temp=record.strip().split(" ")
            readings.update({temp:time})
            temp_sum=temp_sum+float(temp)
    min_temp=str(sorted(readings)[0])
    max_temp=str(sorted(readings)[-1])
    s1="The minimum temperature recorded is: "+min_temp
    s2="Maximum temperature was obtained at "+readings[min_temp]
    s3="The Maximum temperature recorded is: "+max_temp
    s4="Maximum temperature was obtained at "+readings[max_temp]
    s5="The average temperature is: "+str(temp_sum/len(readings))
    s=s1+"\n"+s2+"\n"+s3+"\n"+s4+"\n"+s5
    l2["text"]=s

window=Tk()
window.geometry("600x300")
window.title("Interpret")
l1=Label(window,text="Enter name and path of file:")
l1.place(x=10,y=20)
e1=Entry(window)
e1.place(x=200,y=20)
b1=Button(window,text="Interpret",command=interpret)
b1.place(x=400,y=25)
l2=Label(window,text="Output will appear here.")
l2.place(x=50,y=70)
window.mainloop()
