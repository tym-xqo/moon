#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from datetime import datetime

import moon
from ephem import Observer


def obs():
    obs = Observer()
    obs.date = datetime.utcnow()
    obs.lat = 0.7342900185238562
    obs.long = -1.5309223776242014
    obs.elevation = 186.2

    return obs


def moon_phase(request):
    obs_ = obs()
    phase_ = moon.phase(obs_)
    phase_ = phase_.replace("_", " ").title()
    lum = moon.lunar_illumination(obs_)
    next = moon.next_phase_point(obs_)
    next_name = next[0].replace("_", " ").title()
    next_date = next[1].isoformat()
    payload = dict(
        phase=phase_,
        illumination=lum,
        next_phase=next_name,
        next_phase_on_date=next_date,
    )
    return json.dumps(payload)
