from django.test import SimpleTestCase
from django.urls import reverse

from .cards import (
    CARDS,
    CURRICULUM_LEVELS,
    FOUNDATION_SEQUENCE,
    LEVEL_ZERO_SEQUENCE,
    MODULES,
)


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
            "context",
            "explanation",
            "kind",
                "difficulty",
                "source",
            "verdict",
            "level",
            "sequence",
            "prerequisites",
        }
        for card in CARDS:
            with self.subTest(card=card["id"]):
                self.assertTrue(required.issubset(card))
                self.assertTrue(card["question"].strip())
                self.assertTrue(card["answer"].strip())
                self.assertTrue(card["source"].startswith("https://"))

    def test_curriculum_assigns_every_card_to_one_level(self):
        level_ids = {level["id"] for level in CURRICULUM_LEVELS}

        self.assertEqual(level_ids, {0, 1, 2, 3, 4})
        self.assertTrue(all(card["level"] in level_ids for card in CARDS))
        self.assertEqual(
            sum(level["card_count"] for level in CURRICULUM_LEVELS),
            len(CARDS),
        )

    def test_foundations_are_ordered_and_explained_from_first_principles(self):
        foundations = sorted(
            (card for card in CARDS if card["level"] == 1),
            key=lambda card: card["sequence"],
        )

        self.assertEqual([card["id"] for card in foundations], FOUNDATION_SEQUENCE)
        self.assertEqual(foundations[0]["id"], "h01")
        self.assertNotIn("python", {card["module"] for card in foundations})
        self.assertTrue(all(len(card["explanation"]) >= 120 for card in foundations))
        self.assertLess(
            next(card["sequence"] for card in foundations if card["id"] == "o01"),
            next(card["sequence"] for card in foundations if card["id"] == "d08"),
        )
        self.assertEqual(
            next(card["prerequisites"] for card in foundations if card["id"] == "d08"),
            ["o01", "d12", "p04"],
        )

    def test_backend_primers_cover_the_request_to_database_path(self):
        primers = [card for card in CARDS if card["id"].startswith("b")]

        self.assertEqual([card["id"] for card in primers], [f"b{i:02}" for i in range(1, 17)])
        self.assertTrue(all(card["level"] == 0 for card in primers))
        self.assertTrue(all(card["context"] and card["explanation"] for card in primers))

    def test_level_zero_teaches_vocabulary_before_framework_code(self):
        introductions = sorted(
            (card for card in CARDS if card["level"] == 0),
            key=lambda card: card["sequence"],
        )

        self.assertEqual([card["id"] for card in introductions], LEVEL_ZERO_SEQUENCE)
        self.assertEqual(introductions[0]["id"], "z01")
        self.assertEqual(introductions[-1]["id"], "z18")
        self.assertGreaterEqual(len(introductions), 30)
        self.assertTrue(all(card["context"] and card["explanation"] for card in introductions))
        self.assertLess(
            next(card["sequence"] for card in introductions if card["id"] == "z07"),
            next(card["sequence"] for card in introductions if card["id"] == "b10"),
        )

    def test_interview_cards_live_in_final_level(self):
        interview_cards = [card for card in CARDS if card["module"] == "entrevista"]

        self.assertTrue(interview_cards)
        self.assertTrue(all(card["level"] == 4 for card in interview_cards))

    def test_complex_cards_include_context_and_first_principles(self):
        contextual = [card for card in CARDS if card["context"]]
        explained = [card for card in CARDS if card["explanation"]]

        self.assertGreaterEqual(len(contextual), 30)
        self.assertGreaterEqual(len(explained), 30)
        self.assertTrue(all(len(card["context"]) >= 60 for card in contextual))
        self.assertTrue(all(len(card["explanation"]) >= 120 for card in explained))

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

    def test_short_case_studies_have_complete_learning_flow(self):
        cases = [card for card in CARDS if card["kind"] == "mini caso"]

        self.assertGreaterEqual(len(cases), 28)
        for card in cases:
            with self.subTest(card=card["id"]):
                self.assertTrue(card["context"])
                self.assertTrue(card["code"])
                self.assertTrue(card["answer_code"])
                self.assertTrue(card["explanation"])

    def test_study_page_exposes_case_study_filter(self):
        response = self.client.get(reverse("trainer:study"))

        self.assertContains(response, '<option value="casos">Mini-casos</option>')


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

    def test_study_page_exposes_progressive_curriculum(self):
        response = self.client.get(reverse("trainer:study"))

        self.assertContains(response, "Tu camino hasta la entrevista")
        self.assertContains(response, 'data-level-choice="0"')
        self.assertContains(response, 'data-level-choice="1"')
        self.assertContains(response, 'data-level-choice="4"')
        self.assertContains(response, "100% visto")

    def test_cards_api_can_filter_by_module(self):
        response = self.client.get(reverse("trainer:cards_api"), {"module": "drf"})

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        expected = sum(card["module"] == "drf" for card in CARDS)
        self.assertEqual(payload["count"], expected)
        self.assertTrue(all(card["module"] == "drf" for card in payload["cards"]))
        self.assertEqual(len(payload["curriculum"]), 5)

    def test_meta_api_exposes_deck_stats(self):
        payload = self.client.get(reverse("trainer:meta_api")).json()

        self.assertEqual(payload["cards"], len(CARDS))
        self.assertEqual(len(payload["modules"]), len(MODULES))
        self.assertEqual(payload["module_count"], len(MODULES))
        self.assertEqual(payload["with_code"], len(CARDS))
        self.assertEqual(payload["verdicts"], 20)
        self.assertEqual(len(payload["curriculum"]), 5)
