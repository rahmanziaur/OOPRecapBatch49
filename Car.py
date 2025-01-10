from Engine import Engine

class Car:
    def __init__(self, model):
        self.model = model
        self.engine = Engine()  # Composition: Car owns Engine

    def start_car(self):
        return f"{self.engine.start()} in the {self.model} car."

    def stop_car(self):
        return f"{self.engine.stop()} in the {self.model} car."
