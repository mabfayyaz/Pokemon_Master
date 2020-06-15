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
            
            
    def attack(self, other_pokemon):
        if self.is_knocked_out == True:
            print(f"Cannot attack because the Pokemon {self.name} is already knocked out!!")
        
        else:
            other_pokemon.lose_health(pokemon_type[self.pokemon_type][other_pokemon.pokemon_type] * 99)
            


###########################################
# Once we have created our class we can instantiate it now
###########################################

Charmander = Pokemon("Charmander", "Fire",  5)
Squirltle =Pokemon("Squirlte", "Water", 7)
Bulbasaur = Pokemon("Bulbasaur", "Ground", 10)
Pikatchu = Pokemon("Pikatchu", "Air", 10)


##########################################
# Now Pokemon Master's Class #
##########################################

# A class to define
class Trainer:
    # Initialisation of class
    def __init__(self, name, pokemons_list, potents, current_pokemon):
        
        self.name = name
        self.pokemons_list = pokemons_list
        self.potents = potents
        self.current_pokemon = current_pokemon
        
        
        # Representation method to return string
    def __repr__(self):
        print(f"The trainer {self.name} has pokemons")
        for pokemon in self.pokemons_list:
            pokemon_name = pokemon.name
            print(pokemon_name)
        return "and the current pokemon is {current}".format(current =self.current_pokemon.name)

    # method to change current pokemon    
    def change_current_pokemon(self, new_name):

            
        if self.current_pokemon.is_knocked_out == True:
            print(f"Cannot change pokemon since {self.current_pokemon} is knocked out itself.")

        elif self.current_pokemon == new_name:
            print("Cannot change the same pokemon to itself.")
            
        else:
            self.current_pokemon = new_name
            print("The new current pokemon is {name}".format(name=new_name.name))
            
            
    def attack_other_trainer_pokemon(self, other_trainer):
        self.current_pokemon.attack(other_trainer.current_pokemon)
        
        # Use potent
    def use_potent(self):
        
        if self.current_pokemon.health <= 0 and self.potents != 0:
            self.current_pokemon.revive()
            self.potents -= 1
        elif self.current_pokemon.health > 0 and self.current_pokemon.health < self.current_pokemon.max_health and self.potents != 0:
            self.current_pokemon.gain_health(99)
            self.potents -= 1
            print(f"The pokemon {self.current_pokemon.name} has gained health and new health value is {self.current_pokemon.health}")
        elif self.current_pokemon.health >= self.current_pokemon.max_health and self.potents != 0:
            print("The pokemon {name} is already at its highest health level".format(name= self.current_pokemon.name))
        else:
            print("No more potents left to use.")
            
            
###########################################
# Once we have created our class we can instantiate it now
###########################################

trainer_one = Trainer("Asad", [Charmander, Squirltle, Pikatchu], 3, Squirltle)
trainer_two = Trainer("Bilal", [ Squirltle, Pikatchu, Bulbasaur], 5, Charmander)


###################################################
# You can now test it using different commands#####
###################################################


print(Charmander)
print(Squirltle)
print(Bulbasaur)
print(Pikatchu)
print(trainer_one)
print(trainer_two)
trainer_one.attack_other_trainer_pokemon(trainer_two)
trainer_two.attack_other_trainer_pokemon(trainer_one)
trainer_two.use_potent()
trainer_one.attack_other_trainer_pokemon(trainer_two)
trainer_two.change_current_pokemon(Squirltle)
trainer_two.change_current_pokemon(Charmander)
