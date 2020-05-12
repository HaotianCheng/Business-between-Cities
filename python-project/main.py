import tkinter as tk
from tkinter import messagebox
from tkinter import font
from PIL import Image, ImageTk
from core import Cargo, Market, Warehouse, Player, Transport, City

class CareerLeague(tk.Tk):

    def __init__(self):
        '''Initiate frame container to switch frames'''
        tk.Tk.__init__(self)
        self.title("100 Days Challenge")
        tk.Tk.geometry(self, "500x300")

        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.a_font = font.Font(family='Helvetica', size=13, weight="bold")
        
        container = tk.Frame(self, bg = "blue", width = 500, height=300)
        container.pack()

        tframe = tk.Frame(container, bg = "red", width = 500, height=300)
        tframe.grid(row=0, column=0)

        self.frames = {}
        
        for F in (StartPage, GamePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky = 'NWSE')

        self.show_frame("StartPage")

        # do sth when user hits enter
        self.bind("<Return>", 
                        lambda event: 
                            self.event_func(self.frames["GamePage"]))
        
    def show_frame(self, page_name):
        '''switch frames in the frame container'''
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "GamePage":
            self.frames[page_name].reset()
        
     
    def event_func(self, frame):
        '''set frame foucus'''
        if "spinbox" in str(self.focus_get()):
            print (self.focus_get())
            self.focus_set()
    

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        '''Initiate StartPage layout'''
        tk.Frame.__init__(self, parent, bg = 'white', width = 500, height = 300)
        self.controller = controller
        label = tk.Label(self, text="100 Days Challenge", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Play",padx = 50, pady = 10,
                            command=lambda: controller.show_frame("GamePage"))

        button1.pack(pady=80)


