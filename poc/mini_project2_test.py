import simpletest

def run_suite(game):
    """Some informal testing code"""

    # create a TestSuite object
    suite = simpletest.TestSuite()
    
    # test game on reset
    game.height = 2
    game.width = 3
    suite.run_test(game.reset(), [[0, 0, 0], [0, 0, 0]], "Test #1:")

    game.width = 5
    game.height = 4
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

    suite.report_results()


