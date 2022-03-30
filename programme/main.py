from openpyxl import Workbook
from datetime import datetime

from .modelisation import Equipe, Atelier
from .calcul import calculUnAtelier

""" 
Répartir les équipes dans des ateliers. 
"""


def programmerAteliers(nbEquipes, nbAteliersAFaire):
    """Initialisation"""
    arrayEquipes = [Equipe(f"Equipe {i}") for i in range(1, nbEquipes + 1)]
    arrayAteliers = [
        Atelier("Cécifoot", "Sport"),
        Atelier("Biathlon Sarbacane", "Sport"),
        Atelier("Incollables", "Sensibilisation"),
        Atelier("Rugby fauteuil", "Sport"),
        Atelier("Para-judo", "Sport"),
        Atelier("LSF", "Sensibilisation"),
        Atelier("Athlétisme", "Sport"),
        Atelier("Jean Lagarde", "Sensibilisation"),
    ]

    """Boucle de calcul"""
    # On tourne, tout simplement
    newArrayEquipes = arrayEquipes
    for i in range(nbAteliersAFaire):
        newArrayEquipes = calculUnAtelier(i, newArrayEquipes, arrayAteliers)

    """ Enregistrer """
    # Excel résultat
    wb = Workbook()
    ws = wb.active
    ws.title = "Programme par équipe"
    for equipe in arrayEquipes:
        ws.append([equipe.nom])
        for match in equipe.planning:
            ws.append([f"{match}"])
        ws.append([])

    timestamp = datetime.now().strftime("%H%M%S")
    dest_filename = f"programme_{timestamp}.xlsx"
    wb.save(filename=dest_filename)


if __name__ == "__main__":
    programmerAteliers(16, 4)
