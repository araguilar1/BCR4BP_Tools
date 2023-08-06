import asset_asrl as ast
import asset_asrl.Astro.Constants as c
from asset_asrl.OptimalControl import ODEBase

from BCR4BPFrame import BCR4BPFrame

vf = ast.VectorFunctions
oc = ast.OptimalControl

class BCR4BP(ODEBase, BCR4BPFrame):
    def __init__(self, P1mu, P2mu, P3mu, lstartEM, lstarSB1, theta0, eta):
        BCR4BPFrame.__init__(self, P1mu, P2mu, P3mu, lstartEM, lstarSB1, theta0, eta)

        args = oc.ODEArguments(7,0)

        r, v, theta = args.XVec().tolist([(0,3),(3,3),(6,1)])

        ode = self.BCR4BPEOMS(r, v, theta, eta=eta, otherAccs=[])

        ODEBase.__init__(self, ode, 7)

class BCR4BPSB1(ODEBase, BCR4BPFrame):
    def __init__(self, P1mu, P2mu, P3mu, lstartEM, lstarSB1, theta0):
        BCR4BPFrame.__init__(self, P1mu, P2mu, P3mu, lstartEM, lstarSB1, theta0)

        args = oc.ODEArguments(7,0)

        r, v, theta = args.XVec().tolist([(0,3),(3,3),(6,1)])

        ode = self.BCR4BPSB1EOMS(r, v, theta, otherAccs=[])

        ODEBase.__init__(self, ode, 7)