import random

class Cargo:
    def __init__(self, name, price, vol, num, fluctuation = 1):
        # the price here is mean price and priceF is what is been displayed
        self.__name = name
        self.__price = price
        self.__vol = vol
        self.__num = int(num)
        self.__sigma = (price/4)/fluctuation
        self.__priceF = price
        self.__numF = num

    def __repr__(self):
        return 'The average price of {} in the current market is {}'.format(self.__name, self.__price)

    def getName(self):
        return self.__name

    def getPrice(self):
        return self.__price

    def getPriceF(self):
        return self.__priceF

    def getVol(self):
        return self.__vol

    def getNum(self):
        return self.__num

    def getNumF(self):
        return self.__numF

    def getSigma(self):
        return self.__sigma

    def setName(self, name):
        self.__name = name

    def setPrice(self, price):
        self.__price = price

    def setVol(self, vol):
        self.__vol = vol

    def setSigma(self, sigma):
        self.__sigma = int(sigma)

    def setNum(self, num):
        self.__num = int(num)

    def addNum(self, num):
        self.__num += num

    def addNumF(self, num):
        self.__numF += num

    def generateF(self):
        '''use random gaussian(slightly revised a little bit) to generate the final price and num to be displayed'''
        bias = round(random.gauss(self.__price, self.__sigma)) - self.__price
        if bias >= self.__sigma * 2 and bias < self.__sigma * 3:
            begin = self.__sigma * 2
            end = 2 * self.__price
            min_rate = 1
            max_rate = end/(3 * self.__sigma)
            numerator = bias - self.__sigma * 2
            rate = (numerator/(end - begin)) * (max_rate - min_rate) + min_rate
        elif bias >= self.__sigma * 3:
            begin = 2 * self.__price
            end = 8 * self.__price
            min_rate = 3
            max_rate = end/(3 * self.__sigma)
            numerator = bias - self.__sigma * 3
            rate = (numerator/(end - begin)) * (max_rate - min_rate) + min_rate
        else:
            rate = 1
        
        self.__priceF = round((self.__price + bias * rate))
        total = self.__price * self.__num
        if bias >= 0:
            self.__numF = round((total/(self.__priceF)) / (random.random()/5 + 1))
        else:
            self.__numF = round((total/(self.__priceF)) * (random.random()/5 + 1))
        
    def display_market(self, d_list):
        # d_list refers a turple of display elements
        d_list[0].set(self.__name)
        d_list[1].set(self.__priceF)
        d_list[2].set(self.__vol)
        d_list[3].set(self.__numF)
        d_list[4].set(0)
        

    def display_player(self, d_list):
        d_list[0].set(self.__name)
        d_list[1].set(round(self.__price))
        d_list[2].set(self.__vol)
        d_list[3].set(self.__num)
        d_list[4].set(0)
        

class Market:
    def __init__(self, name):
        self.__name = name
        self.__cargos = {}

    def getName(self):
        return self.__name

    def getCargos(self):
        return self.__cargos

    

    def setName(self, name):
        self.__name = name

    def setCargo(self, cargo):
        self.__cargos[cargo.getName()] = cargo

    

    def sold(self, d_list):
        market_cargo = self.__cargos[d_list[0].get()]
        num = d_list[4].get()
        if market_cargo.getNumF() >= num:
            market_cargo.addNumF(-num)
        else:
            print(market_cargo.getName(),"Not enough stock!")

    def bought(self, d_list):
        market_cargo = self.__cargos[d_list[0].get()]
        num = d_list[4].get()
        market_cargo.addNumF(num)
        

    def refresh(self):
        '''refresh final price and num of cargos stored in market'''
        for cargo in self.__cargos.values():
            cargo.generateF()
        
    def display_all(self, d_lists, index=0):
        '''display all the cargos market has'''
        cargo_list = [cargo for cargo in self.__cargos.values()]
        if len(cargo_list)%len(d_lists) != 0 or len(cargo_list) == 0:
            num = len(d_lists) - len(cargo_list)%len(d_lists)
            cargo_list = cargo_list + ["empty"] * num
        for n, d_list in enumerate(d_lists):
            f_n = n + index * len(d_lists)
            if type(cargo_list[f_n]) == Cargo:
                cargo_list[f_n].display_market(d_list)
            else:
                self.__display_empty(d_list)

    def __display_empty(self, d_list):
        '''display Empty if there is no more cargo to display on that page'''
        d_list[0].set("Empty")
        d_list[1].set(0)
        d_list[2].set(0)
        d_list[3].set(0)
        d_list[4].set(0)        
        
        


class Warehouse:
    # func is described as its names
    def __init__(self, name, cost, vol, isOwned = False):
        self.__name = name
        self.__cost = cost
        self.__vol = vol
        self.__isOwned = False

    def getName(self):
        return self.__name

    def getCost(self):
        return self.__cost

    def getVol(self):
        return self.__vol

    def setName(self, name):
        self.__name = name

    def is_owned(self):
        return self.__isOwned

    def setOwned(self, isOwned):
        self.__isOwned = isOwned

    def setCost(self, cost):
        self.__cost = cost

    def setVol(self, vol):
        self.__vol = vol
    

