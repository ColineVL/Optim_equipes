from .modelisation import Match


def calculUnAtelier(horaire, teams, arrayAteliers):

    nbTeams = len(teams)
    assert nbTeams % 2 == 0
    for i in range(int(nbTeams / 2)):
        equipe1 = teams[i]
        equipe2 = teams[nbTeams - i - 1]
        # Créer un nouveau match et l'ajouter au planning de chaque équipe
        match = Match(arrayAteliers[0], (equipe1, equipe2), horaire)
        equipe1.addPlanning(match)
        equipe2.addPlanning(match)

    newArray = [teams[0]]
    newArray.append(teams[-1])
    for i in range(1, nbTeams - 1):
        newArray.append(teams[i])
    print("-----------")
    return newArray
