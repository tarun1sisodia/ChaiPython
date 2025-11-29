space_mix = set()

print(f"Initial Spice Mix id:{id(space_mix)}")
space_mix.add("H2")
space_mix.add("o2")
print(f"After Space mix id  :{id(space_mix)}")
space_mix.add("Oxygen")
print(f"Content of Space {space_mix}")