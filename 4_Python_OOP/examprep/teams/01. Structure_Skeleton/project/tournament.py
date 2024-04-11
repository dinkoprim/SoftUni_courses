from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    EQUIPMENT_TYPES = {'KneePad': KneePad, 'ElbowPad': ElbowPad}
    TEAM_TYPES = {'OutdoorTeam': OutdoorTeam, 'IndoorTeam': IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise ValueError("Invalid equipment type!")
        self.equipment.append(self.EQUIPMENT_TYPES[equipment_type]())
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise ValueError("Invalid team type!")
        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        self.teams.append(self.TEAM_TYPES[team_type](team_name, country, advantage))
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        equipment_sold = self._get_equipment(equipment_type)
        team = self._get_team(team_name)

        if team.budget < equipment_sold.price:
            raise Exception("Budget is not enough!")

        team.budget -= equipment_sold.price
        team.equipment.append(equipment_sold)
        self.equipment.remove(equipment_sold)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._get_team(team_name)
        if not team:
            raise Exception("No such team!")
        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")
        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([eq.increase_price() for eq in self.equipment if type(eq).__name__ == equipment_type])
        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_team(team_name1)
        team2 = self._get_team(team_name2)
        team1_power = sum(eq.protection for eq in team1.equipment) + team1.advantage
        team2_power = sum(eq.protection for eq in team2.equipment) + team2.advantage

        if team1.__class__.__name__ != team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        if team1_power > team2_power:
            team1.win()
            return f"The winner is {team1.name}."
        elif team1_power < team2_power:
            team2.win()
            return f"The winner is {team2.name}."
        return "No winner in this game."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda team: (-team.wins))
        result = [
            f"Tournament: {self.name}",
            f"Number of Teams: {len(self.teams)}",
            f"Teams:",
        ]
        for team in sorted_teams:
            result.append(team.get_statistics())
        return '\n'.join(result)

    def _get_team(self, team_name: str):
        te = [t for t in self.teams if t.name == team_name]
        return te[0] if te else None

    def _get_equipment(self, equipment_type: str):
        eq = [e for e in self.equipment if type(e).__name__ == equipment_type]
        return eq[-1] if eq else None