# source env/bin/activate
# activation du venv dans le terminal pour chaque exo

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# les listes sont mutables
ft_list[1] = "World!"

# (les tuples sont immutables, creation d'un nouveau a chaque fois)
ft_tuple = ("Hello", "France!")
# Impossible de modifier un tuple existant, on doit en créer un nouveau

# Réassignation complète car aucun ordre établi
ft_set.clear
ft_set.remove("tutu!")
ft_set.add("Perpignan!")

# Les dictionnaires sont mutables, on peut modifier les valeurs
ft_dict["Hello"] = "42Perpignan!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)