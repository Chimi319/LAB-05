class CustomerQueue:
    def __init__(self):
        self.queue = []

    def add_customer(self, name):
        self.queue.append(name)

    def serve_customer(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return "No customers to serve"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


# Testing the customer service system
cq = CustomerQueue()

# Adding customers
cq.add_customer("Sonam")
cq.add_customer("Pema")
cq.add_customer("Karma")

print("Customers waiting:")
cq.display()

# Serving one customer
served = cq.serve_customer()
print("Serving customer:", served)

print("Remaining queue:")
cq.display()