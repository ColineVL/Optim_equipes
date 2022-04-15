import math as m
from modelisation import Equipe, Team, Atelier


def initEquipes():
    colleges = [
        "Emile Zola",
        "Hubertine Auclert",
        "Vauquelin",
        "Claude Nougaro",
        "George Sand",
        # "Jolimont",
        "Bagatelle",
        "Jean Jaurès",
        "Fermat 1",
        "Fermat 2",
        "Fermat 3",
        "Fermat 4",
    ]
    arrayEquipes = [Equipe(f"Equipe {college}") for college in colleges]
    teams = [
        Team(arrayEquipes[i], arrayEquipes[-i - 1])
        for i in range(m.ceil(len(arrayEquipes) / 2))
    ]

    return teams


def initAteliers():
    parcours1 = [Atelier("DIY 1"), Atelier("Carbone 1"), Atelier("Tri")]
    parcours2 = [Atelier("DIY 2"), Atelier("Carbone 2"), Atelier("Abeilles")]
    return parcours1, parcours2


if __name__ == "__main__":
    teams = initEquipes()
    print(teams)
