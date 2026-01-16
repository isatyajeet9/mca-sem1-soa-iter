# A6Q3
# Question: What will be the output on executing each of the statements for:
#           address = 'Plot-6, Nayapalli, Bhubaneswar '
# Name: Satyajeet Nayak
# Appl No: 25C200429

address = "Plot-6, Nayapalli, Bhubaneswar "

print(len(address))
print(address[17:-1])
print(address[-len(address):len(address)])
print(address[:2] + address[-11:])
print(address.find("bhubaneswar"))
print(address.swapcase())
print(address.split(","))
print(address.isalpha())