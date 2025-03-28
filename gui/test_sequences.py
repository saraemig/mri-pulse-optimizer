from app.sequences import get_spin_echo_sequence

def test_sequence_length():
    seq = get_spin_echo_sequence(90, 1000)
    assert len(seq) == 4
