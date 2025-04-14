# 1. Créer une liste de tuples contenant les coordonnées des villes
villes = [
    ("Paris", (48.8566, 2.3522)),
    ("New York", (40.7128, -74.0060)),
    ("Tokyo", (35.6895, 139.6917)),
    ("Sydney", (-33.8688, 151.2093)),
    ("Cairo", (30.0444, 31.2357))
]

# 2. Afficher chaque ville avec ses coordonnées
print("Coordonnées des villes :")
for ville in villes:
    nom, (lat, lon) = ville
    print(f"{nom} : latitude = {lat}, longitude = {lon}")

# 3. Afficher uniquement les latitudes
print("\nLatitudes des villes :")
for ville in villes:
    print(ville[1][0])

# 4. Calculer et afficher la latitude moyenne
latitudes = [ville[1][0] for ville in villes]
moyenne = sum(latitudes) / len(latitudes)
print(f"\nLatitude moyenne : {moyenne:.4f}")