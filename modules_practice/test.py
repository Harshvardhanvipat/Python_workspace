import unittest
import randomgame


class TestGame(unittest.TestCase):
    def test_input(self):
        result = randomgame.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = randomgame.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_out_of_order_guess(self):
        result = randomgame.run_guess(15, 0)
        self.assertFalse(result)

    def test_input_string(self):
        result = randomgame.run_guess(15, 'sdefsf')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
