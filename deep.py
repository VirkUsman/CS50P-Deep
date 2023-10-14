x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?  ")

x = x.lower()

x = x.strip()

x = x.replace("-", " ")

if x == "42" or x == "forty two":

        print("Yes")

else:
        print("No")