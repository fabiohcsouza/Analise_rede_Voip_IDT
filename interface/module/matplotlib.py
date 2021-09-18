import os
import re
import numpy as np
import matplotlib.pyplot as mpl

def controle(valor1):
    qnt_ping = 10
    fs = np.linspace(1,qnt_ping,qnt_ping)

    aping = np.array(valor1,np.float)
    ping1 = np.array(qnt_ping)
    mpl.plot(fs,aping,"o-")

    mpl.legend(ping)
    mpl.show()

controle()