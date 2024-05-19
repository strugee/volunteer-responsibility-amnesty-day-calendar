#!/usr/bin/env python3

import ephem
from datetime import datetime

def get_summer_solstice(year):
    observer = ephem.Observer()
    observer.lat = '0'  # Latitude of the observer (Equator)
    observer.lon = '0'  # Longitude of the observer (Prime Meridian)

    solstice_date = ephem.next_summer_solstice(datetime(year, 1, 1))
    return solstice_date.datetime().date()

current_year = datetime.now().year
for i in range(current_year, current_year + 20):
    print(f"Summer Solstice in {i}: {get_summer_solstice(i)}")

