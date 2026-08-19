from django.test import SimpleTestCase
from django.urls import reverse

from .cards import CARDS, MODULES


class CardCatalogTests(SimpleTestCase):
    def test_catalog_has_interview_depth_and_code_first_focus(self):
        self.assertGreaterEqual(len(CARDS), 140)
        self.assertGreaterEqual(
            sum(bool(card["code"]) for card in CARDS) / len(CARDS),
            0.75,
        )
        self.assertGreaterEqual(
            sum(card["module"] == "entrevista" for card in CARDS),
            20,
        )

    def test_ids_are_unique_and_modules_are_valid(self):
        ids = [card["id"] for card in CARDS]
        module_ids = {module["id"] for module in MODULES}

        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(card["module"] in module_ids for card in CARDS))

    def test_every_card_has_required_content_and_official_source(self):
        required = {
            "id",
            "module",
            "question",
            "answer",
            "code",
            "answer_code",
            "kind",
                "difficulty",
                "source",
                "verdict",
        }
        for card in CARDS:
            with self.subTest(card=card["id"]):
                self.assertTrue(required.issubset(card))
                self.assertTrue(card["question"].strip())
                self.assertTrue(card["answer"].strip())
                self.assertTrue(card["source"].startswith("https://"))

    def test_requested_core_modules_exist(self):
        module_ids = {module["id"] for module in MODULES}
        self.assertTrue(
            {
                "django",
                "modelos",
                "orm_db",
                "serializers",
                "drf",
                "http_api",
                "auth_security",
                "testing",
                "git_deploy",
                "python",
                "entrevista",
            }.issubset(module_ids)
        )

    def test_verdict_exercises_are_balanced(self):
        verdict_cards = [card for card in CARDS if card["verdict"] is not None]

        self.assertGreaterEqual(len(verdict_cards), 20)
        self.assertEqual(
            sum(card["verdict"] is True for card in verdict_cards),
            sum(card["verdict"] is False for card in verdict_cards),
        )
        self.assertTrue(all(card["kind"] == "veredicto" for card in verdict_cards))


class TrainerViewsTests(SimpleTestCase):
    def test_pages_render(self):
        for name in ("trainer:home", "trainer:study", "trainer:about"):
            with self.subTest(name=name):
                self.assertEqual(self.client.get(reverse(name)).status_code, 200)

    def test_study_page_exposes_verdict_interaction(self):
        response = self.client.get(reverse("trainer:study"))

        self.assertContains(response, "¿Está bien o mal?")
        self.assertContains(response, 'data-verdict-choice="true"')
        self.assertContains(response, 'data-verdict-choice="false"')

    def test_cards_api_can_filter_by_module(self):
        response = self.client.get(reverse("trainer:cards_api"), {"module": "drf"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        expected = sum(card["module"] == "drf" for card in CARDS)
        self.assertEqual(payload["count"], expected)
        self.assertTrue(all(card["module"] == "drf" for card in payload["cards"]))

    def test_meta_api_exposes_deck_stats(self):
        payload = self.client.get(reverse("trainer:meta_api")).json()

        self.assertEqual(payload["cards"], len(CARDS))
        self.assertEqual(len(payload["modules"]), len(MODULES))
        self.assertEqual(payload["module_count"], len(MODULES))
        self.assertEqual(payload["with_code"], len(CARDS))
        self.assertEqual(payload["verdicts"], 20)
