import sys

args = sys.argv[1:]

if len(args) != 1:
    print("Veuillez saisir l'heure en format HH:MM")
else:
    try:
        heure, minute = map(int, args[0].split(":"))
        if not (0 <= heure <= 23 and 0 <= minute <= 59):
            raise ValueError
        suffix = "AM" if heure < 12 else "PM"
        heure = heure % 12 or 12
        print(f"{heure:02}:{minute:02} {suffix}")
    except ValueError:
        print("Des nombres au format HH:MM svp.")