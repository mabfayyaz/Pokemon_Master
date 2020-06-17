# We will need pokemon types for later use, so lets define it here. Each type can be used to attack another pokemon and it has its associated value of impact.
pokemon_type = {

        "Fire":{"Fire":0.5 ,"Water":0.5 , "Ground":0 , "Air":0},
        "Water":{"Fire":2 ,"Water":0.5 , "Ground":2 , "Air":0},
        "Ground":{"Fire":2 ,"Water":0.25 , "Ground":0.25 , "Air":0},
        "Air":{"Fire":0.5 ,"Water":0 , "Ground":0 , "Air":0.25}
    }

# Let us define class using simple syntax of
# class Name:
class Pokemon:
    # Initialise some parameters everytime you call this class using
    # def __init__(self, parm1,param2...)
    #      self.parm1 = parm1 (and so on)

    def __init__ (self, name, pokemon_type, level):
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level
        self.health = level * 99
        self.max_health = level * 99
        self.is_knocked_out = False

    # For people using it return a meaningful string using
    #  def __repr__(self):
    #      return string
    def __repr__(self):
        return """The {name} has a type {type} and is at Level {level} with a
    health of {health} value.""".format(name=self.name, type=self.pokemon_type,level=self.level, health=self.health)
    # Now comes the methods to call for this class, such as reviving a pokemon, knocking out, gaining or losing health

    def revive(self):
        self.is_knocked_out = False

        if self.health == 0:
            self.health = 1
        print(f"The Pokemon {self.name} is revived.")


    def knocked_out(self):
        self.is_knocked_out = True

        if self.health != 0:
            self.health = 0
        print(f"The Pokemon {self.name} is knocked out.")
        # I have used two methods of print function. One uses a format of
        # "String is here {var_keywork}".format(var_keyword= name)
        # f"Here is the string with variables in {here}"

    def lose_health(self, value):
        self.health -= value

        if self.health <= 0:
            self.knocked_out()
        else:
            print("""The Pokemon {name} has lost health of value {value} and
            has now health of {new_health}.""".format(name=self.name, value= value,new_health=self.health))

    def gain_health(self, value):

        if self.health == 0:
            self.revive()

        self.health += value

        if self.health >= self.max_health:
            self.health = self.max_health
            print("Cannot add more health it is already at its highest value of {health}".format(health=self.health))
        else:
            print("""The Pokemon {name} has gain health of value {value} and
            has now health of {new_health}.""".format(name=self.name, value= value,new_health=self.health))



    def attack(self, other_pokemon, strength = "Normal"):
        self.strength = strength

        if self.is_knocked_out == True:
            print(f"Cannot attack because the Pokemon {self.name} is already knocked out!!")

        elif self.is_knocked_out == False and self.strength == "Normal":
            other_pokemon.lose_health(pokemon_type[self.pokemon_type][other_pokemon.pokemon_type] * 99)

        elif self.is_knocked_out == False and self.strength == "Strong":
            other_pokemon.lose_health(pokemon_type[self.pokemon_type][other_pokemon.pokemon_type] * 99 * 2)

        elif self.is_knocked_out == False and self.strength == "Weak":
             print(f"You are too weak to attack, regain health or try harder")





