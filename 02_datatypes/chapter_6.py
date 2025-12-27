chai_type = "Ginger Chai"
customer_care = "Tarun"
print(f"Order For {customer_care} :{chai_type} Please!")


demo = "Aromatic and Bold"
print(demo[3])   # Output: m , because we are directly indexing the string.
print(demo[0:12:2])  # skipping the 2 values everytime
print(demo[3:-2])

print(f"To reverse a string directly use:: {demo[::-1]}")
label_text  =  "Tarun Siso@ia"
encoded_label = label_text.encode("utf-8")
print(encoded_label)
print(label_text)