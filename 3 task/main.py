class TSStack:
    items = []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Empty stack")
        return self.items.pop(0)


# Псевдодебаг
test = TSStack()
test.push(5)
test.push(10)
print(test.pop())
print(test.pop())
print(test.pop())