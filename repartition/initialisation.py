from openpyxl import load_workbook
import math
from .modelisation import College, Equipe


def init(arrayColleges, nbEquipes):
    arrayEquipes = [
        Equipe(f"Equipe {i}", arrayColleges) for i in range(1, nbEquipes + 1)
    ]

    nbElevesTotal = sum([col.nbEleves for col in arrayColleges])
    maxParEquipe = math.ceil(nbElevesTotal / nbEquipes)

    return arrayEquipes, maxParEquipe


def cleanNombre(value):
    if value == None:
        value = 0
    return int(value)


def readExcel(option="collège"):
    nomFichier = "Journée 31 mars - Sensibilisation au handicap.xlsx"
    wb = load_workbook(nomFichier, data_only=True)
    sheet = wb["Présents"]

    (colonneNoms, colonneNombres) = ("F", "J") if option == "lycée" else ("A", "E")

    noms = [
        cell.value.strip()
        for cell in sheet[colonneNoms][3:]
        if (cell.value != None and cell.value != "TOTAL")
    ]
    nbNoms = len(noms)
    eleves = [cleanNombre(cell.value) for cell in sheet[colonneNombres][3 : nbNoms + 3]]

    assert len(noms) == len(eleves)

    arrayColleges = [
        College(noms[i], eleves[i]) for i in range(len(noms)) if eleves[i] > 0
    ]
    arrayColleges.sort()
    return arrayColleges
