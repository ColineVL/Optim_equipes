class Equipe:
    """
    Une équipe, constituée d'élèves de différents établissements scolaires

    Attributes
    ----------
    nom: string
        Nom de l'équipe
    effectifs: dict
        Un dictionnaire contenant pour chaque établissement, le nombre de ses élèves dans cette équipe
    """

    def __init__(self, nom):
        self.nom = nom
        self.nbEleves = 0
        self.effectifs = {}

    def __repr__(self):
        return f"Equipe {self.nom} : {self.nbEleves} élèves"

    def __str__(self):
        return f"Equipe {self.nom} : {self.nbEleves} élèves"

    def getNbEleves(self):
        return sum([value for value in self.effectifs.values()])

    def setEleves(self, college, nombre):
        if college.nom not in self.effectifs:
            self.effectifs[college.nom] = 0

        self.effectifs[college.nom] += nombre


class College:
    """
    Un collège (ou un lycée)

    Attributes
    ----------
    nom: string
        Nom de l'établissement scolaire
    nbEleves : int
       Nombre d'élèves présents à l'événement
    repartition: dict
        Répartition des élèves selon les équipes
    """

    def __init__(self, nom, nbEleves):
        self.nom = nom
        self.nbEleves = nbEleves
        self.repartition = {}

    def __repr__(self):
        return f"{self.nom} : {self.nbEleves} élèves"

    def __str__(self):
        return f"{self.nom} : {self.nbEleves} élèves"

    def __lt__(self, other):
        return self.nbEleves < other.nbEleves
