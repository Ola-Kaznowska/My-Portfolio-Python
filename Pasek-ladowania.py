import time

# #
# -

def pasek_ladowania(gotowe, wszystko = 100):
    """
    ###-------

    #####-----
    """

    wykonane = round( 10 * (gotowe/wszystko) )
    niewykonane = 10 - wykonane

    wykonane = '#' * wykonane
    niewykonane = '-' * niewykonane

    print(f'\r[{wykonane}{niewykonane}]', end = " ")
    return wykonane
    pass

for i in range(100):
    wwwww = pasek_ladowania(i, wszystko=100)
    time.sleep(0.1)
    pass
    