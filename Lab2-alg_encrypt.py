# Anh Nguyen
# CSCI 101 – Section G
# Python Lab 2 
# References: Searched how to join a list
# Time: 1 hour and 5 minutes

# Getting inputs
l1 = input("LIST1> ")
l2 = input("LIST2> ")
l3 = input("LIST3> ")
l4 = list(input("LIST4> "))
l5 = input("LIST5> ")

l1_back = l1[-2:]
l1_front = l1[:-2]
l1 = l1_back + l1_front

l2 = l2[:-2]

l3_back_half = int(len(l3) / 2)
l3 = l3[-(l3_back_half):]

temp = l4[2]
l4[2] = l4[4]
l4[4] = temp
l4 = "".join(l4)

l5_half_int = int(len(l5) / 2)
l5_front_half = l5[:-(l5_half_int)]
l5_back_half = l5[-(l5_half_int):]
print("OUTPUT " + l5_front_half + " " + l1 + l2 + l3 + l4 + " " + l5_back_half)
