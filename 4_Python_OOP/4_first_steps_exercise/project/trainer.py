class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = {}

    def add_pokemon(self, pokemon):
        if pokemon.name not in self.pokemons:
            self.pokemons[pokemon.name] = pokemon.health
            return f'Caught {pokemon.pokemon_details()}'
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name):
        for pokemon in self.pokemons:
            if pokemon == pokemon_name:
                del self.pokemons[pokemon]
                return f"You have released {pokemon}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n'
        for poke, health in self.pokemons.items():
            result += f'- {poke} with health {health}'
        return result


