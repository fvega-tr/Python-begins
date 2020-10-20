def letra_duplicada(txt):
    '''
    Hola me llamo Ambrosio
    >>> letra_duplicada("mellamo")
    True
    '''
    return any(l1==l2 for l1,l2 in zip(txt, txt[1:]))

import doctest
doctest.testmod()

#print(letra_duplicada.__doc__)