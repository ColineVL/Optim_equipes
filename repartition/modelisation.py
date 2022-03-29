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

    def __init__(self, nom, arrayColleges):
        self.nom = nom
        self.effectifs = {}
        for col in arrayColleges:
            self.effectifs[col.nom] = 0

    def __repr__(self):
        return f"Equipe {self.nom} : {self.getNbEleves()} élèves"

    def __str__(self):
        return f"Equipe {self.nom} : {self.getNbEleves()} élèves"

    def getNbEleves(self):
        return sum([value for value in self.effectifs.values()])

    def setEleves(self, college, nombre):
        self.effectifs[college.nom] += nombre

        college.elevesRestants -= nombre

    def getPlacesRestantes(self, maxParEquipe):
        return maxParEquipe - self.getNbEleves()


class College:
    """
    Un collège (ou un lycée)

    Attributes
    ----------
    nom: string
        Nom de l'établissement scolaire
    nbEleves : int
       Nombre d'élèves présents à l'événement
    elevesRestants: int
        Nombre d'élèves pas encore affectés à une équipe
    repartition: dict
        Répartition des élèves selon les équipes
    """

    def __init__(self, nom, nbEleves):
        self.nom = nom
        self.nbEleves = nbEleves
        self.repartition = {}
        self.elevesRestants = nbEleves

    def __repr__(self):
        return f"{self.nom} : {self.nbEleves} élèves"

    def __str__(self):
        return f"{self.nom} : {self.nbEleves} élèves"

    def __lt__(self, other):
        return self.nbEleves < other.nbEleves
