import unittest
from website.utils import get_external_data

class TestExternalRequest(unittest.TestCase):

    def test_instance(self):
        req = get_external_data()
        self.assertTrue(isinstance(req, dict))

if __name__ == "__main__":
    unittest.main()