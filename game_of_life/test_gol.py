import unittest
from parameterized import parameterized
from gol import evolve, count_neighbours


class TestGOL(unittest.TestCase):
    @parameterized.expand([
        ("underpopulation_0_neighbours", 0, False, False),
        ("underpopulation_2_neighbours", 2, False, False),
        ("stay_alive_2_neighbours", 2, True, True),
        ("stay_alive_3_neighbours", 3, True, True),
        ("resurrection", 3, False, True),
        ("overpopulation_and alive", 4, True, False),
        ("overpopulation_and_dead", 4, False, False),
    ])
    def test_gol_rules(self, name, alive_neighbours, cell_is_alive, result):
        is_alive = evolve(alive_neighbours=alive_neighbours, cell_is_alive=cell_is_alive)
        self.assertEqual(is_alive, result, msg=name)

    @parameterized.expand([
        ("0 neighbours", [(0, 0, 0),  # board
                          (0, 0, 0),
                          (0, 0, 0)],
                          (1, 1),  # position
                          0),  # alive_neighbours
        ("1 neighbours", [(1, 0, 0),  # board
                          (0, 0, 0),
                          (0, 0, 0)],
         (1, 1),  # position
         1),  # alive_neighbours
        ("8 neighbours", [(1, 1, 1),  # board
                          (1, 1, 1),
                          (1, 1, 1)],
         (1, 1),  # position
         8),  # alive_neighbours
        ("5 neighbours", [(0, 1, 1, 1),  # board
                          (0, 1, 1, 1),
                          (0, 0, 0, 0),
                          (0, 0, 0, 0)],
        (1, 2),  # position
         5),  # alive_neighbours
    ])
    def test_alive_neighbours(self, name, board, position, result):
        alive_neighbours = count_neighbours(board, position)
        self.assertEqual(alive_neighbours, result, msg=name)



if __name__ == '__main__':
    unittest.main()
