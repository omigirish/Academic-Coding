l1 = {"A011": 1450.00, "A012": 120.00, "A013": 250.00, "A015": 2000.00}  #CREATING A LIST
x=0
while x!=5 :
    x = int(input("\n\nPress 1. To add a new product to inventory\nPress 2. To delete a product from inventory\n"
                  "Press 3. To display the price of a particular product \nPress 4. To display total cost of inventory\n"
                  "Press 5. To Exit\n\nEnter your choice : "))
    if x==1 :
       key = input("\nEnter the product code starting with 'A' : ")
       price = float(input("\nEnter the price of the product : "))
       l1[key] = price  #ADDING NEW KEY AND VALUE TO THE DICTIONARY
       print("\nThis product is successfully stored in inventory!")
    elif x==2 :
        key = input("\nEnter the product code starting with 'A' to be deleted : ")
        del l1[key]  #DELETING THE SPECIFIED KEY AND ITS VALUE
        print("\nThe product is successfully deleted!")
    elif x==3 :
        key = input("\nEnter the product code starting with 'A' : ")
        price = float(l1.get(key)) #SPECIFYING PRICE OF PARTICULAR KEY
        print("\nThe price of this product is : ",price)
    elif x==4 :
        t = l1.values()
        w = sum(t)#TO DISPLAY TOTAL COST OF THE INVENTORY
        print("Total cost of inventory is:",w)
    elif x==5 :
        print("\n\nBye!")

