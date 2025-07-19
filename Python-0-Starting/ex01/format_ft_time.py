import time
from datetime import datetime

# timestamp Unix actuel (secondes depuis le 1er janvier 1970)
current_timestamp = time.time()

# date actuelle
current_date = datetime.now()

# garder 4 décimales et formatage des virgules
formatted_timestamp = f"{current_timestamp:,.4f}"

# formatage en 2 décimales
scientific_notation = f"{current_timestamp:.2e}"

# formatage format "Mois Jour ann&ée"
formatted_date = current_date.strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {formatted_timestamp} or {scientific_notation} in scientific notation")
print(formatted_date)