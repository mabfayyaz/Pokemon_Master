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
