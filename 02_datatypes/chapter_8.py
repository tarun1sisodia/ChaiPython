
ingredients = [ "water", "milk", "black_tea"]
ingredients.append("sugar") #adds in last of array.
print(f"Total Ingredients: {ingredients}")

ingredients.pop()
print(f"After Poping the last element/ Data : {ingredients}")

ingredients.remove('water')

print(f"After Water: {ingredients}")

# print(f"Ingredients: {ingredients.reverse()}")

spice_options = ["ginger", "Cardmom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(f"Chai and Chai Ingredients : {chai_ingredients}")

chai_ingredients.insert(2,"black_tea")
print(f"chai:{chai_ingredients}")

last_option = chai_ingredients.pop()
print(last_option)

chai_ingredients.reverse()
print(chai_ingredients)

chai_ingredients.sort()
print(chai_ingredients)

sugar_levels = [1,2,3,4,5]
print(f"Max of Sugar Level: {max(sugar_levels)}")
print(f"Min of Sugar Level: {min(sugar_levels)}")

base_liquid  = ["water","milk"]
extra_flavour = ["ginger"]

print(f"Liquid Mixture: {base_liquid+extra_flavour}")

strong_brew = ["black tea"] * 3

print(f"Brew: {strong_brew}")