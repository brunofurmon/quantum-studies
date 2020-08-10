import time
from numpy import array
from operators.hadamard import H
from operators.bitFlip import X


zero = array([
    [1],
    [0]
])
one = array([
    [0],
    [1]
])

def main():
    timeStart = time.time()
    print('Started at {}'.format(timeStart))

    superpositionExamples()
    bitFlipExamples()

    print('Finished in {}'.format(time.time() - timeStart))

# Superposition
def superpositionExamples():
    print('=== Hadamard Operation on 1 qubit ===\n')
    
    print('\nphi = |0>\n')
    print(zero)
    print('\nH(phi)\n')
    print(H(zero))

    print('\n-----\n')

    print('\nphi = |1>\n')
    print(one)
    print('\nH(phi)\n')
    print(H(one))

    print('\n-----\n')

    print('\nH is reversible so...\n')

    print('\nphi = H(|0>)\n')
    print(H(zero))
    print('\nH(H(phi))\n')
    print(H(H(zero)))

    print('\nphi = H(|1>)\n')
    print(H(one))
    print('\nH(H(phi))\n')
    print(H(H(one)))

def bitFlipExamples():
    print('=== Bit flip Operation on 1 qubit ===')

    print('\nphi = |0>\n')
    print(zero)
    print('\nX(phi)\n')
    print(X(zero))

    print('\n-----\n')

    print('\nphi = |1>\n')
    print(one)
    print('\nX(phi)\n')
    print(X(one))

    print('\n-----\n')

    print('\nX is reversible so...\n')

    print('\nphi = X(|0>)\n')
    print(X(zero))
    print('\nX(X(phi))\n')
    print(X(X(zero)))

    print('\nphi = X(|1>)\n')
    print(X(one))
    print('\nX(X(phi))\n')
    print(X(X(one)))

if __name__ == '__main__':
    main()
