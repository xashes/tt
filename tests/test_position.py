"""
Test cases for Position Class
"""

from tt.position import Position

# Sample instance for testing
ZGZT = Position('601390')
ZGCB = Position('600150')


def test_init():
    """
    test cases for __init__ method
    """
    assert ZGZT.sid == '601390'
    assert ZGCB.sid == '600150'
