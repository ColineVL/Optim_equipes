class Equipe:
    """
    Une équipe, constituée d'élèves de différents établissements scolaires

    Attributes
    ----------
    nom: string
        Nom de l'équipe
    """

    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return f"{self.nom}"


class Atelier:
    """
    Un atelier proposé

    Attributes
    ----------
    nom: string
        Nom de l'atelier
    planning : array
        Liste des matchs faits dans cet atelier, dans l'ordre
    """

    def __init__(self, nom):
        self.nom = nom
        self.planning = []

    def __str__(self):
        return f"Atelier {self.nom}"

    def __repr__(self):
        return f"Atelier {self.nom}"

    def addPlanning(self, match):
        self.planning.append(match)


class Team:
    """
    Deux équipes qui passent l'aprem ensemble

    Attributes
    ----------
    equipe1 : Equipe
       Première équipe
    equipe2 : Equipe
        Deuxième équipe
    planning: array
        Liste des matchs faits par cette team, dans l'ordre
    nom : string
        Nom de la team
    """

    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2
        if self.equipe1 == self.equipe2:
            self.nom = self.equipe1.nom
        else:
            self.nom = f"{self.equipe1.nom} et {self.equipe2.nom}"
        self.planning = []

    def __str__(self):
        return self.nom

    def __repr__(self):
        return self.nom

    def addPlanning(self, match):
        self.planning.append(match)


class Match:
    """
    Une rencontre entre deux équipes, sur un atelier particulier, à un horaire précis

    Attributes
    ----------
    atelier: Atelier
        Atelier sur lequel se déroule le match
    team : Team
       Deux équipes
    horaire : int
        Première, deuxième rotation ?
    """

    def __init__(self, atelier, horaire):
        self.atelier = atelier
        self.horaire = horaire

    def __str__(self):
        return f"{self.horaire}) {self.atelier.nom}"
