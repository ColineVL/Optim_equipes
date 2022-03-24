import math
from modelisation import College, Equipe


def init():
    arrayColleges = [College("Lautrec", 4), College("Fermat", 5)]
    arrayColleges.sort()

    nbEquipes = 2
    arrayEquipes = [Equipe(f"Equipe_{i}") for i in range(nbEquipes)]

    nbElevesTotal = sum([col.nbEleves for col in arrayColleges])
    maxParEquipe = math.ceil(nbElevesTotal / nbEquipes)

    return arrayColleges, arrayEquipes, nbEquipes, maxParEquipe
