from typing import List

from project.divers.base_diver import BaseDiver
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    DIVER_TYPES = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    FISH_TYPES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        diver = self._find_diver(diver_name)

        if diver is not None:
            return f"{diver_name} is already a participant."

        self.divers.append(self.DIVER_TYPES[diver_type](diver_name))
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._find_fish(fish_name)

        if fish is not None:
            return f"{fish_name} is already permitted."

        self.fish_list.append(self.FISH_TYPES[fish_type](fish_name, points))
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):

        diver, fish = self._find_diver(diver_name), self._find_fish(fish_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.update_health_status()
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.update_health_status()
            return f"{diver_name} missed a good {fish_name}."

        diver.hit(fish)
        if diver.oxygen_level == 0:
            diver.update_health_status()
        return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        recovered = 0
        for d in self.divers:
            if d.has_health_issue:
                d.renew_oxy()
                d.update_health_status()
                recovered += 1
        return f"Divers recovered: {recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = self._find_diver(diver_name)
        return f"**{diver_name} Catch Report**\n{'\n'.join(fish.fish_details() for fish in diver.catch)}"

    def competition_statistics(self):
        healthy_divers = [d for d in self.divers if not d.has_health_issue]
        sorted_divers = sorted(healthy_divers,
                               key=lambda diver: (-diver.competition_points, -len(diver.catch), diver.name))
        return f"**Nautical Catch Challenge Statistics**\n{'\n'.join(str(d) for d in sorted_divers)}"

    def _find_diver(self, diver_name):
        diver = [d for d in self.divers if d.name == diver_name]
        return diver[0] if diver else None

    def _find_fish(self, fish_name):
        fish = [f for f in self.fish_list if f.name == fish_name]
        return fish[0] if fish else None




