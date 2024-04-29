def convertir_en_format_12h(heure_24h):
    heure, minute = map(int, heure_24h.split(":"))
    return "{:02d}:{:02d} {}".format((heure % 12) or 12, minute, "AM" if heure < 12 else "PM")

heure_24h = input("Entrez l'heure au format 24 heures (HH:MM) : ")
print("L'heure en format 12 heures est :", convertir_en_format_12h(heure_24h))