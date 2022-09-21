# Anh Nguyen
# CSCI 102 – Section B
# Assessment 04A
# References: None
# Time: 45 minutes

# All inputs
comp_name = input("Enter company name: ")
comp_location = input("Enter company city/state: ")
comp_cashier = input("Enter cashier name: ")
item_1_name = input("Purchased item 1 name: ")
item_1_price = float(input("Purchased item 1 price: "))
item_2_name = input("Purchased item 2 name: ")
item_2_price = float(input("Purchased item 2 price: "))
item_3_name = input("Purchased item 3 name: ")
item_3_price = float(input("Purchased item 3 price: "))
thank_msg = input("Enter your favorite ending message: ")
print()

# Creating additional string variable to use in upcoming f string
gen_msg = "        RECEIPT GENERATOR"
welcome_msg = "Welcome Valued Customer"
item_msg = "    Item Name       Item Price"
line_msg = "-----------------------------------"
double_line_msg = "==================================="
total_price = "%.2f" % (item_1_price + item_2_price + item_3_price)

# Creating the massive output using f strings
superstring = (
  f"{gen_msg}\n"
  f"{line_msg}\n"
  f"    {comp_name}\n"
  f"    {comp_location}\n"
  f"{double_line_msg}\n"
  f"    Your cashier was: {comp_cashier}\n"
  f"    {welcome_msg}\n"
  f"{double_line_msg}\n"
  f"{item_msg}\n"
  f"    {item_1_name}        {item_1_price}\n"
  f"    {item_2_name}        {item_2_price}\n"
  f"    {item_3_name}        {item_3_price}\n"
  f"{double_line_msg}\n"
  f"    Total Cost of Order: {total_price}\n"
  f"{double_line_msg}\n"
  f"    {thank_msg}\n"
  f"{line_msg}"
)

# Printing the massive output
print(superstring)
