chai_order =dict(type="Masala Chai",size="Large",sugar=2)
print(f"Chai Order:{chai_order}")

chai_recipe = {}

chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "Milk"

print(f"Chai Recipe:{chai_recipe}")

#to delete from the Dictionary
del chai_recipe["liquid"]

print(f"Chai Recipe:{chai_recipe}")

#membership 

print(f"Is Base available: {"base" in chai_recipe}")

print(f"Chai Recipe Keys :{chai_recipe.keys()}")

chai_order = {"type":"Ginger","size":"Medium","sugar":2}

print(f"Chai Order after long time: {chai_order}")

extra_spice = {"cardmom":"crushed","ginger":"sliced"}

print(f"Chai Keys: {chai_order.keys()}")

chai_recipe.update(extra_spice)
print(f"Chai Recipe: {chai_recipe}")

chai_recipe.update(chai_order)
print(f"Chai Recipe + Chai Order {chai_recipe}")


