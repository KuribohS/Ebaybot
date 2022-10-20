from tkinter import *
from UploadProduct import Upload



#Window:
mainwindow = Tk()
mainwindow.title('Ebaybot')
mainwindow.geometry('800x600')

#Creating Entrys:
usernameEntry = Entry(mainwindow, width=20)
pwEntry = Entry(mainwindow, width=20)
sellprodEntry = Entry(mainwindow, width=20)
descriptionEntry = Entry(mainwindow, width=20)
picsEntry = Entry(mainwindow, width=20)
priceEntry = Entry(mainwindow, width=20)

#Creating Labels:
usernameLable = Label(mainwindow, text="Username:")
pwLable = Label(mainwindow, text="Password:")
sellprodLable = Label(mainwindow, text="Productname:")
descriptionLable = Label(mainwindow, text="Information about the Product:")
picsLable = Label(mainwindow, text="Path to the pic:")
priceLable = Label(mainwindow, text="Price:")


#packs:
usernameLable.pack()
usernameEntry.pack()

pwLable.pack()
pwEntry.pack()

sellprodLable.pack()
sellprodEntry.pack()

descriptionLable.pack()
descriptionEntry.pack()

picsLable.pack()
picsEntry.pack()

priceLable.pack()
priceEntry.pack()

def getInformation():
    username = usernameEntry.get()
    pw = pwEntry.get()
    sellprod = sellprodEntry.get()
    description = descriptionEntry.get()
    pics = descriptionEntry.get()
    price = priceEntry.get()
    print("START")
    upload = Upload(username, pw, sellprod, description, pics, price)
    upload.bypass()
    
    


#Button
goButton = Button(mainwindow, text="Upload the files!", command=lambda : getInformation() )
goButton.pack()
        

mainwindow.mainloop()