class Package:
    def __init__(self, size, number, header=24):
        self.number = number
        self.size = size
        self.header = header

    def __repr__(self):
        return f"Package(number={self.number} size={self.size} header={self.header})"

