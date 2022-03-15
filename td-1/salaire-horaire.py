DUREE_LEGALE = 35
TAUX_MAJ_HEUR_SUP = 150 
 
def salaire_hebdomadaire(nb_heures, salaire_horaire):
    if (nb_heures < DUREE_LEGALE):
        return nb_heures*salaire_horaire
    else:
        return  (DUREE_LEGALE + (nb_heures - DUREE_LEGALE) * (TAUX_MAJ_HEUR_SUP / 100.0))*salaire_horaire

print(salaire_hebdomadaire(35, 550))
