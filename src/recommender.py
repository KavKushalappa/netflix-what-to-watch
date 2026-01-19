import json
from dataclasses import dataclass
from typing import List, Dict, Any, Tuple

@dataclass
class Preferences:
    mood: str
    genre: str
    time_available: int
    pacing: int
    intensity: int
    binge: int

def load_shows(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def score_show(show: Dict[str, Any], pref: Preferences) -> Tuple[float, Dict[str, float]]:
    w_mood = 3.0
    w_genre = 2.5
    w_time = 2.0
    w_pacing = 1.5
    w_intensity = 1.5
    w_binge = 1.0

    mood_match = 1.0 if pref.mood in show.get("mood", []) else 0.0
    genre_match = 1.0 if pref.genre in show.get("genres", []) else 0.0

    ep = int(show.get("episode_minutes", 45))
    if ep <= pref.time_available:
        time_fit = 1.0
    else:
        time_fit = max(0.0, 1.0 - (ep - pref.time_available) / max(ep, 1))

    pacing_fit = 1.0 - min(abs(int(show.get("pacing", 2)) - pref.pacing), 3) / 3.0
    intensity_fit = 1.0 - min(abs(int(show.get("intensity", 2)) - pref.intensity), 3) / 3.0
    binge_fit = 1.0 - min(abs(int(show.get("bingeability", 3)) - pref.binge), 4) / 4.0

    components = {
        "mood": w_mood * mood_match,
        "genre": w_genre * genre_match,
        "time": w_time * time_fit,
        "pacing": w_pacing * pacing_fit,
        "intensity": w_intensity * intensity_fit,
        "binge": w_binge * binge_fit
    }

    total = sum(components.values())
    return total, components


def recommend(shows: List[Dict[str, Any]], pref: Preferences, top_n: int = 3):
    scored = []
    for s in shows:
        total, components = score_show(s, pref)
        scored.append({
            **s,
            "score": round(total, 3),
            "explain": {k: round(v, 3) for k, v in components.items()}
        })

    scored.sort(key=lambda x: x["score"], reverse=True)
    return scored[:top_n]
