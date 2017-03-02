from tt.position import Position

# Sample instance for testing
GHZQ = Position('000750')
ZGZT = Position('601390')
ZGCB = Position('600150')


def test_init():
    assert ZGZT.sid == '601390'
    assert ZGCB.sid == '600150'

def test_records():
    assert len(GHZQ.records) == 11
    assert len(ZGZT.records) == 12

