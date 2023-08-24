import unittest

class TestScraping(unittest.TestCase):
    def test_csv_file(self):
        with open("ia-data.csv", mode="r", encoding="utf-8") as file:
            lines = file.readlines()

            self.assertTrue(len(lines) > 1) 

if __name__ == '__main__':
    unittest.main()
