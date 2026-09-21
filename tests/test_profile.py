import unittest

from scripts.validate_profile import validate


class ProfileIntegrityTests(unittest.TestCase):
    def test_profile_is_evidence_scoped(self) -> None:
        self.assertEqual([], validate())


if __name__ == "__main__":
    unittest.main()
