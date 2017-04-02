from GUIconnection import GUIconnection
from Pt import Pt

class nthPoint(GUIconnection):

    def displayName(self):
        return "nthPoint"

    def displayParameterName(self):
        return "n ="

    def thinPoints(self, pts, param):
        new_pts = []
        for i in range(len(pts)):
            if i % param == 0:
                new_pts.append(pts[i])
        return new_pts
