# Pokémon is the "class"
class Pokemon:
    # constructor
    def __init__(self, name: str, hp: int):
        assert hp > 0, f"HP {hp} is not greater than zero, you probably are a zombie!"
        """
        attributes and methods are defined on the class; at class creation time and then at instantiate time 
        (create an object from class) you are given the "arguments" for those attributes and methods.
        """
        # Initialize attributes to describe a Pokémon. (plus encapsulation)
        self.__name = name
        self.__hp = hp
        # setting default value for experience attribute
        self.__experience = 0

    # setting read only attribute (encapsulation)
    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def experience(self):
        return self.__experience

    def evolve(self):
        pass

    def check_experience(self):
        # Print a statement showing the Pokémon's experience.
        print(f"This Pokémon has {self.experience} points of experience.")

    def update_experience(self, exp_points):
        # Print a statement showing the Pokémon's experience.
        self.__experience = self.__experience + exp_points

# Instantiated Objects (creating objects) from the class, with the class attributes and methods (thx to .__init__)
pikachu = Pokemon("Pikachu", 35)
bulbasaur = Pokemon("Bulbasaur", 45)
charmander = Pokemon("Charmander", 39)

print(type(charmander))
print(charmander.update_experience(15))
print(charmander.check_experience())
print(charmander.update_experience(25))
print(charmander.check_experience())


