#Tuples

#they are immutable -- no change 

masala_spices = ("cardamom","cloves","cinnamom")

(spice1,spice2,spice3) = masala_spices

print(f"Main Masala Spices: {spice1}, {spice2}, {spice3}")

ginger_ratio , cardmom_ratio = 2,1

print(f"Ratio is G: {ginger_ratio} and Ratio is C: {cardmom_ratio}")

ginger_ratio ,cardmom_ratio = cardmom_ratio, ginger_ratio

print(f"Ratio is G: {ginger_ratio} and Ratio is C: {cardmom_ratio}")

#Membership testing

print(f"is Ginger in Masala Spice ?  {'ginger' in masala_spices}")
print(f"is Cinnamom in Masala Spice ?  {'cinnamom' in masala_spices}")