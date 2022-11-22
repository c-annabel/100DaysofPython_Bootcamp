#pypi.org
#https://pokemondb.net/pokedex/game/x-y

#https://pypi.org/project/prettytable/
#https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki
# in ASCII
from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)