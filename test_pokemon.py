from Pokemon import Pokemon
from Trainer import Trainer
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
