from tt.position import *

class TestPosition:

    def __init__(self):
        self.zgzt = Position('601390')

    def test_init(self):
        assert self.zgzt.sid == '601390'
