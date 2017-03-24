class Cart:

    def __init__(self):
        self._contents = dict()

    def __repr__(self):
        return "{0} {1}".format(Cart, self.__dict__)

    def process(self, u_order):
        if u_order.add:
            if u_order.item not in self._contents:
                self._contents[u_order.item] = 0
            self._contents[u_order.item] += 1
        elif u_order.delete:
            self._contents[u_order.item] -= 1
            if self._contents[u_order.item] <= 0:
                del self._contents[u_order.item]


