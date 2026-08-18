"""demo-service — the simplest possible app for practicing our git flow.

Run it:        python3 app.py
Run its tests: python3 -m unittest app
"""

VERSION = "0.1.0"


def greet(name="world"):
    return f"hello {name}, this is demo-service {VERSION}"


# --- tests live in the same file to keep the demo to one .py file ---
import unittest


class TestGreet(unittest.TestCase):
    def test_default_greeting(self):
        self.assertEqual(greet(), f"hello world, this is demo-service {VERSION}")

    def test_greeting_uses_the_name(self):
        self.assertIn("sparta", greet("sparta"))


if __name__ == "__main__":
    print(greet())
