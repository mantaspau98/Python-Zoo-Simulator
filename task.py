from datetime import datetime, timedelta
import random
import tkinter as tk
class Zoo:
   def __init__(self, monkeyList, giraffeList, elephantList):
      self.now = datetime.now()
      self.monkeyList = monkeyList
      self.giraffeList = giraffeList
      self.elephantList = elephantList

   def hourPass(self):
       #Add an hour to the time, reduce health for each animal separately
       self.now +=timedelta(hours=1)
       for item in self.monkeyList:
           item.reduceHealth()
       for item in self.giraffeList:
           item.reduceHealth()
       for item in self.elephantList:
           item.reduceHealth()

   def feedAnimals(self):
       #Create a random number for each animal species and increase their health
       monkeyNumber = random.randint(10,25)
       giraffeNumber = random.randint(10,25)
       elephantNumber = random.randint(10,25)
       for item in self.monkeyList:
           item.increaseHealth(monkeyNumber)
       for item in self.giraffeList:
            item.increaseHealth(giraffeNumber)
       for item in self.elephantList:
            item.increaseHealth(elephantNumber)

class Animal:
   def __init__(self, name):
      self.name = name
      self.health = float(100)
      self.isDead = False

   def increaseHealth(self,number):
       self.health = self.health + self.health*(number/100)
       if(self.health > 100.0):
           self.health = 100.0

class Monkey(Animal):
   def __init__(self, name):
         Animal.__init__(self, name)
   def reduceHealth(self):
       self.health = self.health - self.health*(random.randint(1,20)/100)
       if(self.health < 30.0):
           self.isDead = True

class Giraffe(Animal):
   def __init__(self, name):
         Animal.__init__(self, name)
   def reduceHealth(self):
       self.health = self.health - self.health*(random.randint(1,20)/100)
       if(self.health < 50.0):
           self.isDead = True

class Elephant(Animal):
   def __init__(self, name):
         Animal.__init__(self, name)
         self.canWalk = True
   def reduceHealth(self):
       self.health = self.health - self.health*(random.randint(1,20)/100)
       if(self.canWalk == False):
           self.isDead = True
       if(self.health < 70.0):
           self.canWalk = False
   #override method for elephant's health increse
   def increaseHealth(self,number):
       self.health = self.health + self.health*(number/100)
       if(self.health > 100.0):
           self.health = 100.0
       if(self.health >= 70.0):
           self.canWalk = True


class Application(tk.Frame):
    #create animals, initialize user interface
    def __init__(self, master=None):
        monkeyList = []
        giraffeList = []
        elephantList = []
        for i in range(5):
           monkeyList.append(Monkey("Monkey #"+str(i+1)))
           giraffeList.append(Giraffe("Giraffe #"+str(i+1)))
           elephantList.append(Elephant("Giraffe #"+str(i+1)))
        self.zoo = Zoo(monkeyList, giraffeList, elephantList)
        super().__init__(master)
        self.master = master
        self.pack()
        self.initUI()

    #initiate afer feed button press
    def feed(self):
        self.zoo.feedAnimals()
        self.updateZooInfo()

    #initiate afer hour button press
    def hour(self):
        self.zoo.hourPass()
        self.updateZooInfo()

    def updateZooInfo(self):
        #update information about zoo (time) and animals it has
        text=""
        self.T1.config(state='normal')
        for monkey in self.zoo.monkeyList:
            if(monkey.isDead == True):
                text+= monkey.name+" Health: Dead\n"
            else:
                text+= monkey.name+" Health:"+str(round(monkey.health,2))+" Alive\n"
        self.T1.delete(1.0, tk.END)
        self.T1.insert(tk.END, text)
        self.T1.config(state='disabled')

        text=""
        self.T2.config(state='normal')
        for giraffe in self.zoo.giraffeList:
            if(giraffe.isDead == True):
                text+= giraffe.name+" Health: Dead\n"
            else:
                text+= giraffe.name+" Health:"+str(round(giraffe.health,2))+" Alive\n"

        self.T2.delete(1.0, tk.END)
        self.T2.insert(tk.END, text)
        self.T2.config(state='disabled')

        text=""
        self.T3.config(state='normal')
        for elephant in self.zoo.elephantList:
            if(elephant.isDead == True):
                text+= elephant.name+" Health: Dead\n"
            else:
                text+= elephant.name+" Health:"+str(round(elephant.health,2))+" Alive\n"
        self.T3.delete(1.0, tk.END)
        self.T3.insert(tk.END, text)
        self.T3.config(state='disabled')
        self.time["text"] = "{:%d/%m/%y - %H:%M:%S}".format(self.zoo.now)


    def initUI(self):
        #initialize user interface and put everyting into places
        self.feedZoo = tk.Button(self, command=self.feed, text="Feed the Zoo")
        self.feedZoo.pack(side="left")

        self.hourPass = tk.Button(self, command=self.hour, text="Pass one hour")
        self.hourPass.pack(side="left")

        self.fr = tk.Frame (root)
        self.fr.pack(side="top")

        self.time = tk.Label(self.fr, text="{:%d/%m/%y - %H:%M:%S}".format(self.zoo.now))
        self.time.pack(side="bottom")

        self.fr1 = tk.Frame(self.fr)
        self.fr1.pack(side="left")

        self.fr2 = tk.Frame(self.fr)
        self.fr2.pack(side="left")

        self.fr3 = tk.Frame(self.fr)
        self.fr3.pack(side="left")


        w1 = tk.Label(self.fr1, text="Monkeys")
        w1.pack(side="top")
        self.T1 = tk.Text(self.fr1, height=6, width=30)
        self.T1.pack(side="top")
        text=""
        for monkey in self.zoo.monkeyList:
            text+= monkey.name+" Health:"+str(monkey.health)+" Alive\n"
        self.T1.insert(tk.END, text)
        self.T1.config(state='disabled')

        w2 = tk.Label(self.fr2, text="Giraffes")
        w2.pack(side="top")
        self.T2 = tk.Text(self.fr2, height=6, width=30)
        self.T2.pack(side="top")
        text=""
        for giraffe in self.zoo.giraffeList:
            text+= giraffe.name+" Health:"+str(giraffe.health)+" Alive\n"
        self.T2.insert(tk.END, text)
        self.T2.config(state='disabled')

        w3 = tk.Label(self.fr3, text="Elephants")
        w3.pack(side="top")
        self.T3 = tk.Text(self.fr3, height=6, width=30)
        self.T3.pack(side="top")
        text=""
        for elephant in self.zoo.elephantList:
            text+= elephant.name+" Health:"+str(elephant.health)+" Alive\n"
        self.T3.insert(tk.END, text)
        self.T3.config(state='disabled')

root = tk.Tk()
app = Application(master=root)
app.mainloop()
