# --- COMPOSITION ---
# Composition means one object owns another object. Here, a Car 'is composed of' an Engine.
class Engine:
    def start(self):
        return "Engine starts"

    def stop(self):
        return "Engine stops"