import simpletest

def run_suite(game):
    """
    Some informal testing code. 
    Uncomment self.new_tile() lines in reset method!
    """

    # create a TestSuite object
    suite = simpletest.TestSuite()
    
    # test game on reset
    game.height = 2
    game.width = 3
    suite.run_test(game.reset(), [[0, 0, 0], [0, 0, 0]], "Test #1:")

    game.height = 4
    game.width = 5
    suite.run_test(game.reset(), [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], "Test #2:")

    # test game on print
    suite.run_test(str(game), "\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n[0, 0, 0, 0, 0]\n", "Test #3:")
    suite.run_test(str(game), 
"""
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test #4:")

    game.height = 2
    game.width = 3
    game.reset()

    # test set_tile
    game.set_tile(5, 5, 4)
    suite.run_test(str(game), 
"""
[0, 0, 0]
[0, 0, 0]
""", "Test #5:")

    game.set_tile(0, 2, 8)
    suite.run_test(str(game), 
"""
[0, 0, 8]
[0, 0, 0]
""", "Test #6:")

    game.set_tile(1, 1, 5)
    suite.run_test(str(game), 
"""
[0, 0, 8]
[0, 5, 0]
""", "Test #7:")

    # test get_tile
    suite.run_test(game.get_tile(0, 0), 0, "Test #8:")
    suite.run_test(game.get_tile(0, 2), 8, "Test #9:")
    suite.run_test(game.get_tile(1, 1), 5, "Test #10:")
    suite.run_test(game.get_tile(5, 1), None, "Test #11:")

    # pseudo-test new_tile
    game.height = 4
    game.width = 5

    # game.reset()
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game
    # game.new_tile(); print game

    # test initial tiles dictionary

    game.reset()
    game.set_tile(0, 1, 2)
    game.set_tile(1, 0, 4)
    game.set_tile(1, 1, 4)
    game.set_tile(2, 1, 2)
    game.set_tile(3, 2, 8)
    game.set_tile(3, 3, 8)
    game.set_tile(1, 4, 2)
    game.set_tile(0, 4, 2)
    game.set_tile(2, 0, 4)

    # [0, 2, 0, 0, 2]
    # [4, 4, 0, 0, 2]
    # [4, 2, 0, 0, 0]
    # [0, 0, 8, 8, 0]

    suite.run_test(game.initial[1], [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)], "Test #12:")
    suite.run_test(game.initial[2], [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4)], "Test #13:")
    suite.run_test(game.initial[3], [(0, 0), (1, 0), (2, 0), (3, 0)], "Test #14:")
    suite.run_test(game.initial[4], [(0, 4), (1, 4), (2, 4), (3, 4)], "Test #15:")

    # test move
    suite.run_test(game.move(1), 
"""
[8, 2, 8, 8, 4]
[0, 4, 0, 0, 0]
[0, 2, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test #16")
    
    suite.run_test(game.move(3), 
"""
[8, 2, 16, 4, 0]
[4, 0, 0, 0, 0]
[2, 0, 0, 0, 0]
[0, 0, 0, 0, 0]
""", "Test #17")
    
    suite.run_test(game.move(2), 
"""
[0, 0, 0, 0, 0]
[8, 0, 0, 0, 0]
[4, 0, 0, 0, 0]
[2, 2, 16, 4, 0]
""", "Test #18")

    suite.run_test(game.move(4), 
"""
[0, 0, 0, 0, 0]
[0, 0, 0, 0, 8]
[0, 0, 0, 0, 4]
[0, 0, 4, 16, 4]
""", "Test #19")

    suite.report_results()
