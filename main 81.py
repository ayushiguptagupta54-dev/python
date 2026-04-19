#  Example of hybrid inheritence
class BaseClass:
    pass

class Derived(BaseClass):
    pass
class Derived2(BaseClass):
    pass
class Derived3(Derived, Derived2):
    pass

#  Hierarchical inheritance
class D1(BaseClass):
    pass
class D2(BaseClass):
    pass
class D3(D1):
    pass