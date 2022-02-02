from sequence_generation import seq_binary
from vector_utils import rotate_n, reverse, rotate_right


def find_necklace(sequence):
    potential_necklace = sequence.copy()
    for k in range(1, len(sequence)):
        rotated_sequence = rotate_n(sequence, k)
        if potential_necklace > rotated_sequence:
            potential_necklace = rotated_sequence
    return potential_necklace


def equal_necklaces(sequence_a, sequence_b):
    return find_necklace(sequence_a) == find_necklace(sequence_b)


def successor(sequence):
    len_sequence = len(sequence)
    largest_index_equal_to_zero = find_largest_index_equal_to_zero(sequence)

    if largest_index_equal_to_zero is None:
        return None

    mod_sequence = sequence[:largest_index_equal_to_zero] + [1]
    t = len_sequence // (largest_index_equal_to_zero + 1)
    j = len_sequence % (largest_index_equal_to_zero + 1)

    return repeat_tth_times_and_fill_jth_values(mod_sequence, t, j)


def fkm_algorithm(start, end):

    if len(start) != len(end):
        return None

    l = len(start)

    start_necklace = find_necklace(start)
    end_necklace = find_necklace(end)

    current = min(start_necklace, end_necklace)
    real_end = max(start_necklace, end_necklace)

    yield current

    while current < real_end:
        i = find_largest_index_equal_to_zero(current) + 1
        t = l // i
        j = l % i

        mod_current = current[: i - 1] + [1]
        current = repeat_tth_times_and_fill_jth_values(mod_current, t, j)
        if j == 0:
            yield current


def seq_necklaces_of_half_density(length):
    density = length // 2
    current = [0] * (length - density) + [1] * density
    last_necklace = [(i + 1) % 2 for i in range(length)]
    last_necklace[0] = 0

    yield current
    while current < last_necklace:
        i = find_largest_index_equal_to_zero(current) + 1
        t = length // i
        j = length % i

        mod_current = current[: i - 1] + [1]
        current = repeat_tth_times_and_fill_jth_values(mod_current, t, j)
        if j == 0 and sum(current) == density:
            yield current
    return


def find_largest_index_equal_to_zero(sequence):
    for k in range(len(sequence) - 1, -1, -1):
        if sequence[k] == 0:
            return k

    return None


def repeat_tth_times_and_fill_jth_values(sequence, t, j):
    return sequence * t + sequence[:j]


def find_bracelet(sequence):
    potential_bracelet = sequence.copy()
    for n in range(len(sequence)):
        rotated_sequence = rotate_n(sequence, n)
        if rotated_sequence < potential_bracelet:
            potential_bracelet = rotated_sequence
        reverse_rotated_sequence = reverse(rotated_sequence)
        if reverse_rotated_sequence < potential_bracelet:
            potential_bracelet = reverse_rotated_sequence
    return potential_bracelet


def find_bracelet_from_necklace(sequence):
    potential_bracelet = sequence.copy()
    reverse_sequence = reverse(sequence)
    for n in range(len(sequence)):
        reverse_rotated_sequence = rotate_n(reverse_sequence, n)
        if reverse_rotated_sequence < potential_bracelet:
            potential_bracelet = reverse_rotated_sequence
    return potential_bracelet


def seq_bracelets_of_half_density(length):
    density = length // 2
    current = [0] * (length - density) + [1] * density
    last_necklace = [(i + 1) % 2 for i in range(length)]
    last_necklace[0] = 0

    yield current
    while current < last_necklace:
        i = find_largest_index_equal_to_zero(current) + 1
        t = length // i
        j = length % i

        mod_current = current[: i - 1] + [1]
        current = repeat_tth_times_and_fill_jth_values(mod_current, t, j)
        if (
            j == 0
            and sum(current) == density
            and current == find_bracelet_from_necklace(current)
        ):
            yield current
    return


def seq_bracelets(sequences):

    observed_sequences = set()
    for seq in sequences:
        if tuple(seq) not in observed_sequences:
            seen_seq = seq.copy()
            for k in range(len(seen_seq)):
                seen_seq = rotate_right(seen_seq)
                observed_sequences.add(tuple(seen_seq))
                observed_sequences.add(tuple(reverse(seen_seq)))

            yield seq

    return


def main():  # pragma: no cover
    print("Entry point for playing around")
    n = 7
    sequences = [seq for seq in fkm_algorithm([0] * n, [1] * n)]
    count = 0

    for seq in sequences:
        print(
            f"seq {seq} density {sum(seq)} count {count} is bracelet {seq == find_bracelet(seq)}"
        )
        count += 1

    print(len(sequences))

    count = 0
    bracelet = set()
    for seq in sequences:
        seq_bracelet = tuple(find_bracelet(seq))
        if seq_bracelet not in bracelet:
            print(f"seq_bracelet {seq_bracelet} count {count}")
            count += 1
            bracelet.add(seq_bracelet)
    print(count)


if __name__ == "__main__":  # pragma: no cover
    main()
