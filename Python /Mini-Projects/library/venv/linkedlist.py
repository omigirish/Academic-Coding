class node():
    def __init__(self,data=None):
        self.data=data
        self.next=None

class queue():
    def __init__(self):
        self.head=node()
        self.ptr=self.head

    def enqueue(self):     #appends a node to the end of the list
        x=input("Enter data to be saved in the node:")
        if self.head.data==None:
            self.head.data=x
        else:
            p=node(x)
            self.ptr.next=p
            self.ptr=p

    def dequeue(self):  #removes an element from the beginning of the queue
        if self.head!=None:
            self.head=self.head.next
        else:
            print("Cannot dequeue....List is empty")

    def __str__(self): #dunder method to print a list
        print("Linked list is: ")
        t=self.head
        if t==None:
            print("List is empty")
        while t!= None:
            print(t.data,end=" ")
            t=t.next
        print()
        return ""

l=queue()
choice=1

while choice==1:
    l.enqueue()
    str(l)
    choice = int(input("Wanna enqueue more(1/0)?"))
choice=1
while choice==1:
    choice=int(input("Wanna dequeue more(1/0)?"))
    l.dequeue()
    str(l)
