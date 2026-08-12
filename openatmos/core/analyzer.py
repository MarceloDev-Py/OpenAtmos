import providers.metnorway as metnorway, providers.openmeteo as openmeteo, json

class Analyze:

    def __init__(self):

        self.norway = metnorway.norwayprovider()
        self.openmet = openmeteo.openmprovider()
        print(self.norway)
        print("\n" ** 2)
        print(self.openmet)

obj = Analyze()