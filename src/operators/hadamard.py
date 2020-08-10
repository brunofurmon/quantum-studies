from numpy import array, tensordot, sqrt


def H(input):
    ''' Hadamard operation on 1 qbit\n
    @input qbit must be in row form, like [[0],[1]]\n
    returns the superposition state of @input qbit
    '''
    hadamardMatrix = (1 / sqrt(2)) * array([[1, 1],
                                            [1, -1]])

    return tensordot(hadamardMatrix, input, (1, 0))
