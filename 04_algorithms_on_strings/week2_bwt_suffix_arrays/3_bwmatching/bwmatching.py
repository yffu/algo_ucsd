# python3
import sys
debug = False


def last_to_first(bwt, bwt_sort):
    cnt_b = dict()
    cnt_i = dict()
    lf = [None] * len(bwt)
    prev = None
    for i in range(len(bwt_sort)):
        if bwt_sort[i] != prev:
            cnt_b[bwt_sort[i]] = i
        prev = bwt_sort[i]

    for i in range(len(bwt)):
        if bwt[i] in cnt_i:
            cnt_i[bwt[i]] += 1
        else:
            cnt_i[bwt[i]] = 1
        lf[i] = cnt_b[bwt[i]] + cnt_i[bwt[i]] - 1
    return lf


def bwtmatching_naive(bwt, pattern):
    first_col = "".join(sorted(bwt))
    last_col = bwt
    lf = last_to_first(last_col, first_col)
    if debug:
        print("first col: {}, last col: {}, lf: {}".format(first_col, last_col, lf))
    top = 0
    btm = len(last_col) - 1
    while top <= btm:
        if pattern:
            symbol = pattern[-1:]
            pattern = pattern[:-1]
            top_i = bwt.find(symbol, top, btm + 1)
            btm_i = bwt.rfind(symbol, top, btm + 1)
            if top_i >= 0 and btm_i >= 0:
                top = lf[top_i]
                btm = lf[btm_i]
            else:
                return 0
        else:
            return btm - top + 1


def PreprocessBWT(bwt):
    """
    Preprocess the Burrows-Wheeler Transform bwt of some text
    and compute as a result:
      * starts - for each character C in bwt, starts[C] is the first position
          of this character in the sorted array of
          all characters of the text.
      * occ_count_before - for each character C in bwt and each position P in bwt,
          occ_count_before[C][P] is the number of occurrences of character C in bwt
          from position 0 to position P inclusive.
    """
    bwt_len = len(bwt)
    bwt_sort = sorted(bwt)
    starts = dict()
    prev = None
    for i in range(bwt_len):
        if bwt_sort[i] != prev:
            starts[bwt_sort[i]] = i
            prev = bwt_sort[i]
    occ_count_before = {x: [0]*(bwt_len + 1) for x in starts.keys()}
    for i in range(0, bwt_len):
        for k in occ_count_before:
            v = occ_count_before[k]
            if bwt[i] == k:
                v[i+1] = v[i] + 1
            else:
                v[i+1] = v[i]
    return starts, occ_count_before


def CountOccurrences(pattern, bwt, starts, occ_counts_before):
    """
    Compute the number of occurrences of string pattern in the text
    given only Burrows-Wheeler Transform bwt of the text and additional
    information we get from the preprocessing stage - starts and occ_counts_before.
    """
    top = 0
    btm = len(bwt) - 1
    while top <= btm:
        if pattern:
            symbol = pattern[-1:]
            pattern = pattern[:-1]
            if bwt.find(symbol, top, btm+1) != -1:
                top = starts[symbol] + occ_counts_before[symbol][top]
                btm = starts[symbol] + occ_counts_before[symbol][btm+1] - 1
            else:
                return 0
        else:
            return btm - top + 1


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    pattern_count = int(sys.stdin.readline().strip())
    patterns = sys.stdin.readline().strip().split()
    # Preprocess the BWT once to get starts and occ_count_before.
    # For each pattern, we will then use these precomputed values and
    # spend only O(|pattern|) to find all occurrences of the pattern
    # in the text instead of O(|pattern| + |text|).
    starts, occ_counts_before = PreprocessBWT(bwt)
    if debug:
        print("starts: {}".format(starts))
        print("occ_counts_before: {}".format(occ_counts_before))
    occurrence_counts = []
    occurrence_counts_naive = []
    for pattern in patterns:
        #occurrence_counts_naive.append(bwtmatching_naive(bwt, pattern))
        occurrence_counts.append(CountOccurrences(pattern, bwt, starts, occ_counts_before))
    #print(' '.join(map(str, occurrence_counts_naive)))
    print(' '.join(map(str, occurrence_counts)))
