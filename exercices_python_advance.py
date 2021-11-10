# Structure générale d'une compréhension: Exo 1

ma_liste = [3, -4, 8, 7, 20, 32, -9, 21]
abs_liste_impair = [i + 1 for i in ma_liste if i % 2 == 0 and i > 0]
print(abs_liste_impair)


# Structure générale d'une compréhension: Exo 2
lst1=[2, 4, 6, 8, 10, 12, 14]
big_square_list = [i ** 2 for i in lst1 if i ** 2 > 50]
print(big_square_list)


# Structure générale d'une compréhension: Exo 3
lst2 = [i for i in range(1200, 2000, 130)]
print(lst2)


# Structure générale d'une compréhension: Exo 4
vehicules_weight = {"truck": 10000,
                    "plane": 50000,
                    "skateboard": 5,
                    "bike": 20,
                    "car": 1200,
                    "shoes": 0.5
}
slim_vehicles = [name.upper() for name in vehicules_weight if vehicules_weight[name] < 5000]
print(slim_vehicles)


# Compréhension de dictionnaire: Exo 1
lst=["NY", "FL", "CA", "VT"]
dict = {elmt:elmt for elmt in lst}
print(dict)


# Compréhension de dictionnaire: Exo 2
div_hundred = {i:i/100 for i in range(100, 160, 10)}
print(div_hundred)


# Compréhension de dictionnaire: Exo 3
dict1={"NFLX":4950,"TREX":2400,"FIZZ":1800, "XPO":1700}
dict1_redux = {key:dict1[key] for key in dict1 if dict1[key] > 2000}
print(dict1_redux)


# Compréhension de dictionnaire: Exo 4
lst1=["Netflix", "Hulu", "Sling", "Hbo"]
lst2=[198, 166, 237, 125]
dict2 = {item[0]:item[1] for item in zip(lst1,lst2)}
print(dict2)