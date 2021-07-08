# Hanoi Tower
# There are three pegs which can hold stacks of disks of different diameters. One of them will be the initial position
# of the stack (starting peg = peg_str = A), other will be the target position of the stack
# (target peg = peg_trg = peg_C), and the last one will be the auxiliar peg (peg_aux = peg_B) used to move the elements
# between pegs A and C.

# Ask of initial number of elements in the Hanoi Tower.
num_elem = int(input("Enter the number of elements of the Hanoi Tower. "))
# n = 3
# Initial statement
A = []
B = []
C = []
for i in range(1, num_elem+1):
    A.append(i)
A.reverse()
print(A, B, C)


# For num_elem=3 element:
def hanoi_3():
    C.append(A.pop(-1))
    print(A, B, C)
    B.append(A.pop(-1))
    print(A, B, C)
    B.append(C.pop(-1))
    print(A, B, C)

    C.append(A.pop(-1))
    print(A, B, C)

    A.append(B.pop(-1))
    print(A, B, C)
    C.append(B.pop(-1))
    print(A, B, C)
    C.append(A.pop(-1))
    print(A, B, C)


# Moving elements function:
def move_element(n, peg_str, peg_trg, peg_aux):
    if n == 1:
        peg_trg.append(peg_str.pop(-1))
        print(peg_str, peg_aux, peg_trg)
        return
    move_element(n-1, peg_str, peg_aux, peg_trg)

    peg_trg.append(peg_str.pop(-1))
    print(peg_str, peg_aux, peg_trg)

    move_element(n-1, peg_aux, peg_trg, peg_str)


# Driver code:

move_element(num_elem, A, C, B)
