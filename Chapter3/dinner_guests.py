invited = ['Ana', 'Aline', 'Cherie']
print("I found " + invited[0] + ", " + invited[1] + " and "+ invited[2] + " in a small table")
print("Look around, there is a bigger table. I'll call for more friends")
invited.insert(0, 'Matias')
invited.insert(1, 'John')
invited.append('Anthony')
print("Welcome guys... " + invited[0] + ", "  + invited[1] + " and "  + invited[-1])
print("The amount of people it's: ", + len(invited))
