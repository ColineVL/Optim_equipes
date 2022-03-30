from repartition import repartirLesElevesEnEquipes
from programme import programmerAteliers

nbEquipes = 16
option = "collège"
nbTours = 4
# repartirLesElevesEnEquipes(nbEquipes, option)
# programmerAteliers(nbEquipes, nbTours, option)

nbEquipes = 10
option = "lycée"
nbTours = 2
repartirLesElevesEnEquipes(nbEquipes, option)
programmerAteliers(nbEquipes, nbTours, option)
