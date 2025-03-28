def get_spin_echo_sequence(TE, TR, flip_angle=90):
    return [
        {'time': 0, 'event': 'RF', 'flip_angle': flip_angle},
        {'time': TE / 2, 'event': '180 RF', 'flip_angle': 180},
        {'time': TE, 'event': 'Echo'},
        {'time': TR, 'event': 'Repeat'}
    ]
