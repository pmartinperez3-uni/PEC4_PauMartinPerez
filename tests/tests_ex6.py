import os
import sys
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from exercises.ex6 import fun_total_goals  # noqa: E402


class TestFunTotalGoals(unittest.TestCase):
    """Tests unitarios para la función fun_total_goals."""

    def setUp(self):
        """Crea un DataFrame pequeño de prueba."""
        self.data = pd.DataFrame({
            "FTHG": [3, 1, 0, 2],
            "FTAG": [0, 2, 1, 1],
        })

    def test_home_goals(self):
        """Los goles totales del local deben ser la suma de FTHG."""
        home, _, _ = fun_total_goals(self.data)
        self.assertEqual(home, 6)

    def test_away_goals(self):
        """Los goles totales del visitante deben ser la suma de FTAG."""
        _, away, _ = fun_total_goals(self.data)
        self.assertEqual(away, 4)

    def test_total_goals(self):
        """Los goles totales deben ser la suma de home + away."""
        home, away, total = fun_total_goals(self.data)
        self.assertEqual(total, home + away)
        self.assertEqual(total, 10)

    def test_return_types(self):
        """Todos los valores devueltos deben ser enteros."""
        home, away, total = fun_total_goals(self.data)
        self.assertIsInstance(home, int)
        self.assertIsInstance(away, int)
        self.assertIsInstance(total, int)

    def test_empty_dataframe(self):
        """Un DataFrame vacío debe devolver ceros."""
        empty = pd.DataFrame({"FTHG": [], "FTAG": []})
        home, away, total = fun_total_goals(empty)
        self.assertEqual(home, 0)
        self.assertEqual(away, 0)
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()
