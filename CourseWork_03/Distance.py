from GUIconnection import GUIconnection
from Pt import Pt

class Distance(GUIconnection):

    def displayName(self):
        return "Distance"

    def displayParameterName(self):
        return "min distance"

    def thinPoints(self, pts, param):
        new_pts = []
        last_kept = pts[0]
        new_pts.append(last_kept)
        for i in range(1, len(pts)):
            current = pts[i]
            if current.EuclideanDistance(last_kept) >= param:
                last_kept = current
                new_pts.append(last_kept)
        return new_pts
