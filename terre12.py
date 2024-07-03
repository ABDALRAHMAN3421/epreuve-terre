import sys

def convert_to_24h(time_12h):
    parts = time_12h.strip().split()
    if len(parts) != 2:
        raise ValueError("Format incorrect. Utilisez HH:MM AM/PM.")
    
    time, period = parts
    hour, minute = map(int, time.split(':'))
    
    if period.upper() not in ["AM", "PM"]:
        raise ValueError("Période incorrecte. Utilisez AM ou PM.")
    
    if not (1 <= hour <= 12) or not (0 <= minute <= 59):
        raise ValueError("Heure ou minute incorrecte.")
    
    if period.upper() == "PM" and hour != 12:
        hour += 12
    elif period.upper() == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minute:02}"

if len(sys.argv) != 2:
    print("Veuillez saisir l'heure en format 12h (HH:MM AM/PM).")
else:
    try:
        time_12h = sys.argv[1]
        time_24h = convert_to_24h(time_12h)
        print(time_24h)
    except ValueError as e:
        print(e)