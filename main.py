from pokemon import Pokemon
from pokemon_fire_type import Fire_Pokemon

# Instantiated Objects (creating objects) from the class, with the class attributes and methods (thx to .__init__)
pikachu = Pokemon("Pikachu")
bulbasaur = Pokemon("Bulbasaur")

charmander = Fire_Pokemon("Charmander")

print(type(charmander.hp))