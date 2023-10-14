x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?  ")

x = x.lower()

# print (x)

x = x.strip()

# print (x)

x = x.replace("-", " ")

# print (x)

if x == "42" or x == "forty two":

        print("Yes")

else:
        print("No")