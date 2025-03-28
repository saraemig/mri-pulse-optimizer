import matplotlib.pyplot as plt

def plot_sequence(sequence):
    times = [event['time'] for event in sequence]
    labels = [event['event'] for event in sequence]

    plt.figure(figsize=(10, 2))
    for t, label in zip(times, labels):
        plt.axvline(x=t, linestyle='--', color='b')
        plt.text(t, 0.5, label, rotation=90, verticalalignment='center')
    plt.yticks([])
    plt.title("Pulse Sequence Timeline")
    plt.xlabel("Time (ms)")
    plt.tight_layout()
    plt.show()
