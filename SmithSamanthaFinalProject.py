#Author: Samantha Smith
#Date written: 02/27/23
#Assignment: Final Project
#Short Desc: A burrito ordering application that allows the user to select a few filling options and place
#the order for it to be ready in fifteen minutes. 

#Import the needed libraries.
import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image, ImageTk
import random

#Set filling prices.
prices = {
    "Chicken" : 7,
    "Steak" : 8,
    "Romaine" : 1,
    "Rice" : 1,
    "Tomatoes" : 1,
    "Cheese" : 2,
}

#Create root window.
root  = Tk()
root.title("Build Your Burrito!")
root.iconbitmap('c:/GUI/newapp/Images/favicon.ico')

#Functions

#Generating a random Order ID when starting a new order
def ORDER_ID():
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    order_id = "BUR_"
    random_letters = ""
    random_digits = ""
    for i in range(0,3):
        random_letters += random.choice(letters)
        random_digits += str(random.choice(numbers))

    order_id += random_letters + random_digits
    return order_id #Return the generated order id to display at top of order section.

#Add to Order Button
def add():
    #Updating the transaction label
    current_order = orderTransaction.cget("text")
    added_filling = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")]) + "$ "
    updated_order = current_order + added_filling
    orderTransaction.configure(text=updated_order)

    #Updating the order total label
    order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
    order_total = order_total.replace("$", "")
    updated_total = int(order_total) + prices[displayLabel.cget("text")]
    orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#Remove Button Function
def remove():
    filling_to_remove = displayLabel.cget("text") + "...." + str(prices[displayLabel.cget("text")])
    transaction_list = orderTransaction.cget("text").split("$ ")
    transaction_list.pop(len(transaction_list) - 1)

    if filling_to_remove in transaction_list:
        #Update transaction label
        transaction_list.remove(filling_to_remove)
        updated_order = ""
        for item in transaction_list:
            updated_order += item + "$ "

        orderTransaction.configure(text = updated_order)

        #Update transaction total
        order_total = orderTotalLabel.cget("text").replace("TOTAL : ", "")
        order_total = order_total.replace("$", "")
        updated_total = int(order_total) - prices[displayLabel.cget("text")]
        orderTotalLabel.configure(text="TOTAL : " + str(updated_total) + "$")

#Display Button Functions
def displayChicken(): #Displays the fillings section with the chicken frame selected.
    chickenFillingFrame.configure(
        relief = "sunken",
        style = "SelectedFilling.TFrame"
    )
    romaineFillingFrame.configure(style = "FillingFrame.TFrame")
    cheeseFillingFrame.configure(style= "FillingFrame.TFrame")
    tomatoesFillingFrame.configure(style = "FillingFrame.TFrame")
    riceFillingFrame.configure(style = "FillingFrame.TFrame")
    steakFillingFrame.configure(style = "FillingFrame.TFrame")

    displayLabel.configure( #Configure the look of the chicken filling option in the fillings window when cheese is selected.
        image = chickenImage,
        text = "Chicken",
        font=('Helvetica', 12,"bold"),
        foreground="white",
        compound = "bottom",
        padding = (5, 5, 5, 5),
    )

