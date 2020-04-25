import time 
from termcolor import colored
from simpleeval import simple_eval
import random

class Bot:

    wait = 1
    
    def __init__(self,runtype='once'):
        self.q = ''
        self.a = ''
        self.runtype=runtype
        
    def _think(self,s):
        return s

    def _say(self,s):
        time.sleep(Bot.wait)
        print(colored(s,'green'))
        
    def _run_once(self):
        self._say(self.q)
        self.a = input()   
        self._say(self._think(self.a))
        
    def _run_looped(self):
        self._say(self.q)
        while True:
            self.a = input()
            if self.a.lower() in ['q','x','quit','exit']:
                break
            self._say(self._think(self.a))
            
    def run(self):
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'looped':
            self._run_looped()


class HelloBot(Bot):
    
    def __init__(self,runtype='once'):
        super().__init__(runtype)
        self.q = 'Hi,what is your name?'
        
    def _think(self,s):
        return f'Hello {s}！'    
            
        
class GreetingBot(Bot):
    
    def __init__(self,runtype='once'):
        super().__init__(runtype)
        self.q = 'How are you today?'
        
    def _think(self,s):
        if 'good' in s.lower():
            return 'I\'m feeling good too'
        else:
            return 'Sorry to hear that'       
            

class FavoriteColorBot(Bot):
    
    def __init__(self,runtype='once'):
        super().__init__(runtype)
        self.q = 'What is your favorite color?'
        
    def _think(self,s):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple']
        return f'You like {s.lower()}? My favorite color is {random.choice(colors)}'
    
class CalcBot(Bot):
    def __init__(self,runtype='once'):
        super().__init__(runtype)
        self.q = 'Through recent upgrade I can do calculation now.'
        
    def _think(self,s):
        result = simple_eval(s)
        return f'Done. Result = {result}'    


class Garfield:
    
    def __init__(self):
        self.bots = []
        
    def add(self,bot):
        self.bots.append(bot)
        
    def run(self):
        print('Welcome to Garfield dialog system. Let\'s talk.')
        print()
              
        for bot in self.bots:
            bot.run()
            
garfield = Garfield()
garfield.add(HelloBot())
garfield.add(GreetingBot())
garfield.add(FavoriteColorBot())
garfield.add(CalcBot('looped'))
garfield.run()