init python:
    class Actor():
        """docstring for Actor"""
        def __init__(self, character, name):
            self.character = character
            self.name = name
            
define dan = Actor(Character(name="Dan", image="Dan"), "Dan")
define tamcin = Actor(Character(name="Tamcin", image="Tamcin"), "Tamcin")
define twill = Actor(Character(name="Twill", image="Twill"), "Twill")