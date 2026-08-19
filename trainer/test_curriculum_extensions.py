from django.test import SimpleTestCase

from .curriculum import CARDS, FOUNDATION_SEQUENCE


class PracticalFoundationTests(SimpleTestCase):
    def test_level_one_contains_practical_junior_building_blocks(self):
        expected = {
            "dj12",  # INSTALLED_APPS
            "f01",   # leer un Model completo
            "m15",   # ManyToMany básico
            "f02",   # CRUD ORM
            "s03",   # ModelSerializer explícito
            "d02",   # IsAuthenticated
            "d03",   # perform_create
            "f03",   # API mínima integrada
        }
        level_one = {card["id"] for card in CARDS if card["level"] == 1}
        self.assertTrue(expected.issubset(level_one))

    def test_practical_foundations_are_code_first_and_explained(self):
        practical = {
            card["id"]: card
            for card in CARDS
            if card["id"] in {"dj12", "f01", "m15", "f02", "s03", "d02", "d03", "f03"}
        }
        self.assertEqual(len(practical), 8)
        self.assertTrue(all(card["code"] for card in practical.values()))
        self.assertTrue(all(len(card["explanation"]) >= 120 for card in practical.values()))

    def test_integrated_api_exercise_comes_after_required_pieces(self):
        position = {card_id: index for index, card_id in enumerate(FOUNDATION_SEQUENCE)}
        for prerequisite in ("f01", "f02", "s03", "d01", "d02", "d03", "d04"):
            self.assertLess(position[prerequisite], position["f03"])
