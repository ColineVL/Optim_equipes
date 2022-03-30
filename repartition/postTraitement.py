from openpyxl import Workbook
from datetime import datetime


def writeResultsInExcel(arrayEquipes, arrayColleges, option):
    wb = Workbook()

    """ Première page : par équipe """
    ws = wb.active
    ws.title = "Répartition par équipe"

    for equipe in arrayEquipes:
        ws.append([equipe.nom])
        for key, value in equipe.effectifs.items():
            if value > 0:
                ws.append([key, value])
        ws.append([])

    """ Deuxième page : par équipe """
    ws = wb.create_sheet(title=f"Répartition par {option}")

    for college in arrayColleges:
        # D'abord calcul python
        for equipe in arrayEquipes:
            college.repartition[equipe.nom] = equipe.effectifs[college.nom]
        # Puis on enregistre
        ws.append([college.nom])
        for key, value in college.repartition.items():
            if value > 0:
                ws.append([key, value])
        # Une petite ligne vide pour que ce soit plus propre
        ws.append([])

    """ Enregistrer """
    timestamp = datetime.now().strftime("%H%M%S")
    dest_filename = f"repartition_{option}_{timestamp}.xlsx"
    wb.save(filename=dest_filename)
