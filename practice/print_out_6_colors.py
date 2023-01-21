#Print out 6 colors in a non repeating pattern
import itertools

colors = ['yellow', 'green', 'blue', 'red', 'pink', 'orange']

gem = [p for p in itertools.permutations(colors, 6)]

for i in gem:
#   print("Number of permutations are {} ".format(str(len(gem))))
    print(str(i))

#New comment