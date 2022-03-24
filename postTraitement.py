def simplePrint(arrayEquipes, arrayColleges):
    for equipe in arrayEquipes:
        print(equipe.effectifs)

    # On calcule la répartition du point de vue des collèges
    for college in arrayColleges:
        for equipe in arrayEquipes:
            college.repartition[equipe.nom] = equipe.effectifs[college.nom]
        print(f"{college.nom} : {college.repartition}")
