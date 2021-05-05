class Signal:
    def __init__(self):
        self.slots = []

    def __radd__(self, other):
        self.slots.append(other)

    def attach(self, callback):
        self.slots.append(callback)

    def emit(self, *args, **kwargs):
        for s in self.slots:
            s(*args, **kwargs)

