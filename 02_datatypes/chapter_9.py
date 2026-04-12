essentials_spice = {"cardmom","ginger","cinnamom"}
optional_spices = {"cloves","ginger","black_paper"}

all_spices = essentials_spice | optional_spices
print(all_spices)

common_spices = essentials_spice & optional_spices
print(f"Common Spices : {common_spices}")

only_in_essential = essentials_spice - optional_spices
print(f" Essentails:  {only_in_essential}")
    
#membership test

print(f"Check CLoves Exists or not: {'cloves' in essentials_spice}")
print(f"Check Ginger Exists or not: {'ginger' in essentials_spice}")