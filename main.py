band_members = ["Jisoo", "Rosé", "Lisa", "Jennie"]
member = input("Enter a band member name: ")

if member in band_members:
    print("{} is a member of BLACKPINK".format(member))
else:
    print("{} is not a member of BLACKPINK".format(member))

# Slice a list. Leave off a range to slice to inclusive from beginning [:n] or through end [n:]
# Slice is inclusive of the first index in the range, exclusive of the second
# Make a copy of the whole list with [:]
sp_girls = ["Madison", "Olivia", "Nicole", "Ji-won", "Mei", "Ella", "Jessica"]
under_girls = sp_girls[2:6]
print(under_girls)

# Note that slicing like this is always making a copy of the list
# If you just pass a list into a new var, it is simply creating a new object reference
# to the *same list* and changing one will change the other
sp_girls_two = sp_girls
print(sp_girls_two)
sp_girls_two.pop()  # Pop the last element of the list off
print(sp_girls_two)  # Prints with Jessica popped off
print(sp_girls)  # Prints with Jessica popped off
