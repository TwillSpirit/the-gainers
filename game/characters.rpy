init python:
    class Actor():
        """docstring for Actor"""
        def __init__(self, character, name):
            self.character = character
            self.name = name
            
define dan = Actor(Character(name="Dan", image="Dan", color="#a58338"), "Dan")
define tamcin = Actor(Character(name="Tamcin", image="Tamcin", color="#282835"), "Tamcin")
define twill = Actor(Character(name="Twill", image="Twill", color="#282835"), "Twill")
define radio = Actor(Character(name="Radio",  color="#282835"), "Radio")