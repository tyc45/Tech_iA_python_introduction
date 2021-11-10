ma_liste = [3, -4, 8, 7, 20, 32, -9, 21]
abs_liste_impair = [i+1 for i in ma_liste if i % 2 == 0 and i > 0]
print(abs_liste_impair)


lst1=[2, 4, 6, 8, 10, 12, 14]
big_square_list = [i**2 for i in lst1 if i**2 > 50]
print(big_square_list)


lst2 = [i for i in range(1200, 2000, 130)]
print(lst2)


vehicules_weight = {"truck": 10000,
                    "plane": 50000,
                    "skateboard": 5,
                    "bike": 20,
                    "car": 1200,
                    "shoes": 0.5
}
slim_vehicles = [name for name, weight in vehicules_weight.items() if weight < 5000]
print(slim_vehicles)