class GamePage(tk.Frame):

    def __init__(self, parent, controller):
        '''Initiate GamePage layout'''
        tk.Frame.__init__(self, parent,  bg = 'red')
        self.controller = controller
        
        t = tk.Frame(self, bg = 'red', width = 150, height = 300)
        t.grid(row=0, column=0, sticky = 'NWSE')
        t = tk.Frame(self, bg = 'red', width = 350, height = 300)
        t.grid(row=0, column=1, sticky = 'NWSE')

        # several frames in GamePage
        menu = tk.Frame(self, bg = 'orange', width = 150, height = 300)
        menu.grid(row=0, column=0, sticky = 'NWSE')
        market = tk.Frame(self, bg = 'green', width = 350, height = 300)
        market.grid(row=0, column=1, sticky = 'NWSE')
        warehouse = tk.Frame(self, bg = 'black', width = 350, height = 300)
        warehouse.grid(row=0, column=1, sticky = 'NWSE')
        travel = tk.Frame(self, bg = 'cyan', width = 350, height = 300)
        travel.grid(row=0, column=1, sticky = 'NWSE')
        self.show(market)


        self.market_f = market
        
        
        #line breaker
        f=tk.Frame(self,height=300,width=2,bg="black")
        f.place(x = 148, y = 0)
        

        #menu stuff
        self.day_string = tk.StringVar()
        self.place_string = tk.StringVar()

        
        day_label = tk.Label(menu, textvariable=self.day_string, font=controller.title_font)
        day_label.pack(side="top", fill="x", pady=3)
        place_label = tk.Label(menu, textvariable=self.place_string, font=controller.title_font)
        place_label.pack(side="top", fill="x", pady=3)
        
        button1 = tk.Button(menu, text="Next Day",padx = 35, pady = 5,
                            command=lambda: self.nextDay(1))
        button2 = tk.Button(menu, text="Market",padx = 40, pady = 5,
                            command=lambda: self.show(market))
        button3 = tk.Button(menu, text="Warehouse",padx = 28, pady = 5,
                            command=lambda: self.show(warehouse))
        button4 = tk.Button(menu, text="Travel",padx = 43, pady = 5,
                            command=lambda: self.show(travel))
        button5 = tk.Button(menu, text="End",padx = 33, pady = 5,
                            command=lambda: controller.show_frame("StartPage"))
        
        button1.pack(pady=3)
        button2.pack(pady=3)
        button3.pack(pady=3)
        button4.pack(pady=3)
        button5.pack(pady=3)

        #market.grid_rowconfigure
        for i in range(6):
            market.grid_columnconfigure(i, weight=1)

        for i in range(8):
            market.grid_rowconfigure(i+2, weight=1)
        

        #market stuff
        b = tk.Label(market, text="", font=controller.a_font,bg = "yellow")
        b.grid(row=0, column=0, columnspan = 6, sticky="ew")
        b = tk.Label(market, text="", font=controller.a_font,bg = "red")
        b.grid(row=1, column=0, columnspan = 6, sticky="ew")

        self.marketVar = tk.StringVar()
        self.marketVar.set("Market")
        self.priceVar = tk.StringVar()
        self.priceVar.set("Price")
        self.stockVar = tk.StringVar()
        self.stockVar.set("Stock")
        
        market_label = tk.Label(market, textvariable=self.marketVar, font=controller.title_font,bg = "yellow")
        market_label.grid(row=0, column=0, columnspan = 6,sticky="ew")
        the_type_label = tk.Label(market, text="Type", font=controller.a_font,bg = "red")
        the_type_label.grid(row=1, column=0,sticky="w")
        the_price_label = tk.Label(market, textvariable=self.priceVar, font=controller.a_font,bg = "red")
        the_price_label.grid(row=1, column=1,sticky="w")
        the_vol_label = tk.Label(market, text="Vol.", font=controller.a_font,bg = "red")
        the_vol_label.grid(row=1, column=2,sticky="w")
        s_label = tk.Label(market, textvariable=self.stockVar, font=controller.a_font,bg = "red")
        s_label.grid(row=1, column=3, sticky="w")
        num_label = tk.Label(market, text="Num", font=controller.a_font,bg = "red")
        num_label.grid(row=1, column=4,columnspan=2, sticky="w")

        # put 6 turples of market display elements in a list
        self.display_lists = []
        for i in range(6):
            stringVar = tk.StringVar()
            numVar1 = tk.IntVar()
            numVar2 = tk.IntVar()
            numVar3 = tk.IntVar()
            numVar4 = tk.IntVar()
            stringVar.set("Empty")
            self.display_lists.append((stringVar,numVar1,numVar2,numVar3,numVar4))
            type_label = tk.Label(market, textvariable=stringVar, font=controller.a_font,bg = "green")
            price_label = tk.Label(market, font=controller.a_font,bg = "green", textvariable=numVar1)
            vol_label = tk.Label(market, font=controller.a_font,bg = "green", textvariable=numVar2)
            os_label = tk.Label(market, font=controller.a_font,bg = "green", textvariable=numVar3)
            num_entry = tk.Spinbox(market, from_=0, to=100000, width=1,textvariable=numVar4)
            type_label.grid(row=i+2,column=0, sticky="w")
            price_label.grid(row=i+2,column=1, sticky="w")
            vol_label.grid(row=i+2,column=2, sticky="w")
            os_label.grid(row=i+2,column=3, sticky="w")
            num_entry.grid(row=i+2,column=4,columnspan=2, sticky="ew")            
        
        # True if the current frame is market
        self.isMarket = True

        pre_button = tk.Button(market, text="Pre",command=lambda: self.switchPage(-1))
        pre_button.grid(row=8,column=0,columnspan = 2,sticky="ew")
        next_button = tk.Button(market, text="Next",command=lambda: self.switchPage(1))
        next_button.grid(row=8,column=2,columnspan = 3,sticky="ew")
        switch_button = tk.Button(market, text="$",command=lambda: self.switch_display())
        switch_button.grid(row=8,column=5,columnspan = 1,sticky="ew")         

        b = tk.Label(market, text="", font=controller.a_font,bg = "black")
        b.grid(row=9, column=0, columnspan = 6, sticky="ewsn")

        self.bsVar = tk.StringVar()
        self.bsVar.set("Buy")
        bs_button = tk.Button(market, textvariable=self.bsVar,command=lambda: self.deal())
        bs_button.grid(row=9,column=5,sticky="ew")
        
        self.moneyVar = tk.StringVar()
        self.volLeftVar = tk.StringVar()

        money_label = tk.Label(market, textvariable=self.moneyVar, font=controller.a_font,bg = "black", fg = "white")
        money_label.grid(row=9,column=0,columnspan = 2, sticky="w")
        volLeft_label = tk.Label(market, textvariable=self.volLeftVar, font=controller.a_font,bg = "black", fg = "white")
        volLeft_label.grid(row=9,column=2,columnspan = 3, sticky="w")
        
        #warehouse.grid_rowconfigure
        for i in range(5):
            warehouse.grid_columnconfigure(i, weight=1)

        for i in range(6):
            warehouse.grid_rowconfigure(i+1, weight=1)
        

        
        #warehouse stuff
        b = tk.Label(warehouse, text="", font=controller.a_font,bg = "yellow")
        b.grid(row=0, column=0, columnspan = 5, sticky="ew")
        b = tk.Label(warehouse, text="", font=controller.a_font,bg = "red",height = 1)
        b.grid(row=4, column=0, columnspan = 5, sticky="ew")

        warehouse_label = tk.Label(warehouse, text="Warehouse", font=controller.title_font,bg = "yellow")
        warehouse_label.grid(row=0, column=0, columnspan = 5,sticky="ew")

        warehouse0 = Warehouse("w0", 2000, 500)
        warehouse1 = Warehouse("w1", 10000, 2000)
        warehouse2 = Warehouse("w2", 100000, 20000)
        warehouse3 = Warehouse("w3", 500000, 100000)
        self.warehouses = (warehouse0,warehouse1,warehouse2,warehouse3)

        # read imgs and put them into list
        self.img_set = []
        for wh in self.warehouses:
            img = ImageTk.PhotoImage( Image.open("./images/"+wh.getName()+".jpg").resize((200,100)))
            img_label = tk.Label(warehouse, image=img, width = 200, height = 100, bg = "grey")
            img_label.image = img # make the img shown
            img_label.grid(row = 1, column = 0, rowspan = 3, columnspan = 5, sticky="ewns")
            self.img_set.append(img_label)

        self.costWVar = tk.StringVar()
        self.stockWVar = tk.StringVar()   

        cost_label = tk.Label(warehouse, textvariable=self.costWVar, font=controller.title_font,bg = "red", height = 1)
        cost_label.grid(row = 4, column = 0, columnspan = 3,sticky="ew")
        stock_label = tk.Label(warehouse, textvariable=self.stockWVar, font=controller.title_font,bg = "red", height = 1)
        stock_label.grid(row = 4, column = 3, columnspan = 2,sticky="ew")

        # own label appears when player owns the current displayed warehouse
        self.own_label = tk.Label(warehouse, text="Owned", font=controller.title_font,bg = "red", height = 1)
        self.own_label.grid(row = 2, column = 0,columnspan = 5, sticky="ew")

        self.own_label.grid_remove()

        self.bsWVar = tk.StringVar()
        self.bsWVar.set("Buy")
        
        pre_button2 = tk.Button(warehouse, text="Pre",command=lambda: self.preWarehouse())
        pre_button2.grid(row=5,column=0,sticky="ew")
        next_button2 = tk.Button(warehouse, text="Next",command=lambda: self.nextWarehouse())
        next_button2.grid(row=5,column=4,sticky="ew")
        bs_button2 = tk.Button(warehouse, textvariable=self.bsWVar,command=lambda: self.dealW())
        bs_button2.grid(row=5,column=1,columnspan = 3,sticky="ew")

        self.warehouseVar = tk.StringVar()
        
        money_label2 = tk.Label(warehouse, textvariable=self.moneyVar, font=controller.a_font,bg = "black", fg = "white")
        money_label2.grid(row=6,column=0,columnspan = 3, sticky="sw")
        warehouse_label2 = tk.Label(warehouse, textvariable=self.warehouseVar, font=controller.a_font,bg = "black", fg = "white")
        warehouse_label2.grid(row=6,column=3,columnspan = 2, sticky="sw")


        

        
        #travel.grid_rowconfigure
        for i in range(5):
            travel.grid_columnconfigure(i, weight=1)

        for i in range(6):
            travel.grid_rowconfigure(i+1, weight=1)

        
        #travel stuff
        b = tk.Label(travel, text="", font=controller.a_font,bg = "yellow")
        b.grid(row=0, column=0, columnspan = 5, sticky="ew")
        b = tk.Label(travel, text="", font=controller.a_font,bg = "red")
        b.grid(row=1, column=2, columnspan = 3, sticky="ewns")
        b = tk.Label(travel, text="", font=controller.a_font,bg = "black")
        b.grid(row=6, column=0, columnspan = 5, sticky="ewns")

        travel_label = tk.Label(travel, text="Travel", font=controller.title_font,bg = "yellow")
        travel_label.grid(row=0, column=0, columnspan = 5,sticky="nsew")

        img2 = ImageTk.PhotoImage( Image.open("./images/map.png").resize((100,200)))
        img_label2 = tk.Label(travel, image=img2, width = 100, height = 200, bg = "blue")
        img_label2.image = img2 # make the img shown
        img_label2.grid(row = 1, column = 0, rowspan = 4, columnspan = 2, sticky="ewns")
        
        city_label = tk.Label(travel, text="City", font=controller.a_font,bg = "red")
        city_label.grid(row=1, column=2,sticky="ew")
        daycost_label = tk.Label(travel, text="Days", font=controller.a_font,bg = "red")
        daycost_label.grid(row=1, column=3,sticky="ew")
        travelcost_label = tk.Label(travel, text="Cost", font=controller.a_font,bg = "red")
        travelcost_label.grid(row=1, column=4,sticky="ew")

        selected = tk.IntVar()

        # put 3 turples of city display elements in a list
        self.city_display_lists =[]
        for i in range(3):
            cityVar = tk.StringVar()
            daysVar = tk.IntVar()
            costVar = tk.IntVar()
            cityVar.set("Empty")
            city_rb = tk.Radiobutton(travel, textvariable=cityVar, font=controller.a_font, value=i, variable=selected,
                                    activebackground="cyan", bg = "cyan", command=lambda: self.enableTravel())
            city_rb.grid(row=i+2, column=2, sticky="ew")
            day_a = tk.Label(travel, font=controller.a_font,bg = "cyan", textvariable=daysVar)
            day_a.grid(row=i+2, column=3, sticky="ew")
            cost = tk.Label(travel, font=controller.a_font,bg = "cyan", textvariable=costVar)
            cost.grid(row=i+2, column=4, sticky="ew")
            self.city_display_lists.append((cityVar, daysVar, costVar, city_rb))


        


        selected2 = tk.StringVar()

        self.selectedCT = (selected, selected2)
                          
        self.bus_rb = tk.Radiobutton(travel, text="Bus", font=controller.a_font, value="bus", variable=selected2,
                                command=lambda: self.display_city())
        self.bus_rb.grid(row=5, column=0, sticky="ewns")
        train_rb = tk.Radiobutton(travel, text="Train", font=controller.a_font, value="train", variable=selected2,
                                  command=lambda: self.display_city())
        train_rb.grid(row=5, column=1, sticky="ewns")
        plane_rb = tk.Radiobutton(travel, text="Plane", font=controller.a_font, value="plane", variable=selected2,
                                  command=lambda: self.display_city())
        plane_rb.grid(row=5, column=2, sticky="ewns")
        boat_rb = tk.Radiobutton(travel, text="Boat", font=controller.a_font, value="boat", variable=selected2,
                                 command=lambda: self.display_city())
        boat_rb.grid(row=5, column=3, sticky="ewns")
        
        self.travel_button = tk.Button(travel, text="Go", font=controller.a_font, bg = "yellow",command=lambda: self.travel())
        self.travel_button.grid(row=5, column=4, sticky="ewns")
        
        money_label3 = tk.Label(travel, textvariable=self.moneyVar, font=controller.a_font,bg = "black", fg = "white")
        money_label3.grid(row=6,column=0,columnspan = 2, sticky="w")
        warehouse_label3 = tk.Label(travel, textvariable=self.warehouseVar, font=controller.a_font,bg = "black", fg = "white")
        warehouse_label3.grid(row=6,column=2,columnspan = 3, sticky="e")

        
        # initiate market A,B,C,D
        self.market_a = Market("A")
        self.market_a.setCargo(Cargo("Wine", 30, 20, 3000))
        self.market_a.setCargo(Cargo("Perfume", 600, 1, 1000))
        self.market_a.setCargo(Cargo("Car", 15000, 2000, 1000))
        self.market_a.setCargo(Cargo("Drug", 100, 1, 50))
        self.market_a.setCargo(Cargo("Seafood", 200, 15, 10))
        self.market_a.setCargo(Cargo("Jewelry", 3500, 5, 500))
        self.market_a.setCargo(Cargo("Fruit", 10, 3, 5000))
        self.market_a.setCargo(Cargo("Electronics", 1000, 10, 1000))
        self.market_a.setCargo(Cargo("Painting", 50000, 100, 10))
        self.market_a.setCargo(Cargo("Clothes", 800, 30, 50))
        self.market_a.setCargo(Cargo("Sofa", 300, 500, 1500))
        self.market_a.setCargo(Cargo("Coffee", 15, 15, 100))

        market_b = Market("B")
        market_b.setCargo(Cargo("Wine", 20, 20, 800))
        market_b.setCargo(Cargo("Perfume", 500, 1, 100))
        market_b.setCargo(Cargo("Car", 25000, 2000, 100))
        market_b.setCargo(Cargo("Drug", 70, 1, 50))
        market_b.setCargo(Cargo("Seafood", 50, 15, 2000))
        market_b.setCargo(Cargo("Jewelry", 3600, 5, 10))
        market_b.setCargo(Cargo("Fruit", 20, 3, 100))
        market_b.setCargo(Cargo("Electronics", 1100, 10, 200))
        market_b.setCargo(Cargo("Painting", 40000, 100, 3))
        market_b.setCargo(Cargo("Clothes", 600, 30, 100))
        market_b.setCargo(Cargo("Sofa", 400, 500, 100))
        market_b.setCargo(Cargo("Coffee", 13, 15, 100))

        market_c = Market("C")
        market_c.setCargo(Cargo("Wine", 20, 20, 1000))
        market_c.setCargo(Cargo("Perfume", 400, 1, 500))
        market_c.setCargo(Cargo("Car", 20000, 2000, 300))
        market_c.setCargo(Cargo("Drug", 80, 1, 10))
        market_c.setCargo(Cargo("Seafood", 150, 15, 500))
        market_c.setCargo(Cargo("Jewelry", 3000, 5, 1000))
        market_c.setCargo(Cargo("Fruit", 10, 3, 2000))
        market_c.setCargo(Cargo("Electronics", 1200, 10, 100))
        market_c.setCargo(Cargo("Painting", 30000, 100, 30))
        market_c.setCargo(Cargo("Clothes", 500, 30, 1000))
        market_c.setCargo(Cargo("Sofa", 500, 500, 200))
        market_c.setCargo(Cargo("Coffee", 8, 15, 3000))

        market_d = Market("D")
        market_d.setCargo(Cargo("Wine", 10, 20, 2000))
        market_d.setCargo(Cargo("Perfume", 300, 1, 10))
        market_d.setCargo(Cargo("Car", 10000, 2000, 0))
        market_d.setCargo(Cargo("Drug", 60, 1, 100))
        market_d.setCargo(Cargo("Seafood", 250, 15, 0))
        market_d.setCargo(Cargo("Jewelry", 3300, 5, 100))
        market_d.setCargo(Cargo("Fruit", 5, 3, 10000))
        market_d.setCargo(Cargo("Electronics", 1300, 10, 0))
        market_d.setCargo(Cargo("Painting", 10000, 100, 0))
        market_d.setCargo(Cargo("Clothes", 300, 30, 250))
        market_d.setCargo(Cargo("Sofa", 250, 500, 10))
        market_d.setCargo(Cargo("Coffee", 15, 15, 0))

        # initiate city A,B,C,D
        city_a = City("A", self.market_a)
        city_a.addTransport(Transport("B", {"days": -1, "cost":-1},{"days": -1, "cost": -1}
                                      ,{"days": 1, "cost": 1000},{"days": 4, "cost": 50}))
        city_a.addTransport(Transport("C", {"days": 3, "cost":50},{"days": 2, "cost": 100}
                                      ,{"days": 1, "cost": 1500},{"days": 2, "cost": 60}))
        city_a.addTransport(Transport("D", {"days": 7, "cost":100},{"days": 3, "cost": 150}
                                      ,{"days": 2, "cost": 2000},{"days": -1, "cost": -1}))

        city_b = City("B",market_b)
        city_b.addTransport(Transport("A", {"days": -1, "cost":-1},{"days": -1, "cost": -1}
                                      ,{"days": 1, "cost": 1000},{"days": 4, "cost": 50}))
        city_b.addTransport(Transport("C", {"days": -1, "cost":-1},{"days": -1, "cost": -1}
                                      ,{"days": 1, "cost": 3000},{"days": 6, "cost": 60}))
        city_b.addTransport(Transport("D", {"days": -1, "cost":-1},{"days": -1, "cost": -1}
                                      ,{"days": 3, "cost": 4000},{"days": -1, "cost": -1}))

        city_c = City("C",market_c)
        city_c.addTransport(Transport("A", {"days": 3, "cost":50},{"days": 2, "cost": 100}
                                      ,{"days": 1, "cost": 1500},{"days": 4, "cost": 30}))
        city_c.addTransport(Transport("B", {"days": -1, "cost":-1},{"days": -1, "cost": -1}
                                      ,{"days": 1, "cost": 3000},{"days": 6, "cost": 60}))
        city_c.addTransport(Transport("D", {"days": 8, "cost":120},{"days": 4, "cost": 200}
                                      ,{"days": 2, "cost": 3000},{"days": -1, "cost": -1}))

        city_d = City("D",market_d)
        city_d.addTransport(Transport("A", {"days": 7, "cost":100},{"days": 3, "cost": 150}
                                      ,{"days": 2, "cost": 2000},{"days": -1, "cost": -1}))
        city_d.addTransport(Transport("C", {"days": 8, "cost":120},{"days": 4, "cost": 200}
                                      ,{"days": 2, "cost": 3000},{"days": -1, "cost": -1}))
        city_d.addTransport(Transport("B", {"days": -1, "cost":-1},{"days": -1, "cost": -1}
                                      ,{"days": 3, "cost": 4000},{"days": -1, "cost": -1}))
        
                            
        self.citys = {"A":city_a,"B":city_b,"C":city_c,"D":city_d}
        
        

    def show(self, frame):
        '''show the frame'''
        frame.tkraise()
        self.focus_set()

    def nextDay(self, num):
        '''do stuff when next day comes'''
        self.day += num
        self.day_string.set("Day: " + str(self.day))
        self.focus_set()
        self.refresh()
        self.isMarket = False # this will make the following switch_display func switch market frame on top and set isMarket to True
        self.switch_display()
        self.daysCheck()
        

    def reset(self):
        '''reset everything'''
        self.player = Player(1000)
        self.currentCity = self.citys["A"]
        self.currentMarket = self.market_a
        self.indexM = 0
        self.indexP = 0
        self.refresh()
        self.isMarket = False
        self.switch_display()
        self.update_MW()
        self.initializeWarehouse()
        self.day = 0
        self.place = self.currentCity.getName()
        self.day_string.set("Day: " + str(self.day))
        self.place_string.set("Place: " + self.place)
        self.deselect()
        self.bus_rb.select()
        self.bus_rb.invoke()
        self.show(self.market_f)
        

    def initializeWarehouse(self):
        '''refresh(update) warehouse frame display'''
        self.img_set[0].tkraise()
        self.currentWarehouse = self.warehouses[0]
        self.costWVar.set("Cost: " + str(self.currentWarehouse.getCost()))
        self.stockWVar.set("Stock: " + str(self.currentWarehouse.getVol()))
        

    def refresh(self):
        '''refresh cargos' parameters in the current market and update every display element'''
        self.currentMarket.refresh()
        self.update_MW()
        self.place = self.currentCity.getName()
        self.place_string.set("Place: " + self.place)

    def display_market(self):
        '''display market'''
        self.currentMarket.display_all(self.display_lists, self.indexM)

    def display_player(self):
        '''display player'''
        self.player.display_all(self.display_lists, self.indexP)


    def display_city(self):
        '''display city'''
        transportation = self.selectedCT[1].get()
        self.currentCity.display(transportation, self.city_display_lists)
        self.deselect()

    def travel(self):
        '''do stuff when player travels to another city'''
        d_index = self.selectedCT[0].get()
        transportation = self.selectedCT[1].get()
        transport = self.currentCity.getTransports()[d_index]
        destination = transport.getDestination()
        cost = transport.getTransportations()[transportation]["cost"]
        days = transport.getTransportations()[transportation]["days"]
        if self.player.getMoney() >= cost:
            self.player.spendMoney(cost)
            self.currentCity = self.citys[destination]
            self.currentMarket = self.currentCity.getMarket()
            self.nextDay(days)
            self.indexM = 0
            self.indexP = 0
            self.display_city()
            self.deselect()
        else:
            messagebox.showinfo("Info", "not enough money")
            

    def update_MW(self):
        '''update money, volume left and total volume display'''
        self.moneyVar.set("Money: "+ str(self.player.getMoney()))
        self.volLeftVar.set("Vol.left: " + str(self.player.getVolLeft()))
        self.warehouseVar.set("Warehouse: " + str(self.player.getVolF()))

    def switch_display(self):
        '''switch display from cargos owned by market and cargos owned by player'''
        if self.isMarket:
            self.display_player()
            self.marketVar.set("Player")
            self.bsVar.set("Sell")
            self.priceVar.set("Avg.P")
            self.stockVar.set("Own")
            self.isMarket = False
        else:
            self.display_market()
            self.marketVar.set("Market")
            self.bsVar.set("Buy")
            self.priceVar.set("Price")
            self.stockVar.set("Stock")
            self.isMarket = True

    def buy(self):
        '''buy cargos from market'''
        final_price = 0
        final_vol = 0
        for d_list in self.display_lists:
            try:
                t = d_list[4].get()
            except:
                d_list[4].set(0)
            if d_list[0].get() != "Empty":
                price = d_list[1].get()
                num = d_list[4].get()
                stock = d_list[3].get()
                vol = d_list[2].get()
            if stock < num:
                messagebox.showinfo(d_list[0].get(), "not enough stock")
                return
            else:
                final_price += price * num
                final_vol += vol * num

        if self.player.getMoney() >= final_price:
            if self.player.getVolLeft() >= final_vol:
                for d_list in self.display_lists:
                    if d_list[0].get() != "Empty":
                        self.player.buyCargo(d_list)
                        self.currentMarket.sold(d_list)
            else:
                messagebox.showinfo("Info", "Not enough Vol. left!!!")
        else:
            messagebox.showinfo("Info", "Not enough money")
            return
        self.update_MW()
        self.display_market()
        self.focus_set()

    def sell(self):
        '''sell cargos to market'''
        for d_list in self.display_lists:
            try:
                t = d_list[4].get()
            except:
                d_list[4].set(0)
            if d_list[0].get() != "Empty":  
                num = d_list[4].get()
                own = d_list[3].get()
                if own < num:
                    messagebox.showinfo(d_list[0].get(), "not enough stock")
                    return
        for d_list in self.display_lists:
            if d_list[0].get() != "Empty":
                market_cargo = self.currentMarket.getCargos()[d_list[0].get()]
                sell_price = market_cargo.getPriceF()
                self.player.sellCargo(d_list, sell_price)
                self.currentMarket.bought(d_list)

        self.update_MW()
        self.display_player()
        self.focus_set()

    def deal(self):
        '''determine the button function on the same button'''
        if self.isMarket:
            self.buy()
        else:
            self.sell()

    def nextWarehouse(self):
        '''switch to the next warehouse display'''
        index = self.warehouses.index(self.currentWarehouse)
        if index < len(self.img_set)-1 :
            index += 1
            self.currentWarehouse = self.warehouses[index]
            self.img_set[index].tkraise()
            self.costWVar.set("Cost: " + str(self.currentWarehouse.getCost()))
            self.stockWVar.set("Stock: " + str(self.currentWarehouse.getVol()))
            self.checkOwned()
                

    def preWarehouse(self):
        '''switch to the previous warehouse display'''
        index = self.warehouses.index(self.currentWarehouse)
        if index > 0:
            index -= 1
            self.currentWarehouse = self.warehouses[index]
            self.img_set[index].tkraise()
            self.costWVar.set("Cost: " + str(self.currentWarehouse.getCost()))
            self.stockWVar.set("Stock: " + str(self.currentWarehouse.getVol()))
            self.checkOwned()

    def checkOwned(self):
        '''check if current warehouse is owned and update own label'''
        if self.currentWarehouse.is_owned():
            self.own_label.grid()
            self.own_label.tkraise()
            self.bsWVar.set("Sell")
        else:
            self.own_label.grid_remove()
            self.bsWVar.set("Buy")

    def dealW(self):
        '''do the deal when player buys or sells warehouse'''
        if self.currentWarehouse.is_owned():
            self.player.removeWarehouse(self.currentWarehouse)
            self.player.addMoney(self.currentWarehouse.getCost())
            self.checkOwned()
            self.update_MW()
        else:
            if self.player.getMoney() >= self.currentWarehouse.getCost():
                self.player.addWarehouse(self.currentWarehouse)
                self.player.spendMoney(self.currentWarehouse.getCost())
                self.checkOwned()
                self.update_MW()
            else:
                messagebox.showinfo("Info", "Not enough money")

    def deselect(self):
        '''deselect the radio-button in the city frame and disable the travel button'''
        self.selectedCT[0].set(-1)
        self.travel_button.configure(state = "disabled")
            
    def enableTravel(self):
        '''enable the travel button'''
        self.travel_button.configure(state = "normal")


    def switchPage(self,direction = 1):
        '''switch pages if market or player has num of types of cargos more than one page'''
        if self.isMarket:
            index = self.indexM + direction
            if len(self.currentMarket.getCargos())%len(self.display_lists) == 0:
                num = len(self.currentMarket.getCargos())//len(self.display_lists)
            else:
                num = len(self.currentMarket.getCargos())//len(self.display_lists) + 1
            if index >= 0 and index < num:
                self.indexM += direction
                self.display_market()
        else:
            index = self.indexP + direction
            if len(self.currentMarket.getCargos())%len(self.display_lists) == 0:
                num = len(self.player.getCargos())//len(self.display_lists)
            else:
                num = len(self.player.getCargos())//len(self.display_lists) + 1
            if index >= 0 and index < num:
                self.indexP += direction
                self.display_player()

    def daysCheck(self):
        '''check if days reaches 100'''
        if self.day > 100:
            self.controller.show_frame("StartPage")
            messagebox.showinfo("You reached 100 days!", "You earned "+str(self.player.getMoney()))


if __name__ == "__main__":
    app = CareerLeague()
    app.mainloop()
