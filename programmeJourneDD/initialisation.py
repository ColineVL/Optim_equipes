import math as m
from modelisation import Equipe, Team


def init():
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


if __name__ == "__main__":
    teams = init()
    print(teams)
