#!/Users/thomas/projects/moon/.venv/bin/python
import json
from datetime import datetime
from math import radians

import ephem
from sh import corelocationcli


def locate_obs():
    # TODO: try/except in case CoreLocationCLI is not installed
    geo_json_str = str(corelocationcli("-json"))
    geo_json = json.loads(geo_json_str)
    return geo_json


def setup_observer():
    # TODO: Allow manual input of observer details
    obs = ephem.Observer()

    loc = locate_obs()
    lat = float(loc["latitude"])
    lng = float(loc["longitude"])
    elv = float(loc["altitude"])

    obs.date = datetime.utcnow()

    obs.lat = radians(lat)
    obs.long = radians(lng)
    obs.elevation = elv

    return obs


OBS = setup_observer()


def lunar_illumination(obs=OBS):
    moon = ephem.Moon()
    moon.compute(obs)
    illumination = round(moon.moon_phase * 100, 3)
    return illumination


def next_phase_point(obs=OBS):
    phase_date_map = dict(
        new=ephem.next_new_moon(obs.date).datetime().date(),
        first_quarter=ephem.next_first_quarter_moon(obs.date).datetime().date(),
        full=ephem.next_full_moon(obs.date).datetime().date(),
        last_quarter=ephem.next_last_quarter_moon(obs.date).datetime().date(),
    )
    phase_date_map = dict(sorted(phase_date_map.items(), key=lambda item: item[1]))
    next_phase = list(phase_date_map.items())[0]
    return next_phase


def intermediate_phase(phase_point):
    phases_map = {
        "first_quarter": "waxing_cresent",
        "full": "waxing_gibbous",
        "last_quarter": "waning_gibbous",
        "new": "waning_crescent",
    }
    return phases_map[phase_point]


def phase(obs=OBS):
    today = obs.date.datetime().date()
    next = next_phase_point(obs)

    if next[1] == today:
        return next[0]

    intermediate = intermediate_phase(next[0])
    return intermediate


def display(obs=OBS):
    phase_ = phase(obs)
    phase_ = phase_.replace("_", " ").title()
    lum = lunar_illumination(obs)
    output = f"The Moon today is {phase_}, with {lum}% illuminated"
    print(output)
    next = next_phase_point(obs)
    next_name = next[0].replace("_", " ").title()
    next_date = next[1].isoformat()
    output = f"{next_name} upcoming on {next_date}"
    print(output)


if __name__ == "__main__":
    display()
