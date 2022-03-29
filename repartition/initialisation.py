from openpyxl import load_workbook
import math
from modelisation import College, Equipe


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

    (colonneNoms, colonneNombres) = ("E", "H") if option == "lycée" else ("A", "D")

    noms = [
        cell.value.strip()
        for cell in sheet[colonneNoms][1:]
        if (cell.value != None and cell.value != "TOTAL")
    ]
    nbNoms = len(noms)
    eleves = [cleanNombre(cell.value) for cell in sheet[colonneNombres][1 : nbNoms + 1]]

    assert len(noms) == len(eleves)

    arrayColleges = [
        College(noms[i], eleves[i]) for i in range(len(noms)) if eleves[i] > 0
    ]
    arrayColleges.sort(reverse=True)
    return arrayColleges
