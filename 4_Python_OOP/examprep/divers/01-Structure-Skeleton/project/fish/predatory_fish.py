from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TIME_TO_CATCH = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, time_to_catch=self.TIME_TO_CATCH)

    def fish_details(self):
        return (f"{type(self).__name__}: {self.name} "
                f"[Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]")