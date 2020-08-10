from numpy import array, tensordot


def X(input):
    ''' Bit flip operation on 1 qbit\n
    @input qbit must be in row form, like [[0],[1]]\n
    returns the inverse state of @input qbit
    '''
    bitFlipMatrix = array([[0, 1],
                            [1, 0]])

    return tensordot(bitFlipMatrix, input, (1, 0))
