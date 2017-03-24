class Cart:

    def __init__(self):
        self._contents = dict()

    def process(self, u_order):
        if u_order.add:
            if u_order.item not in self._contents:
                self._contents[u_order.item] = 0
            self._contents[u_order.item] += 1
        elif u_order.delete:
            self._contents[u_order.item] -= 1
            if self._contents[u_order.item] <= 0:
                del self._contents[u_order.item]


class Order:

    def __init__(self):
        self.quit = False
        self.add = False
        self.delete = False
        self.item = None

    def get_input(self):
        print("[command] [item] (command is a to add, d to delete, q to quit)")
        line = input()
        command = line[:1]
        self.item = line[2:]
        if command == "q":
            self.quit = True
        elif command == "a":
            self.add = True
        elif command == "d":
            self.delete = True

cart = Cart()
order = Order()
order.get_input()

while not order.quit:
    cart.process(order)
    order = Order()
    order.get_input()

