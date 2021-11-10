the_killer = {'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}
dead = ['Lucas', 'Bill'] 

def killer(suspect_info, dead):
    liste = []
    for cle,valeur in suspect_info.items():
        if dead in valeur:
            liste.append(cle)
    return "".join(liste)  


print("the killer is", killer(the_killer,dead))