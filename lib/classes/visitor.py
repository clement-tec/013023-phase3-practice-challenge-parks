class Visitor:
    def __init__(self,name):
        if type(name) is str:
            if len(name) <= 15 and len(name) > 0:
                self._name = name

    def get_name(self):
        return self._name
    def set_name(self,newname):
        print("Can't change")
    
    name = property(get_name,set_name)

   