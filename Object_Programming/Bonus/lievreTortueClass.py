class LievreTortue:
    def __init__(self,aller_vers):
        self._aller_vers=aller_vers
    def aller_vers(self,x, y):
        return self.turtle.towards(x, y)
