from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    FATIGUE = 20
    REQUIRED_STRENGTH = 100

    def __init__(self, name: str):
        super().__init__(name, strength=self.INITIAL_STRENGTH)

    def can_climb(self):
        return self.strength >= self.REQUIRED_STRENGTH

    def climb(self, peak: BasePeak):
        diff_multiplier = 2.0 if peak.difficulty == 'Extreme' else diff_multiplier = 1.5
        self.strength -= self.FATIGUE * diff_multiplier
        self.conquered_peaks.append(peak.name)
