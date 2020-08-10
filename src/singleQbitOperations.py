import time
from numpy import array
from operators.hadamard import H


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
    print('Started in {}'.format(time.time()))

    superposition()

    print('Finished in {}'.format(time.time() - timeStart))

# Superposition
def superposition():
    print('phi = |0> {}'.format(zero))
    print('H(phi) = {}'.format(H(zero)))

    print('phi = |1> {}'.format(one))
    print('H(phi) = {}'.format(H(one)))

    print('H is reversible so...')
    print('phi = H(|0>) {}'.format(zero))
    print('H(H(phi)) = {}'.format(H(H(zero))))

    print('phi = H(|1>) {}'.format(one))
    print('H(H(phi)) = {}'.format(H(H(one))))


if __name__ == '__main__':
    main()
