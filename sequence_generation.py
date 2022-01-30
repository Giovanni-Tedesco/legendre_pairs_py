from vector_utils import reverse, rotate_right
from dft_utils import psd_k, psd


def seq_binary(n):
    if n == 1:
        yield [0]
        yield [1]
    elif n > 1:
        for l in seq_binary(n - 1):
            yield [0] + l
            yield [1] + l

    return


def seq_n_choose_k(n, k):
    if k == 0:
        yield [0] * n
    elif n == k:
        yield [1] * n
    elif n > k:
        for previous_n_current_k in seq_n_choose_k(n - 1, k):
            yield [0] + previous_n_current_k

        for previous_n_previous_k in seq_n_choose_k(n - 1, k - 1):
            yield [1] + previous_n_previous_k

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


"""
def seq_filtering_by_psd(sequences, gamma):
    eps = 1e-10
    return filter(
        lambda x: all([psd_k(x, k) + eps <= gamma for k in range(1, len(x))]), sequences
    )
"""


def seq_filtering_by_psd(sequences, gamma):
    eps = 1e-10
    # filter(lambda x: all([psd_k(x, k) - eps > gamma for k in range(1, len(x))]), sequences)
    for seq in sequences:
        is_psd_bounded_by_gamma = True
        for k in range(1, len(seq)):
            if psd_k(seq, k) - eps > gamma:
                is_psd_bounded_by_gamma = False
                break
        if is_psd_bounded_by_gamma:
            yield seq

    return


def main():  # pragma: no cover
    print("Entry point for playing around")

    n = 27
    gamma = (n + 1) // 2
    kappa = (n - 1) // 2

    bracelets = [seq for seq in seq_bracelets(seq_n_choose_k(n, kappa))]
    filtered_bracelets = [seq for seq in seq_filtering_by_psd(bracelets, gamma)]

    print(
        f"number of bracelents {len(bracelets)} vs number of filtered {len(filtered_bracelets)}"
    )


if __name__ == "__main__":  # pragma: no cover
    main()

"""
seq [0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1] psd [36.0, 5.992228533552934, 4.115459702550342, 1.0328632577910675, 3.609264479338426, 0.2501840267672326, 0.25018402676723245, 3.6092644793384263, 1.0328632577910666, 4.1154597025503445, 5.992228533552935]
seq [0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1] psd [36.0, 4.9671367422089325, 5.749815973232767, 1.8845402974496577, 0.007771466447067587, 2.3907355206615755, 2.390735520661576, 0.007771466447067636, 1.8845402974496568, 5.74981597323277, 4.967136742208933]
seq [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1] psd [36.0, 4.115459702550343, 3.609264479338425, 0.25018402676723245, 1.0328632577910666, 5.992228533552935, 5.992228533552932, 1.032863257791068, 0.2501840267672326, 3.6092644793384254, 4.1154597025503445]
seq [0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1] psd [36.0, 3.0, 3.0000000000000004, 3.0000000000000018, 3.0000000000000004, 3.000000000000001, 2.9999999999999996, 2.9999999999999996, 3.0000000000000018, 3.0000000000000013, 3.0000000000000004]
seq [0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1] psd [36.0, 3.6092644793384245, 1.0328632577910666, 5.992228533552932, 0.2501840267672327, 4.115459702550344, 4.115459702550344, 0.25018402676723245, 5.992228533552933, 1.0328632577910677, 3.6092644793384263]
seq [0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1] psd [36.0, 5.749815973232765, 0.007771466447067529, 2.390735520661574, 1.8845402974496552, 4.967136742208934, 4.967136742208935, 1.8845402974496563, 2.390735520661576, 0.00777146644706747, 5.749815973232768]
seq [0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1] psd [36.0, 1.884540297449657, 2.3907355206615755, 5.749815973232767, 4.967136742208934, 0.007771466447067615, 0.007771466447067582, 4.967136742208933, 5.74981597323277, 2.390735520661576, 1.8845402974496577]
seq [0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1] psd [36.0, 2.3907355206615746, 4.967136742208935, 0.007771466447067499, 5.749815973232767, 1.8845402974496552, 1.8845402974496563, 5.749815973232768, 0.007771466447067547, 4.967136742208934, 2.390735520661576]
seq [0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1] psd [36.0, 1.0328632577910677, 0.2501840267672326, 4.115459702550342, 5.992228533552933, 3.6092644793384236, 3.6092644793384236, 5.992228533552933, 4.115459702550344, 0.25018402676723284, 1.0328632577910684]
seq [0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1] psd [36.0, 0.25018402676723245, 5.992228533552932, 3.6092644793384263, 4.115459702550344, 1.0328632577910666, 1.0328632577910675, 4.115459702550344, 3.6092644793384254, 5.992228533552936, 0.25018402676723267]
seq [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1] psd [36.0, 0.007771466447067577, 1.884540297449657, 4.967136742208933, 2.3907355206615755, 5.7498159732327725, 5.749815973232765, 2.390735520661576, 4.967136742208934, 1.8845402974496572, 0.007771466447067624]
"""

"""
21 -> 8524 vs number of filtered 610
25 -> 104468 vs number of filtered 3780
27 -> 372308 vs number of filtered 10809
"""
