from openpyxl import Workbook
from datetime import datetime

from calcul import tournerAteliers
from initialisation import initAteliers, initEquipes

""" 
Répartir les équipes dans des ateliers. 
"""


def programmerAteliers():
    """Initialisation"""
    teams = initEquipes()
    parcours1, parcours2 = initAteliers()

    """Boucle de calcul"""
    tournerAteliers(teams, parcours1, parcours2)

    """ Enregistrer """
    # Excel résultat
    wb = Workbook()
    ws = wb.active
    # Par équipe
    ws.title = "Programme par équipe"
    for team in teams:
        ws.append([team.nom])
        for match in team.planning:
            ws.append([f"{match}"])
        ws.append([])
    # Par atelier
    ws = wb.create_sheet(title="Programme par atelier")
    for atelier in parcours1 + parcours2:
        ws.append([f"Atelier {atelier.nom}"])
        for match in atelier.planning:
            ws.append([f"{match.horaire}) {match.team.nom}"])
        ws.append([])

    timestamp = datetime.now().strftime("%H%M%S")
    dest_filename = f"programme_journeeDD_{timestamp}.xlsx"
    wb.save(filename=dest_filename)


if __name__ == "__main__":
    programmerAteliers()