class Player:
    def __init__(self, money = 0):
        self.__money = money
        self.__warehouses = []
        self.__cargos = {}
        self.__vol = 100
        

    def getMoney(self):
        return self.__money

    def getWarehouses(self):
        return self.__warehouses

    def getCargos(self):
        return self.__cargos

    def getVol(self):
        return self.__vol

    def setMoney(self, money):
        self.__money = money

    def addMoney(self, amount):
        self.__money += amount

    def spendMoney(self, amount):
        if self.__money - amount >= 0:
            self.__money -= amount
        else:
            print("Not enough money!")

    def addWarehouse(self, warehouse):
        warehouse.setOwned(True)
        self.__warehouses.append(warehouse)

    def removeWarehouse(self, warehouse):
        warehouse.setOwned(False)
        self.__warehouses.remove(warehouse)

    def checkWarehouses(self):
        '''update the list of warehouses that is owned by player'''
        warehouses = []
        for warehouse in self.__warehouses:
            if warehouse.is_owned():
                warehouses.append(warehouse)
        self.__warehouses = warehouses

    def addCargo(self, d_list):
        '''when player does not have this type of cargo'''
        cargo_name = d_list[0].get()
        cargo_price = d_list[1].get()
        cargo_vol = d_list[2].get()
        cargo_num = d_list[4].get()
        self.__cargos[cargo_name] = Cargo(cargo_name,cargo_price,cargo_vol,cargo_num)
        moneySpent = cargo_price * cargo_num
        self.spendMoney(moneySpent)

    def removeCargo(self, cargo):
        self.__cargos.pop(cargo.getName())

    def buyCargo(self, d_list):
        if d_list[0].get() in self.__cargos:
            my_cargo = self.__cargos[d_list[0].get()]
            cargo_price = d_list[1].get()
            cargo_num = d_list[4].get()
            moneySpent = cargo_price * cargo_num
            total_price = my_cargo.getPrice() * my_cargo.getNum() + moneySpent
            total_num = my_cargo.getNum() + cargo_num
            if total_num != 0:
                my_cargo.setPrice(total_price/total_num)
                my_cargo.addNum(cargo_num)
                self.spendMoney(moneySpent)
        else:
            if d_list[4].get() > 0:
                self.addCargo(d_list)
            

    def sellCargo(self, d_list, sellPrice):
        my_cargo = self.__cargos[d_list[0].get()]
        sell_num = d_list[4].get()
        if my_cargo.getNum() >= sell_num:
            my_cargo.addNum(-sell_num)
            self.addMoney(int(sellPrice * sell_num))
            if my_cargo.getNum() == 0:
                self.removeCargo(my_cargo)
        else:
            print(my_cargo.getName(), "not enough")        
        

    def getVolF(self):
        '''get the total volume player has'''
        ex = 0
        for warehouse in self.__warehouses:
            ex += warehouse.getVol()
        return self.__vol + ex

    def getVolLeft(self):
        '''get the left volume player has'''
        ex = 0
        for warehouse in self.__warehouses:
            print(warehouse.getName())
            ex += warehouse.getVol()
        total = self.__vol + ex
        
        used = 0
        for cargo in self.__cargos.values():
            used += cargo.getVol() * cargo.getNum()
        return total - used

    def display_all(self, d_lists, index = 0):
        '''display all the cargos player has'''
        cargo_list = [cargo for cargo in self.__cargos.values()]
        if len(cargo_list)%len(d_lists) != 0 or len(cargo_list) == 0:
            num = len(d_lists) - len(cargo_list)%len(d_lists)
            cargo_list = cargo_list + ["empty"] * num
            
        for n, d_list in enumerate(d_lists):
            f_n = n + index * len(d_lists)
            if type(cargo_list[f_n]) == Cargo:
                cargo_list[f_n].display_player(d_list)
            else:
                self.__display_empty(d_list)

    def __display_empty(self, d_list):
        d_list[0].set("Empty")
        d_list[1].set(0)
        d_list[2].set(0)
        d_list[3].set(0)
        d_list[4].set(0) 


class Transport:
    def __init__(self, destination, bus={}, train={}, plane={}, boat={}):
        self.__destination = destination
        self.__transportations = {"bus": bus, "train": train, "plane": plane, "boat": boat}

    def getDestination(self):
        return self.__destination

    def getTransportations(self):
        return self.__transportations

    def setDestination(self, destination):
        self.__destination = destination

    def display(self, transportation, displayVars):
        '''display destinations, cost of days, price depends on the transportation'''
        displayVars[0].set(self.__destination)
        days = self.__transportations[transportation]["days"]
        displayVars[1].set(days)
        cost = self.__transportations[transportation]["cost"]
        displayVars[2].set(cost)
        if days == -1:
            displayVars[3].configure(state = "disabled")
        else:
            displayVars[3].configure(state = "normal")
        

class City:
    def __init__(self, name, market):
        self.__name = name
        self.__market = market
        self.__transports = []

    def getName(self):
        return self.__name

    def getMarket(self):
        return self.__market

    def getTransports(self):
        return self.__transports

    def setName(self, name):
        self.__name = name

    def setMarket(self, market):
        self.__market = market

    def addTransport(self, transport):
        self.__transports.append(transport)


    def display(self, transportation, d_lists):
        '''display information travel to other citys according to the transportation'''
        for n,transport in enumerate(self.__transports):
            transport.display(transportation, d_lists[n])
            
            
    
    








            
        
        

    



    
