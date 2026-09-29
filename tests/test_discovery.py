import unittest

from src.discovery import generate_discovery


class DiscoveryTests(unittest.TestCase):
    def test_generates_prioritized_mvp_backlog_from_a_product_idea(self):
        result = generate_discovery(
            "Uma plataforma para pequenos lojistas acompanharem pedidos e estoque"
        )

        self.assertTrue(result["problem_statement"])
        self.assertGreaterEqual(len(result["hypotheses"]), 2)
        self.assertGreaterEqual(len(result["user_stories"]), 3)
        self.assertEqual(result["backlog"][0]["priority"], "Must have")
        self.assertTrue(all(item["acceptance_criteria"] for item in result["user_stories"]))

    def test_rejects_an_empty_product_idea(self):
        with self.assertRaisesRegex(ValueError, "product idea must not be empty"):
            generate_discovery("  ")


if __name__ == "__main__":
    unittest.main()
