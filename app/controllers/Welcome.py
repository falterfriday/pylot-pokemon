"""
CONTROLLER

"""
from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db

   
    def index(self):
        pokemons = []
        for x in range(1,152):
            pokemons.append("http://pokeapi.co/media/img/"+str(x)+".png")
        return self.load_view('index.html', pokemons=pokemons)

