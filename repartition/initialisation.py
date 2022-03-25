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


def readExcel():
    wb = load_workbook("./effectifs.xlsx", data_only=True)
    sheet = wb[wb.sheetnames[0]]
    noms = [cell.value for cell in sheet["A"][1:]]
    eleves = [int(cell.value) for cell in sheet["B"][1:]]

    assert len(noms) == len(eleves)

    arrayColleges = [College(noms[i], eleves[i]) for i in range(len(noms))]
    arrayColleges.sort(reverse=True)
    return arrayColleges
