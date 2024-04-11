from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):

    @staticmethod
    def get_recommended_gear():
        return ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def calculate_difficulty_level(self):
        return 'Extreme' if self.elevation > 2500 else 'Advanced' if 1500 <= self.elevation <= 2500 else None