def displaySteak(): #Displays the fillings section with the steak frame selected.
    steakFillingFrame.configure(
        relief = "sunken",
        style = "SelectedFilling.TFrame"
    )
    romaineFillingFrame.configure(style="FillingFrame.TFrame")
    cheeseFillingFrame.configure(style="FillingFrame.TFrame")
    tomatoesFillingFrame.configure(style="FillingFrame.TFrame")
    riceFillingFrame.configure(style="FillingFrame.TFrame")
    chickenFillingFrame.configure(style="FillingFrame.TFrame")
    displayLabel.configure( #Configure the look of the steak filling option in the fillings window when cheese is selected.
        text = "Steak",
        font = ('Helvetica', 12,"bold"),
        foreground = "white",
        image = steakImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayRomaine(): #Displays the fillings section with the romaine frame selected.
    romaineFillingFrame.configure(
        relief = "sunken",
        style="SelectedFilling.TFrame"
    )
    chickenFillingFrame.configure(style="FillingFrame.TFrame")
    cheeseFillingFrame.configure(style="FillingFrame.TFrame")
    tomatoesFillingFrame.configure(style="FillingFrame.TFrame")
    riceFillingFrame.configure(style="FillingFrame.TFrame")
    steakFillingFrame.configure(style="FillingFrame.TFrame")
    displayLabel.configure( #Configure the look of the romaine filling option in the fillings window when cheese is selected.
        text = "Romaine",
        font=('Helvetica', 12,"bold"),
        foreground="white",
        image = romaineImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayRice(): #Displays the fillings section with the rice frame selected.
    riceFillingFrame.configure(
        relief = "sunken",
        style="SelectedFilling.TFrame"
    )
    romaineFillingFrame.configure(style="FillingFrame.TFrame")
    cheeseFillingFrame.configure(style="FillingFrame.TFrame")
    tomatoesFillingFrame.configure(style="FillingFrame.TFrame")
    chickenFillingFrame.configure(style="FillingFrame.TFrame")
    steakFillingFrame.configure(style="FillingFrame.TFrame")
    displayLabel.configure( #Configure the look of the rice filling option in the fillings window when cheese is selected.
        text = "Rice",
        font=('Helvetica', 12,"bold"),
        foreground="white",
        image = riceImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayCheese(): #Displays the fillings section with the cheese frame selected.
    cheeseFillingFrame.configure(
        relief = "sunken",
        style="SelectedFilling.TFrame"
    )
    romaineFillingFrame.configure(style="FillingFrame.TFrame")
    chickenFillingFrame.configure(style="FillingFrame.TFrame")
    tomatoesFillingFrame.configure(style="FillingFrame.TFrame")
    riceFillingFrame.configure(style="FillingFrame.TFrame")
    steakFillingFrame.configure(style="FillingFrame.TFrame")
    displayLabel.configure( #Configure the look of the cheese filling option in the fillings window when cheese is selected.
        text = "Cheese",
        font=('Helvetica', 12,"bold"),
        foreground="white",
        image = cheeseImage,
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

def displayTomatoes(): #Displays the fillings section with the tomatoes frame selected.
    tomatoesFillingFrame.configure(
        relief = "sunken",
        style="SelectedFilling.TFrame"
    )
    romaineFillingFrame.configure(style="FillingFrame.TFrame")
    cheeseFillingFrame.configure(style="FillingFrame.TFrame")
    chickenFillingFrame.configure(style="FillingFrame.TFrame")
    riceFillingFrame.configure(style="FillingFrame.TFrame")
    steakFillingFrame.configure(style="FillingFrame.TFrame")
    displayLabel.configure( #Configure the look of the tomatoes filling option in the fillings window when cheese is selected.
        image = tomatoesImage,
        text = "Tomatoes",
        font=('Helvetica', 12,"bold"),
        foreground="white",
        compound = "bottom",
        padding=(5, 5, 5, 5),
    )

#Opening second window and displaying order information from the order button.
def order():
    top = Toplevel(root)
    top.title("Order Details")
    top.geometry("250x150")
    top.iconbitmap('c:/GUI/newapp/Images/favicon.ico')

#Second Window Labels.
    myOrder = Label(top, text="Thank you for your order!", width=20)
    myOrder.grid(row = 1, column = 0, columnspan = 3, sticky = "NSEW")

    myReceipt = Label(top, text="It will be ready in 15 minutes!")
    myReceipt.grid(row = 2, column = 0, columnspan = 3, sticky="NSEW")
#Second Window Close Button.
    buttonClose = ttk.Button(top,text="Ok",command=top.destroy, width=40) 
    buttonClose.grid(row = 3, column = 0, columnspan = 3, sticky="NSEW")
    
#STYLING AND IMAGES

#Style configurations
s = ttk.Style()
s.configure('MainFrame.TFrame', background = "#2B2B28") #Configure the look of the main frame.
s.configure('MenuFrame.TFrame', background = "#4A4A48") #Configure the look of the menu frame.
s.configure('DisplayFrame.TFrame', background = "#0F1110") #Configure the look of the display frame.
s.configure('OrderFrame.TFrame', background = "#B7C4CF") #Configure the look of the order frame.
s.configure('FillingFrame.TFrame', background = "#4A4A48", relief = "raised") #Configure the look of the filling frame.
s.configure('SelectedFilling.TFrame', background = "#C4DFAA") #Configure the look of the selected filling frame.
s.configure('MenuLabel.TLabel', #Configure the look of the menu label.
            background = "#0F1110",
            font = ("Arial", 13, "italic"),
            foreground = "white",
            padding = (5, 5, 5, 5),
            width = 21
            )
s.configure('orderTotalLabel.TLabel', #Configure the look of the order total label.
            background = "#0F1110",
            font = ("Arial", 10, "bold"),
            foreground = "white",
            padding = (2, 2, 2, 2),
            anchor = "w"
            )
s.configure('orderTransaction.TLabel', #Configure the look of the order transaction label.
            background = "#4A4A48",
            font = ('Helvetica', 12),
            foreground = "white",
            wraplength = 170,
            anchor = "nw",
            padding = (3, 3, 3, 3)
            )

#IMAGES

#Top Banner Images
LogoImageObject = Image.open("Images/burrito logo.png").resize((130, 130)) #Open the image for the top left logo image.
LogoImage = ImageTk.PhotoImage(LogoImageObject)

TopBannerImageObject = Image.open("Images/restaurant top banner burrito.png").resize((800, 130)) #Open the image for the top long banner.
TopBannerImage = ImageTk.PhotoImage(TopBannerImageObject)

#Menu Images
displayDefaultImageObject = Image.open("Images/display - Default.png").resize((350,360)) #Open the image for the display screens image for start of application.
displayDefaultImage = ImageTk.PhotoImage(displayDefaultImageObject)

chickenImageObject = Image.open("Images/fillings/chicken.png").resize((350,334)) #Open the image for the chicken filling option to populate the display screen when selected.
chickenImage = ImageTk.PhotoImage(chickenImageObject)

steakImageObject = Image.open("Images/fillings/steak.png").resize((350,334)) #Open the image for the steak filling option to populate the display screen when selected.
steakImage = ImageTk.PhotoImage(steakImageObject)

romaineImageObject = Image.open("Images/fillings/romaine.png").resize((350,334)) #Open the image for the romaine filling option to populate the display screen when selected.
romaineImage = ImageTk.PhotoImage(romaineImageObject)

riceImageObject = Image.open("Images/fillings/rice.png").resize((350,334)) #Open the image for the rice filling option to populate the display screen when selected.
riceImage = ImageTk.PhotoImage(riceImageObject)

tomatoesImageObject = Image.open("Images/fillings/tomatoes.png").resize((350,334)) #Open the image for the tomatoes filling option to populate the display screen when selected.
tomatoesImage = ImageTk.PhotoImage(tomatoesImageObject)

cheeseImageObject = Image.open("Images/fillings/cheese.png").resize((350,334)) #Open the image for the cheese filling option to populate the display screen when selected.
cheeseImage = ImageTk.PhotoImage(cheeseImageObject)

#WIDGETS

#Frames

#Section Frames
mainFrame = ttk.Frame(root, width = 800, height = 580, style = 'MainFrame.TFrame') #Set the size and place the main frame.
mainFrame.grid(row = 0, column = 0, sticky = "NSEW")

topBannerFrame = ttk.Frame(mainFrame) #Place the banner frame.
topBannerFrame.grid(row = 0, column = 0, sticky = "NSEW", columnspan = 3)

menuFrame = ttk.Frame(mainFrame, style = 'MenuFrame.TFrame') #Place the menu frame.
menuFrame.grid(row = 1, column = 0, padx = 3, pady = 3, sticky = "NSEW")

displayFrame = ttk.Frame(mainFrame, style = "DisplayFrame.TFrame") #Place the display frame.
displayFrame.grid(row = 1, column = 1, padx = 3, pady = 3, sticky = "NSEW")

orderFrame = ttk.Frame(mainFrame, style = "OrderFrame.TFrame") #Place the order frame.
orderFrame.grid(row = 1, column = 2, padx = 3, pady = 3, sticky = "NSEW")

#Filling Frames
chickenFillingFrame = ttk.Frame(menuFrame, style = "FillingFrame.TFrame") #Set the style configuration and place the chicken filling frame. 
chickenFillingFrame.grid(row = 1, column = 0, sticky = "NSEW")

steakFillingFrame = ttk.Frame(menuFrame,style ="FillingFrame.TFrame") #Set the style configuration and place the steak filling frame. 
steakFillingFrame.grid(row = 2, column = 0, sticky ="NSEW")

romaineFillingFrame = ttk.Frame(menuFrame, style ="FillingFrame.TFrame") #Set the style configuration and place the romaine filling frame. 
romaineFillingFrame.grid(row = 3, column = 0, sticky ="NSEW")

riceFillingFrame = ttk.Frame(menuFrame, style ="FillingFrame.TFrame") #Set the style configuration and place the rice filling frame. 
riceFillingFrame.grid(row = 4, column = 0, sticky ="NSEW")

tomatoesFillingFrame = ttk.Frame(menuFrame, style ="FillingFrame.TFrame") #Set the style configuration and place the tomatoes filling frame. 
tomatoesFillingFrame.grid(row = 5, column = 0, sticky ="NSEW")

cheeseFillingFrame = ttk.Frame(menuFrame, style ="FillingFrame.TFrame") #Set the style configuration and place the cheese filling frame. 
cheeseFillingFrame.grid(row = 6, column = 0, sticky ="NSEW")

#Top Banner Section
LogoLabel = ttk.Label(topBannerFrame, image = LogoImage, background = "#0F1110") #Top of application image for logo.
LogoLabel.grid(row = 0, column = 0, sticky = "W")

RestaurantBannerLabel = ttk.Label(topBannerFrame, image = TopBannerImage, background = "#0F1110") #Top of application image for banner.
RestaurantBannerLabel.grid(row = 0, column = 1, sticky = "NSEW")

#Fillings Section
MainMenuLabel = ttk.Label(menuFrame, text = "Filling Options", style = "MenuLabel.TLabel") #Filling Options Section Header.
MainMenuLabel.grid(row = 0, column = 0, sticky = "WE")
MainMenuLabel.configure(
    anchor = "center",
    font = ("Helvetica", 14, "bold")
)

ChickenFillingLabel = ttk.Label(chickenFillingFrame, text ="Chicken ..... 7$", style ="MenuLabel.TLabel") #Label displaying the chicken filling option and price.
ChickenFillingLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

SteakFillingLabel = ttk.Label(steakFillingFrame, text ="Steak ..... 8$", style ="MenuLabel.TLabel") #Label displaying the steak filling option and price.
SteakFillingLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

RomaineFillingLabel = ttk.Label(romaineFillingFrame, text ="Romaine ..... 1$", style ="MenuLabel.TLabel") #Label displaying the romaine filling option and price.
RomaineFillingLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

RiceFillingLabel = ttk.Label(riceFillingFrame, text ="Rice ..... 1$", style ="MenuLabel.TLabel") #Label displaying the rice filling option and price.
RiceFillingLabel.grid(row = 0, column = 0, padx =10, pady = 10, sticky = "W")

TomatoesFillingLabel = ttk.Label(tomatoesFillingFrame, text ="Tomatoes ..... 1$", style ="MenuLabel.TLabel") #Label displaying the tomatoes filling option and price.
TomatoesFillingLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

CheeseFillingLabel = ttk.Label(cheeseFillingFrame, text ="Cheese .... 2$", style ="MenuLabel.TLabel") #Label displaying the cheese filling option and price.
CheeseFillingLabel.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "W")

#Buttons
ChickenDisplayButton = ttk.Button(chickenFillingFrame, text ="Display", command = displayChicken) #Button to show the chicken filling frame.
ChickenDisplayButton.grid(row = 0, column = 1, padx = 10)

SteakDisplayButton = ttk.Button(steakFillingFrame, text ="Display", command = displaySteak) #Button to show the steak filling frame.
SteakDisplayButton.grid(row = 0, column = 1, padx = 10)

RomaineDisplayButton = ttk.Button(romaineFillingFrame, text ="Display", command = displayRomaine) #Button to show the romaine filling frame.
RomaineDisplayButton.grid(row = 0, column = 1, padx = 10)

RiceDisplayButton = ttk.Button(riceFillingFrame, text ="Display", command = displayRice) #Button to show the rice filling frame.
RiceDisplayButton.grid(row = 0, column = 1, padx = 10)

TomatoesDisplayButton = ttk.Button(tomatoesFillingFrame, text ="Display", command = displayTomatoes) #Button to show the tomatoes filling frame.
TomatoesDisplayButton.grid(row = 0, column = 1, padx = 10)

CheeseDisplayButton = ttk.Button(cheeseFillingFrame, text ="Display", command = displayCheese) #Button to show the cheese filling frame.
CheeseDisplayButton.grid(row = 0, column = 1, padx = 10)

#Order Section
orderTitleLabel = ttk.Label(orderFrame, text = "YOUR BURRITO") #Header Label
orderTitleLabel.configure(
    foreground="white", background="black",
    font=("Helvetica", 14, "bold"), anchor = "center",
    padding = (5, 5, 5, 5),
)
orderTitleLabel.grid(row = 0, column = 0, sticky = "EW")

orderIDLabel = ttk.Label(orderFrame, text = "ORDER ID : " + ORDER_ID()) #Display order ID below the header label.
orderIDLabel.configure(
    background = "black",
    foreground = "white",
    font = ("Helvetica", 11, "italic"),
    anchor = "center",
)
orderIDLabel.grid(row = 1, column = 0, sticky = "EW", pady = 1)

orderTransaction = ttk.Label(orderFrame, style = 'orderTransaction.TLabel') #Frame for the transaction list to display the burrito filling options selected.
orderTransaction.grid(row = 2, column = 0, sticky = "NSEW")

orderTotalLabel = ttk.Label(orderFrame, text = "TOTAL : 0$", style = "orderTotalLabel.TLabel") #Label that displays the current order total.
orderTotalLabel.grid(row = 3, column = 0, sticky = "EW")

orderButton = ttk.Button(orderFrame, text = "ORDER", command = order) #Order button at the bottom of the order section that 'places' the order and opens second window.
orderButton.grid(row = 4, column = 0, sticky = "EW")

#Display Section 
displayLabel = ttk.Label(displayFrame, image = displayDefaultImage) #Frame to show a burrito image at start and then filling that is selected.
displayLabel.grid(row = 0, column = 0 , sticky = "NSEW", columnspan = 2)
displayLabel.configure(background = "#0F1110")

addOrderButton = ttk.Button(displayFrame, text = "ADD TO ORDER", command = add) #Button to add the selected filling to the burrito order.
addOrderButton.grid(row = 1, column = 0, padx = 2, sticky = "NSEW")

removeOrderButton = ttk.Button(displayFrame, text = "REMOVE", command = remove) #Button to remove the selected filling from the burrito order. 
removeOrderButton.grid(row = 1, column = 1, padx = 2, sticky = "NSEW")

#GRID CONFIGURATIONS
mainFrame.columnconfigure(2, weight = 1)
mainFrame.rowconfigure(1, weight = 1)
menuFrame.columnconfigure(0, weight = 1)
menuFrame.rowconfigure(1, weight = 1)
menuFrame.rowconfigure(2, weight = 1)
menuFrame.rowconfigure(3, weight = 1)
menuFrame.rowconfigure(4, weight = 1)
menuFrame.rowconfigure(5, weight = 1)
menuFrame.rowconfigure(6, weight = 1)
orderFrame.columnconfigure(0, weight = 1)
orderFrame.rowconfigure(2, weight = 1)

root.mainloop() #Run the main loop for the application.
