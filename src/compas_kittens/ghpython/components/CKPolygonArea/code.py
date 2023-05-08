from compas_kittens.algorithms import polygon_area
from ghpythonlib.componentbase import executingcomponent as component


class CKPolygonArea(component):
    def RunScript(self, polygon):
        return polygon_area(polygon)
