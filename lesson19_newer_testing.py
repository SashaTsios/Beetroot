import unittest
from lesson19_newergame2d_WO_test import Car


class GameTest(unittest.TestCase):

    def setUp(self):
        self.car_test = Car('SuperBrand', 'SuperModel', 'SuperColor', 1, [0, 0])

    def test_move_left_2_steps_defaul_speed(self):
        self.assertEqual(self.car_test.move_left(2, 1), [-2, 0])

    def test_change_speed_from_1_to_5(self):
        self.assertEqual(self.car_test.change_speed(5), 5)

    def test_move_left_3_steps_changed_to_5_speed(self):
        self.car_test.change_speed(5)
        self.assertEqual(self.car_test.move_left(3), [-15, 0])

    def test_move_left_3_steps_changed_to_10_speed(self):
        self.assertEqual(self.car_test.move_left(3, 10), [-30, 0])

    def test_combination(self):
        self.assertEqual(self.car_test.move_left(10), [-10, 0])
        self.car_test.change_speed(5)
        self.assertEqual(self.car_test.move_left(1), [-15, 0])
        self.assertEqual(self.car_test.move_left(2, 10), [-35, 0])
        self.assertEqual(self.car_test.current_position(), [-35, 0])
        self.assertEqual(self.car_test.move_right(1, 35), [0, 0])


if __name__ == '__main__':
    unittest.main()
