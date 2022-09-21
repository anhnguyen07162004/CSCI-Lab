# Anh Nguyen
# CSCI 102 – Section B
# Assessment 04B
# References: None
# Time: 20 minutes

# Initial variable that tracks what the amino acid is
acid = ""

# Inputs (saved as first three letters of each element)
car = int(input("CARBON> "))
hyd = int(input("HYDROGEN> "))
nit = int(input("NITROGEN> "))
oxy = int(input("OXYGEN> "))
sul = int(input("SULFUR> "))

# Branching statements to figure out what the acid is given the combination of elements
if car == 3:
  if sul == 0:
    acid = "Alanine"
  elif sul == 1:
    acid = "Cysteine"
elif car == 6:
  if hyd == 14:
    acid = "Arginine"
  elif hyd == 9:
    acid = "Histidine"
elif car == 4:
  acid = "Asparagine"
elif car == 5:
  acid = "Glutamine"

# Creating f strings to make printing the acid easier
element_string = (
  f"{car}C--{hyd}H--{nit}N--{oxy}O--{sul}S"
)

acid_string = (
  f"{acid}"
)

# Printing the result
print("OUTPUT ", element_string)
print("OUTPUT ", acid_string)
