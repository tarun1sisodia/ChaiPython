
sugar_amount = 2
print(f"Intial sugar amount: {sugar_amount} teaspoons")
sugar_amount =12
print(f"Updated new Var: {sugar_amount}")
print(f"ID: 2{sugar_amount}")
print(f"ID: 12{sugar_amount}")

space_mix = set()

print(f"Initial Spice Mix id:{id(space_mix)}")
space_mix.add("H2")
space_mix.add("o2")
print(f"After Space mix id  :{id(space_mix)}")
space_mix.add("Oxygen")
print(f"Content of Space {space_mix}")