from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    FATIGUE = 30
    REQUIRED_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.REQUIRED_STRENGTH

    def climb(self, peak: BasePeak):
        diff_multiplier = 1.3 if peak.difficulty == 'Advanced' else diff_multiplier = 2.5
        self.strength -= self.FATIGUE * diff_multiplier
        self.conquered_peaks.append(peak.name)