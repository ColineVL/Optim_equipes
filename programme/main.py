from openpyxl import Workbook
from datetime import datetime

from .modelisation import Equipe, Atelier
from .calcul import tournerAteliers

""" 
Répartir les équipes dans des ateliers. 
"""


def programmerAteliers(nbEquipes, nbAteliersAFaire, option):
    """Initialisation"""
    arrayEquipes = [Equipe(f"Equipe {i}") for i in range(1, nbEquipes + 1)]
    arrayAteliersCollege = [
        Atelier("Cécifoot 1", "Sport"),
        Atelier("Biathlon Sarbacane", "Sport"),
        Atelier("Incollables", "Sensibilisation"),
        Atelier("Rugby fauteuil", "Sport"),
        Atelier("Cécifoot 2", "Sport"),
        Atelier("LSF", "Sensibilisation"),
        Atelier("Para-judo", "Sport"),
        Atelier("Jean Lagarde", "Sensibilisation"),
    ]

    arrayAteliersLycee = [
        Atelier("Basket fauteuil", "Sport"),
        Atelier("Cécifoot", "Sport"),
        Atelier("LSF", "Sensibilisation"),
        Atelier("Rugby fauteuil", "Sport"),
        Atelier("Boccia", "Sport"),
        Atelier("Biathlon", "Sport"),
    ]

    arrayAteliers = arrayAteliersCollege if option == "collège" else arrayAteliersLycee

    """Boucle de calcul"""
    tournerAteliers(nbAteliersAFaire, arrayEquipes, arrayAteliers)

    """ Enregistrer """
    # Excel résultat
    wb = Workbook()
    ws = wb.active
    # Par équipe
    ws.title = "Programme par équipe"
    for equipe in arrayEquipes:
        ws.append([equipe.nom])
        for match in equipe.planning:
            ws.append([f"{match} {match.equipes[0]} VS {match.equipes[1]}"])
        ws.append([])
    # Par atelier
    ws = wb.create_sheet(title="Programme par atelier")
    for atelier in arrayAteliers:
        ws.append([f"Atelier {atelier.nom}"])
        for match in atelier.planning:
            ws.append([f"{match.horaire}) {match.equipes[0]} VS {match.equipes[1]}"])
        ws.append([])

    timestamp = datetime.now().strftime("%H%M%S")
    dest_filename = f"programme_{option}_{timestamp}.xlsx"
    wb.save(filename=dest_filename)


if __name__ == "__main__":
    programmerAteliers(16, 4)
