from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}
    PEAK_TYPES = {'ArcticPeak': ArcticPeak, 'SummitPeak': SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES:
            return f"{climber_type} doesn't exist in our register."

        climber = self._find_climber(climber_name)

        if climber is not None:
            return f"{climber_name} has been already registered."

        self.climbers.append(self.CLIMBER_TYPES[climber_type](climber_name))
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPES:
            return f"{peak_type} is an unknown type of peak."

        self.peaks.append(self.PEAK_TYPES[peak_type](peak_name, peak_elevation))
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = self._find_climber(climber_name)
        peak = self._find_peak(peak_name)
        recommended_gear = set(peak.get_recommended_gear())
        climbers_gear = set(gear)

        if recommended_gear == climbers_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            missing_gear = sorted(list(recommended_gear - climbers_gear))
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._find_climber(climber_name)
        peak = self._find_peak(peak_name)

        if climber is None:
            return f"Climber {climber_name} is not registered yet."
        if peak is None:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        sorted_climbers = sorted([c for c in self.climbers if c.conquered_peaks],
                                 key=lambda c: (-len(c.conquered_peaks), c.name))

        result = [
            f"Total climbed peaks: {len(self.peaks)}",
            "**Climber's statistics:**"
        ]
        climbers_statistics = '\n'.join(str(c) for c in sorted_climbers)
        result.append(climbers_statistics)

        return '\n'.join(result)

    def _find_climber(self, climber_name):
        climber = [c for c in self.climbers if c.name == climber_name]
        return climber[0] if climber else None

    def _find_peak(self, peak_name):
        peak = [p for p in self.peaks if p.name == peak_name]
        return peak[0] if peak else None
