import pickle
f=open("file.txt","rb")

#l1=[(1,'janhavi','january','res',500),(1,'janhavi','february','res',400),(1,'janhavi','march','res',300),(1,'janhavi','april','res',100),(2,'janhavi','january','com',600),(2,'janhavi','february','com',900),(2,'janhavi','march','com',1000),(2,'janhavi','april','com',800)]
#pickle.dump(l1,f)
l1=pickle.load(f)
f.close()



cid = 4
total = 0.0

class user:

    def __init__(self,no,name,month,unit):
        self.month = month
        self.unit = unit
        self.no = no
        self.name = name

class residential(user):

    def __init__(self,no,name,month,unit,ctype='res'):
        self.month = month
        self.unit = unit
        self.no = no
        self.name = name
        self.ctype = ctype
        user.__init__(self,no,name,month,unit)
        t1 = (self.no,self.name,self.month,self.ctype,self.unit)
        l1.append(t1)


    def rbill(self):
        rname = input("Enter the name of the residential customer : ")
        c = 0
        global total
        for i in l1:
            if i[1] == rname and i[3] == 'res':
                self.calc_rbill(rname,i[2])
                c += 1
        if c != 0:
            print("-------------------------------------------------------", end="")
            print("\nThe total bill for {0} is : {1}".format(rname,total))
            total = 0.0
        else:
            print("Record not present.")


    def calc_rbill(self,rname,month):
        bill = 0.0
        global total
        v3 = 0.0
        v2 = 0.0
        v1 = 0.0
        for i in l1:
            if i[1] == rname and i[2] == month and i[3] == 'res':
                units = i[4]
                if units > 200.0 :
                    v3 = units - 200.0
                    v2 = 100.0
                    v1 = 100.0
                elif units > 100.0 and units <= 200.0:
                    v2 = units - 100.0
                    v1 = 100.0
                else :
                    v1 = units
                bill = v1*10.0 + v2*12.5 + v3*15.0
                total = total + bill
                print("\nBill Price for '{0}' -> '{1}' is : {2}".format(rname,month,bill))


class commercial(user):

    def __init__(self,no,name,month,unit,ctype='com'):
        self.month = month
        self.unit = unit
        self.no = no
        self.name = name
        self.ctype = ctype
        user.__init__(self,no,name,month,unit)
        t1 = (self.no, self.name, self.month, self.ctype, self.unit)
        l1.append(t1)


    def cbill(self):
        cname = input("Enter the name of the residential customer : ")
        c = 0
        global total
        for i in l1:
            if i[1] == cname and i[3] == 'com':
                self.calc_cbill(cname,i[2])
                c = 1
        if c == 1:
            print("-------------------------------------------------------", end="")
            print("\nThe total bill for {0} is : {1}".format(cname,total))
            total = 0.0
        else:
          print("\nRecord not present.")


    def calc_cbill(self,cname,month):
        bill = 0.0
        global total
        v3 = 0.0
        v2 = 0.0
        v1 = 0.0
        for i in l1:
            if i[1] == cname and i[2] == month and i[3] == 'com':
                units = i[4]
                if units > 200.0 :
                    v3 = units - 200.0
                    v2 = 100.0
                    v1 = 100.0
                elif units > 100.0 and units <= 200.0:
                    v2 = units - 100.0
                    v1 = 100.0
                else :
                    v1 = units
                bill = v1*12.0 + v2*15.0 + v3*20.0
                total = total + bill
                print("\nBill Price for '{0}' -> '{1}' is : {2}".format(cname,month,bill))


class main:

  def __init__(self):
    pass


  def addCon(self,utype):
      global cid
      counter = 0
      name = input("\nEnter name : ")
      month = input("\nEnter month (in words) : ")
      unit = int(input("\nEnter energy units consumed : "))
      for i in l1:
        if i[1] == name and i[3] == utype and i[2] == month:
            print("\nRecord already present.\n")
            counter = 1
            break
        elif i[1] == name and i[3] == utype:
            temp = int(i[0])
            t1 = (temp,name,month,utype,unit)
            l1.append(t1)
            print("\nEntry added successfully!")
            counter = 1
            break
      if counter != 1:
        cid += 1
        t1 = (cid,name,month,utype,unit)
        l1.append(t1)
        print("\nRecord added successfully!")


  def delete(self,utype):
      name = input("\nEnter name to be deleted : ")
      month = input("\nEnter the month : ")
      count = 0
      for i in l1:
          if name == i[1] and month == i[2] and utype == i[3]:
              l1.remove(i)
              print("\nRecord deleted successfully!")
              count = 1
              break
      if count != 1:
          print("\nRecord not present.")


  def display(self):
    print("The records in the list are : \n")
    for i in l1:
        print("{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}".format(i[0],i[1],i[2],i[3],i[4]))


  def menu(self):
    choice = 0
    r = residential(3,'xyz','january',123)
    c = commercial(4,'pqr','january',123)
    while choice !=5:
      choice = int(input("\n\n----- MENU -----\n1.Add Record\n2.Delete Record\n3.Generate Bill\n4.Display all records\n5.Exit\n\nEnter your choice : "))
      if choice == 1:
          value=int(input("\nPress :\t1.Residential\t2.Commercial : "))
          if value == 1:
            self.addCon('res')
          else:
            self.addCon('com')
      elif choice == 2:
          value=int(input("\nPress :\t1.Residential\t2.Commercial : "))
          if value == 1:
              self.delete('res')
          else:
              self.delete('com')
      elif choice == 3:
          value=int(input("\nPress :\t1.Residential\t2.Commercial : "))
          if value == 1:
              r.rbill()
          elif value == 2:
              c.cbill()
          else:
              print("\nInvalid input.")
      elif choice == 4:
          self.display()
      elif choice == 5:
          print("\n------------------------- END -------------------------")
          f=open("file.txt","wb")
          pickle.dump(l1,f)
          f.close()


      else:
          print("\nEnter valid choice!\n")

m = main()
m.menu()
