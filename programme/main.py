from openpyxl import Workbook
from datetime import datetime

""" 
Répartir les équipes dans des ateliers. 
"""


def programmerAteliers():
    """Initialisation"""
    arrayAteliers = [
        "Cécifoot",  # Sport
        "Biathlon Sarbacane",  # Sport
        "Incollables",  # Sensibilisation
        "Rugby fauteuil",  # Sport
        "Para-judo",  # Sport
        "LSF",  # Sensibilisation
        "Athlétisme",  # Sport
        "Jean Lagarde",  # Sensibilisation
    ]
    # On suppose qu'il y a autant d'équipes que d'ateliers
    nbEquipes = len(arrayAteliers)
    nbAteliersAFaire = 4

    # Excel résultat
    wb = Workbook()
    ws = wb.active
    ws.title = "Programme par équipe"

    """Boucle de calcul"""
    # On tourne, tout simplement
    for noEquipe in range(1, nbEquipes + 1):
        nameEquipe = f"Equipe {noEquipe}"
        mesAteliers = [
            arrayAteliers[(noEquipe + noAtelier) % nbEquipes]
            for noAtelier in range(nbAteliersAFaire)
        ]
        # J'enregistre dans le excel
        ws.append([nameEquipe])
        for key in mesAteliers:
            ws.append([key])
        ws.append([])

    """ Enregistrer """
    timestamp = datetime.now().strftime("%H%M%S")
    dest_filename = f"programme_{timestamp}.xlsx"
    wb.save(filename=dest_filename)


if __name__ == "__main__":
    programmerAteliers()
