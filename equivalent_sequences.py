from vector_utils import circular_correlation, rotate_left, reverse
from sequence_generation import seq_binary


def find_sequences_with_same_correlation(n):
    correlation_to_sequences = dict()
    for sequence in seq_binary(n):
        correlation_a = tuple(circular_correlation(sequence, sequence))
        if correlation_a not in correlation_to_sequences.keys():
            correlation_to_sequences[correlation_a] = [sequence]
        else:
            correlation_to_sequences[correlation_a] = correlation_to_sequences[
                correlation_a
            ] + [sequence]
    return correlation_to_sequences


def find_rotation_and_reversal_orbit(sequence: list):
    orbit = set()
    modified_sequence = sequence.copy()
    for k in range(len(sequence)):
        modified_sequence = rotate_left(modified_sequence)
        orbit.add(tuple(modified_sequence))
        orbit.add(tuple(reverse(modified_sequence)))

    return orbit


def main():  # pragma: no cover
    orbit = find_rotation_and_reversal_orbit([1, 2, 3])
    print(orbit)


if __name__ == "__main__":  # pragma: no cover
    main()