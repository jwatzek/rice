import simpletest

def run_suite(game):
    """Some informal testing code"""

    # create a TestSuite object
    suite = simpletest.TestSuite()
    
    # test game on reset
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


    suite.report_results()