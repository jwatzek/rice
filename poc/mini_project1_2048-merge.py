"""
Merge function for 2048 game.
"""

def slide(line):
    """
    Slide all non-zero values to the front of the list (lower indices). Returns
    list of same length.
    """
    result = [0] * len(line)
    idx = 0
    for entry in line:
        if entry != 0:
            result[idx] = entry
            idx += 1
    return result

def pair(line):
    """
    Pair adjacent tiles of the same value. Returns list of same length with 
    one tile of twice the value and a zero tile.
    """
    result = list(line)
    prev_merged = False

    for idx in range(len(line) - 1):
        if not prev_merged and line[idx] == line[idx + 1]:
            result[idx] *= 2
            result[idx + 1] *= 0
            prev_merged = True
        else:
            prev_merged = False

    return result

def merge(line):
    """Merges a single row or column in 2048."""
    slid = slide(line)
    paired = pair(slid)
    return slide(paired)

def test_merge():
    """Test code for 2048 merge function"""

    print 'Testing slide - computed:', slide([1]), 'expected:', [1]
    print 'Testing slide - computed:', slide([2, 0, 2, 4]), 'expected:', [2, 2, 4, 0]
    print 'Testing slide - computed:', slide([0, 0, 2, 2]), 'expected:', [2, 2, 0, 0]
    print 'Testing slide - computed:', slide([2, 2, 0, 0]), 'expected:', [2, 2, 0, 0]
    print 'Testing slide - computed:', slide([2, 2, 2, 2, 2]), 'expected:', [2, 2, 2, 2, 2]
    print 'Testing slide - computed:', slide([8, 16, 16, 8]), 'expected:', [8, 16, 16, 8]
    print

    print 'Testing pair - computed:', pair([1]), 'expected:', [1]
    print 'Testing pair - computed:', pair(slide([2, 0, 2, 4])), 'expected:', [4, 0, 4, 0]
    print 'Testing pair - computed:', pair(slide([0, 0, 2, 2])), 'expected:', [4, 0, 0, 0]
    print 'Testing pair - computed:', pair(slide([2, 2, 0, 0])), 'expected:', [4, 0, 0, 0]
    print 'Testing pair - computed:', pair(slide([2, 2, 2, 2, 2])), 'expected:', [4, 0, 4, 0, 2]
    print 'Testing pair - computed:', pair(slide([8, 16, 16, 8])), 'expected:', [8, 32, 0, 8]
    print

    print 'Testing merge - computed:', merge([1]), 'expected:', [1]
    print 'Testing merge - computed:', merge([2, 0, 2, 4]), 'expected:', [4, 4, 0, 0]
    print 'Testing merge - computed:', merge([0, 0, 2, 2]), 'expected:', [4, 0, 0, 0]
    print 'Testing merge - computed:', merge([2, 2, 0, 0]), 'expected:', [4, 0, 0, 0]
    print 'Testing merge - computed:', merge([2, 2, 2, 2, 2]), 'expected:', [4, 4, 2, 0, 0]
    print 'Testing merge - computed:', merge([8, 16, 16, 8]), 'expected:', [8, 32, 8, 0]
    print

test_merge()