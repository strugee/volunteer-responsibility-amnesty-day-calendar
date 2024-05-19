#!/usr/bin/env python3

import ephem
from ical.calendar import Calendar
from ical.calendar_stream import IcsCalendarStream
from ical.event import Event
from datetime import datetime, date


def get_summer_solstice(year):
    observer = ephem.Observer()
    observer.lat = "0"  # Latitude of the observer (Equator)
    observer.lon = "0"  # Longitude of the observer (Prime Meridian)

    solstice_date = ephem.next_summer_solstice(datetime(year, 1, 1))
    return solstice_date.datetime().date()


calendar = Calendar()
current_year = datetime.now().year
for year in range(current_year, current_year + 20):
    solstice_datetime = get_summer_solstice(year)
    print(f"Summer Solstice in {year}: {solstice_datetime}")

    month = solstice_datetime.month
    day = solstice_datetime.day
    print(year, month, day)
    calendar.events.append(
        Event(
            summary="Volunteer Responsibility Amnesty Day",
            start=date(year, month, day),
            end=date(year, month, day + 1),
        ),
    )

print(IcsCalendarStream.calendar_to_ics(calendar))
