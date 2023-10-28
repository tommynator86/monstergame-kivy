import random

class Items():
    
    def __init__(self):
        self.broetchen = 0
        self.fischbroetchen = 0
        self.pfannkuchen = 0
        
        self.eiszauber = 0
        self.feuerzauber = 0
        self.blitzzauber = 0
        
    def ben_broetchen(self):
        self.broetchen -= 1
        return 100
        
    def ben_fischbroetchen(self):
        self.fischbroetchen -= 1
        return 200
        
    def ben_pfannkuchen(self):
        self.pfannkuchen -= 1
        return 250
        
    def printlist(self):
        t = "Items: \n"
        t += "Brötchen: {}\n".format(self.broetchen)
        t += "Fisch-Brötchen: {}\n".format(self.fischbroetchen)
        t += "Pfannkuchen: {}\n".format(self.pfannkuchen)
        return t

class Character():
    
    def __init__(self,  name,  lvl):
        self.cname = name
        self.level = lvl
        self.health = 100 * self.level
        self.ep = 0
        self.attack_min = 10 * self.level
        self.attack_max = 50 * self.level
        self.items = Items()
        
    def levelup(self):
        print("{} ist einen Level aufgestiegen!".format(self.cname))
        t = "{} ist einen Level aufgestiegen!\n".format(self.cname)
        self.level += 1
        self.attack_min = 10 * self.level
        self.attack_max = 50 * self.level
        self.health += 10 * self.level
        self.ep = 0
        return t
        
    def geteplvlup(self):
        return (100 * self.level)
        
    def treffer(self,  char):
        #quote = char.attackpow * random() * char.level
        #char.attackpow = char.attackpow - quote
        t = ""
        lup = False
        quote = random.randint(char.attack_min, char.attack_max)
        self.health = self.health - quote
        char.ep = char.ep + quote
        if char.ep >= (100 * char.level):
            t += char.levelup()
            lup = True
        print("{} wurde getroffen (-{}HP)!".format(self.cname,  quote))
        t += "{} wurde getroffen (-{}HP)!\n".format(self.cname,  quote)
        return t,  lup

    def angriff(self,  achar):
        l = False
        print("{} greift an!".format(self.cname))
        t = "{} greift an!\n".format(self.cname)
        getroffen = random.randint(0, 100)
        if getroffen < 90:
            tx,  l = achar.treffer(self)
            #t += achar.treffer(self)
            t += tx
        else: 
            t+= "{} trifft daneben!\n".format(self.cname)
        return t,  l
        
    def dropitem(self,  echar):
        x = random.randint(0, 100)
        t = ""
        if x > 60:
            t+= "{} hat Item verloren:\n".format(self.cname) 
            i = random.randint(0, 100)
            if i < 30:
                if self.items.pfannkuchen > 0:
                    c = random.randint(1, self.items.pfannkuchen)
                    echar.items.pfannkuchen += c
                    t+= "{} hat {}x Pfannkuchen aufgesammelt\n".format(echar.cname,  c)
            elif i < 60:
                if self.items.fischbroetchen > 0:
                    c = random.randint(1, self.items.fischbroetchen)
                    echar.items.fischbroetchen += c
                    t+= "{} hat {}x Fischbrötchen aufgesammelt\n".format(echar.cname,  c) 
            elif i <= 100:
                if self.items.broetchen > 0:
                    c = random.randint(1, self.items.broetchen)
                    echar.items.broetchen += c
                    t+= "{} hat {}x Brötchen aufgesammelt\n".format(echar.cname,  c) 
            else:
                t+= "{} konnte Item nicht aufsammeln...\n".format(echar.cname) 
        return t
        
    def initrandomitems(self):
        self.items.broetchen = random.randint(0, 3)
        self.items.fischbroetchen = random.randint(0, 2)
        self.items.pfannkuchen = random.randint(0, 1)
        
        
    #def itemben(self,  index):
    #    if index == 0:
    #        if self.items.broetchen > 0:
    #            self.health += 100 * self.level
    #            print("{} isst ein Broetchen!".format(self.cname))
    #        else:
    #            print("Nicht verfügbar!")
    #    if index == 1:
    #        if self.items.fischbroetchen > 0:
    #            self.health += 200 * self.level
    #            print("{} isst ein Fischbroetchen!".format(self.cname))
    #        else:
    #            print("Nicht verfügbar!")
        
    #def status(self):
    #    print("Status von '{}'".format(self.cname))
    #    print("-Gesundheit: {}".format(self.health))
    #    epup = (100 * self.level)
    #    print("-Lvl:{}, EP:{}/{}".format(self.level,  self.ep,  epup))
    #    return self.level,  self.ep,  epup
        #print("-Angriffsp.: {}".format(self.attackpow))
