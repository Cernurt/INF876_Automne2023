from datetime import datetime, timedelta

date_limite = datetime(2023, 12, 31)
aujourd_hui = datetime.now()

jours_restants = (date_limite - aujourd_hui).days

print(f"Date limite : {date_limite.strftime('%Y-%m-%d')}")
print(f"Jours restants : {jours_restants} jours")
now = datetime.now()
jour_semaine = now.strftime("%A")

print(f"Jour de la semaine actuel : {jour_semaine}")

date1 = datetime(2022, 1, 1)
date2 = datetime(2023, 1, 1)

difference = date2 - date1

print(f"Différence entre {date2.strftime('%Y-%m-%d')} et {date1.strftime('%Y-%m-%d')} : {difference}")