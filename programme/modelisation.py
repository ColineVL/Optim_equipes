class Equipe:
    """
    Une équipe, constituée d'élèves de différents établissements scolaires

    Attributes
    ----------
    nom: string
        Nom de l'équipe
    planning: array
        Liste des matchs faits par cette équipe, dans l'ordre
    """

    def __init__(self, nom):
        self.nom = nom
        self.planning = []

    def __str__(self):
        return f"{self.nom}"

    def addPlanning(self, match):
        self.planning.append(match)


class Atelier:
    """
    Un atelier proposé

    Attributes
    ----------
    nom: string
        Nom de l'atelier
    nbEquipes : int
       Nombre d'équipes sur l'atelier
    theme: string
        Type d'atelier : "Sport" ou "Sensibilisation"
    """

    def __init__(self, nom, theme, nbEquipes=2):
        self.nom = nom
        self.nbEquipes = nbEquipes
        self.theme = theme

    def __str__(self):
        return f"Atelier {self.nom}"


class Match:
    """
    Une rencontre entre deux équipes, sur un atelier particulier

    Attributes
    ----------
    atelier: Atelier
        Atelier sur lequel se déroule le match
    equipes : tuple
       Deux équipes qui s'affrontent
    horaire : int
        On a 4 matchs sur le matin
    """

    def __init__(self, atelier, equipes, horaire):
        self.atelier = atelier
        self.equipes = equipes
        self.horaire = horaire

    def __str__(self):
        return f"{self.horaire}-{self.atelier.nom} : {self.equipes[0]} VS {self.equipes[1]}"
