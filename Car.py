from Engine import Engine

class Car:
    engine = Engine()  # Composition: Car owns Engine
    def __init__(self, model):
        self.model = model

    def start_car(self):
        return f"{self.engine.start()} in the {self.model} car."

    def stop_car(self):
        return f"{self.engine.stop()} in the {self.model} car."
