import itertools
import streamlit as st

st.header("Killer Sudoku!")

if "nums" not in st.session_state:
    # list(range(1, 10))  # generate numbers from 1 to 9.
    st.session_state.nums = list(range(1, 10))


def combinationSum2(txt):
    d = []
    txt = txt.split(",")
    newnums = [int(i) for i in txt]
    pairs = list(zip(newnums[::2], newnums[1::2]))
    for numofnums, totals in pairs:
        # generate all combinations of k digits from nums.
        combinations = itertools.combinations(st.session_state.nums, numofnums)
        # filter the combinations whose sum is equal to n.
        d.append([list(i) for i in combinations if sum(i) == totals])

    searchterms = list(itertools.product(*d))
    for counter in searchterms:
        flat_list = [num for sublist in counter for num in sublist]
        if len(set(flat_list)) == len(flat_list):
            st.write(counter)


def pairup(*mynums):
    res = list(zip(mynums[::2], mynums[1::2]))
    st.write(res)
    combinationSum2(res)


st.write("Numbers")

col1, col2, col3 = st.columns(3)


def flip_num(btext, bnum):
    if st.button(btext):
        if bnum in st.session_state.nums:
            st.session_state.nums.remove(bnum)
        else:
            st.session_state.nums.insert(bnum-1, bnum)


with col1:
    flip_num("1", 1)
    flip_num("4", 4)
    flip_num("7", 7)
with col2:
    flip_num("2", 2)
    flip_num("5", 5)
    flip_num("8", 8)
with col3:
    flip_num("3", 3)
    flip_num("6", 6)
    flip_num("9", 9)


if st.button("Reset"):
    del st.session_state.nums
    st.session_state.nums = list(range(1, 10))  # generate numbers from 1 to 9.

st.write(st.session_state.nums)

inputnums = st.text_input('Input numbers')
if st.button("Run"):
    combinationSum2(inputnums)
    #pairup(3, 10, 3, 14)
