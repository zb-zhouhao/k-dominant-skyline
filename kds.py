#!/usr/bin/env python3

import sys, os
sys.path.append(os.curdir)

# from Compiler.program import Program, defaults
from Compiler.program import Program, defaults
opts = defaults()

prog = Program(['kds'], opts)
prog.use_edabit(True)

from Compiler.library import print_ln, for_range, if_, if_e, else_, break_loop
from Compiler.types import sint, Array, Matrix


# set_up
silo = 6
nums = 5
k = 6
combine_list = []
V = [0] * silo
T = []
M = Matrix(nums, silo, sint)

hit = Array(nums, sint)
hit.assign_all(0)

k_dom = Array(nums, sint)
k_dom.assign_all(0)

cond1_array = Array(k, sint)
cond2_array = Array(k, sint)

isDominant = Array(1, sint)

def combine(m, n, src, N):
    if not n:
        combine_list.append(list(T))
        return
    for i in range(src, m):
        if not V[i]:
            V[i] = 1
            T.append(i)
            combine(m, n-1, i + 1, N)
            del T[-1]
            V[i] = 0

def k_dominate(a, b):
    cond2 = Array(2, sint)
    cond2[0] = sint(0)
    cond2[1] = sint(1)
    
    @for_range(k)
    def _(i):
        cond2[0] = (a[i] == sint(1)).if_else(sint(1), cond2[0])
        cond2[1] = (b[i] == sint(1)).if_else(sint(0), cond2[1])
    cond2[0] =  cond2[0] * cond2[1]
    return cond2[0] > sint(0)

combine(silo, k, 0, k)
# print(combine_list)
t1_array = Array(silo, sint)
t2_array = Array(silo, sint)

@for_range(nums)
def _(i):
    @for_range(i+1, nums)
    def _(j):
        for t in range(silo):
            t1_array[t] = sint.get_input_from(t)
            t2_array[t] = sint.get_input_from(t)
        for t in range(len(combine_list)):
            for v in range(k):
                cond1_array[v] = t1_array[combine_list[t][v]]
                cond2_array[v] = t2_array[combine_list[t][v]]
        # p_i k_dom p_j?
            M[i][j] = k_dominate(cond1_array, cond2_array).if_else(sint(1), M[i][j])

        for t in range(silo):
            t1_array[t] = sint.get_input_from(t)
            t2_array[t] = sint.get_input_from(t)
        for t in range(len(combine_list)):
            for v in range(k):
                cond1_array[v] = t1_array[combine_list[t][v]]
                cond2_array[v] = t2_array[combine_list[t][v]]
        # p_j k_dom p_i?
            M[j][i] = k_dominate(cond1_array, cond2_array).if_else(sint(1), M[j][i])

# @for_range(nums)
# def _(i):
#     @for_range(nums)
#     def _(j):
#         print_ln("%s", M[i][j].reveal())

@for_range(nums)
def _(i):
    isDominant[0] = sint(1)
    @for_range(nums)
    def _(j):
        isDominant[0] = (hit[j] == 1).if_else((k_dom[i]==sint(1)).if_else(sint(0), isDominant[0]), isDominant[0])
        hit[j] = (hit[j] == 1).if_else((k_dom[j] == sint(1)).if_else(sint(0), hit[j]), hit[j])
    hit[i] = (isDominant[0] == sint(1)).if_else(sint(1), hit[i])

@for_range(nums)
def _(i):
    @for_range(nums)
    def _(j):
        hit[j] = (i != j).if_else((hit[j] == sint(1)).if_else((M[i][j] == sint(1)).if_else(sint(0), hit[j]), hit[j]), hit[j])         
        
            
@for_range(nums)
def _(i):
    @if_(hit[i].reveal() > 0)
    def _():
        print_ln("@%s", i)
prog.finalize()