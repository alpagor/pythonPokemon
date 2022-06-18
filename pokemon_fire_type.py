# Specialized class that use the base code of the main class
from pokemon import Pokemon

"""Represent aspects of a Pokémon, specific to fire Pokémon"""


class Fire_Pokemon(Pokemon):
    """This will initialize any attributes that were defined in the parent
    __init__() method and make them available in the child class."""

    def __init__(self, name: str, hp=100):
        super().__init__(name, hp)


