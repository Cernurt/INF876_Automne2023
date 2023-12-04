from datetime import datetime

now = datetime.now()
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Date et heure actuelles : {formatted_now}")

date_naissance = datetime(1990, 5, 15)
aujourd_hui = datetime.now()

age = (aujourd_hui - date_naissance).days // 365

print(f"Date de naissance : {date_naissance.strftime('%Y-%m-%d')}")
print(f"Âge actuel : {age} ans")