from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN = 540
    OXY_DECREASE_INDEX = 0.3

    def __init__(self, name: str):
        super().__init__(name, oxygen_level=self.INITIAL_OXYGEN)

    def miss(self, time_to_catch: int):
        used_oxygen = round(self.OXY_DECREASE_INDEX * time_to_catch)
        if self.oxygen_level < used_oxygen:
            self.oxygen_level = 0
        else:
            self.oxygen_level -= used_oxygen

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN
