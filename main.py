from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window
from player import Character
import random
from kivy.core.audio import SoundLoader
import os, sys

class Monstergame():

    def __init__(self):
        self.neuesspiel()
        
    def neuesspiel(self):
        self.spieler = Character("Testplayer",  2)
        self.spieler.items.broetchen = 4
        self.spieler.items.fischbroetchen = 1
        self.monster = Character("Monster One",  1)
        self.gameover = False
        self.monsternum = 0
        self.playsound(4)
        
    def newmonster(self,  countup):
        newmlvl = random.randint(1, self.spieler.level)
        self.monster = Character("Monster {}".format(self.monsternum),  newmlvl)
        self.monster.initrandomitems()
        if countup == True:
            self.monsternum += 1
        return "Monster {} mit Lvl {} erscheint!\n".format(self.monster.cname,  newmlvl)
        
    def statusout(self):
        txt = "Status von '{}'\n".format(self.spieler.cname)
        txt += "-Gesundheit: {}HP\n".format(self.spieler.health)
        txt += "-Lvl:{}, EP:{}/{}\n".format(self.spieler.level,  self.spieler.ep,  self.spieler.geteplvlup())
        txt += self.spieler.items.printlist()
        txt += "\n"
        
        txt += "Status von '{}'\n".format(self.monster.cname)
        txt += "-Gesundheit: {}HP\n".format(self.monster.health)
        txt += "-Lvl:{}, EP:{}/{}\n".format(self.monster.level,  self.monster.ep,  self.monster.geteplvlup())
        txt += self.monster.items.printlist()
        #txt += "\n"
        return txt
        
    def angriff(self):
        t,  l = self.spieler.angriff(self.monster)
        if l == True:
            self.playsound(5)
        t += self.nextround()
        self.playsound(0)
        return t
        
    def nextround(self):
        text = ""
        t, l = self.monster.angriff(self.spieler)
        text += t #self.monster.angriff(self.spieler)
        if self.spieler.health < 1:
            text += "Game over!\n\n"
            self.gameover = True
            self.playsound(1)
        if self.monster.health < 1:
            text += "Monster '{}' ist tot!\n".format(self.monster.cname)
            text += self.monster.dropitem(self.spieler)
            text += self.newmonster(True)
            self.playsound(6)
        return text
        
    def flucht(self):
        t = self.newmonster(False)
        t += self.nextround()
        return t
        
    def itemben(self,  itemnum,  char):
        t = ""
        if self.gameover == False:
            if itemnum== 0:
                if char.items.broetchen > 0:
                    char.health += char.items.ben_broetchen() * char.level
                    t += "{} isst ein Brötchen (+{}HP)\n".format(char.cname,  100 *  char.level)
                    self.playsound(2)
                else:
                    t += "Kein Item mehr!\n"
                    self.playsound(3)
            elif itemnum == 1:
                if char.items.fischbroetchen > 0:
                    char.health += char.items.ben_fischbroetchen() * char.level
                    t += "{} isst ein Fisch Brötchen (+{}HP)\n".format(char.cname,  200 * char.level)
                    self.playsound(2)
                else:
                    t += "Kein Item mehr!\n"
                    self.playsound(3)
            elif itemnum == 2:
                if char.items.pfannkuchen > 0:
                    char.health += char.items.ben_pfannkuchen() * char.level
                    t += "{} isst einen Pfannkuchen (+{}HP)\n".format(char.cname,  250 * char.level)
                    self.playsound(2)
                else:
                    t += "Kein Item mehr!\n"
                    self.playsound(3)
            t += self.nextround()
        return t
        
    def playsound(self,  index):
        try:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            if index == 0:
                self.sound = SoundLoader.load(dir_path + '\Attack3.ogg')
            elif index == 1:
                self.sound = SoundLoader.load(dir_path + '\Gameover1.ogg')
            elif index == 2:
                self.sound = SoundLoader.load(dir_path + '\Item3.ogg')
            elif index == 3:
                self.sound = SoundLoader.load(dir_path + '\Item1.ogg')
            elif index == 4:
                self.sound = SoundLoader.load(dir_path + '\Mystery.ogg')
            elif index == 5:
                self.sound = SoundLoader.load(dir_path + '\Fanfare1.ogg')
            elif index == 6:
                self.sound = SoundLoader.load(dir_path + '\Down3.ogg')
            if self.sound:
                self.sound.play()
        except:
            pass

class MonsterWidget(BoxLayout):
    
    def btn_angreifen(self):
        print("angr")
        if mgame.gameover == False:
            tex = mgame.angriff()
            self.printinbox(tex)
        self.btn_status()
        
    def btn_heilen(self):
        print("heilen")
        self.ids.mainpanel.switch_to(self.ids.itempanel)

    def btn_status(self):
        print("status")
        tex = mgame.statusout()
        self.printinbox2(tex)
    
    def btn_flucht(self):
        print("flucht")
        if mgame.gameover == False:
            tex = mgame.flucht()
            self.printinbox(tex)
        self.btn_status()
    
    def btn_item1(self):
        self.ids.mainpanel.switch_to(self.ids.kampfpanel)
        tex = mgame.itemben(0,  mgame.spieler)
        self.printinbox(tex)
        self.btn_status()
        
    def btn_item2(self):
        self.ids.mainpanel.switch_to(self.ids.kampfpanel)
        tex = mgame.itemben(1,  mgame.spieler)
        self.printinbox(tex)
        self.btn_status()
        
    def btn_item3(self):
        self.ids.mainpanel.switch_to(self.ids.kampfpanel)
        tex = mgame.itemben(2,  mgame.spieler)
        self.printinbox(tex)
        self.btn_status()
        
    def btn_item4(self):
        pass
        
    def btn_item5(self):
        pass
        
    def btn_item6(self):
        pass
        
    def btn_neuesspiel(self):
        self.ids.mainpanel.switch_to(self.ids.kampfpanel)
        mgame.neuesspiel()
        self.ids.ausgabefeld.text = ""
        self.ids.ausgabefeld2.text = ""
        self.btn_status()
        
    def printinbox(self,  outp):
        self.ids.ausgabefeld.text += outp + '\n'
        
    def printinbox2(self,  outp):
        self.ids.ausgabefeld2.text = ""
        self.ids.ausgabefeld2.text += outp + '\n'
        

class GameUI(App):
    
    def build(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        Builder.load_file(dir_path + '\main.kv')
        mwid = MonsterWidget()
        mwid.btn_status()
        return mwid
        
    def on_stop(self):
        Window.close()
    
if __name__ == '__main__':
    mgame = Monstergame()
    GameUI().run()
    
    
