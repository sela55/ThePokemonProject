import pytest
import requests


class TestPokemonApi:
    response = None
    content = None
    fire_pokemons = {}
    memory = {}

    @classmethod
    def setup_class(cls):
        # First initial method before the tests to connect to api and store the information, also reducing the number
        # of connections
        cls.response = requests.get("https://pokeapi.co/api/v2/type")
        content = cls.response.json()
        for result in content["results"]:
            if result["name"] == "fire":
                link = result["url"]
                type_response = requests.get(link)
                type_content = type_response.json()
                for pokemon in type_content["pokemon"]:
                    cls.fire_pokemons[pokemon["pokemon"]["name"]] = pokemon["pokemon"]["url"]
                break

    def test_q1(self):
        pokemon_set_structure = set()
        content = self.response.json()
        for result in content["results"]:
            pokemon_set_structure.add(result["name"])
        assert len(pokemon_set_structure) == 20

    # In both two tests below (q2 and q3) I used DDT in order to assert
    @pytest.mark.parametrize("name, expected", [("charmander", True), ("bulbasaur", False)])
    def test_q2(self, name, expected):
        assert (name in self.fire_pokemons.keys()) == expected

    @pytest.mark.parametrize("name_fire_pokemon", [("charizard-gmax", 10000), ("cinderace-gmax", 10000), ("coalossal-gmax", 10000), ("centiskorch-gmax", 10000), ("groudon-primal", 9997)])
    def test_q3(self, name_fire_pokemon):
        if "tuple_fire_pokemons_and_weight" not in self.memory.keys():
            weight_dict_for_fire_pokemons = dict()
            for name, url in self.fire_pokemons.items():
                response = requests.get(url)
                content = response.json()
                weight_dict_for_fire_pokemons[name] = content["weight"]
            tuple_fire_pokemons_and_weight = tuple(weight_dict_for_fire_pokemons.items())
            tuple_fire_pokemons_and_weight = sorted(tuple_fire_pokemons_and_weight, key=lambda x: x[1])
            tuple_fire_pokemons_and_weight = tuple_fire_pokemons_and_weight[-5:]
            self.memory["tuple_fire_pokemons_and_weight"] = tuple_fire_pokemons_and_weight
        assert name_fire_pokemon in self.memory["tuple_fire_pokemons_and_weight"]









