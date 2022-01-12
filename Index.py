class computer:
    def __init__(self, processor,ram):
        self.processor = processor
        self.ram = ram
    def parts(self):
        print(f"This computer has {self.processor} processor and {self.ram}gb ram")
lenovo = computer('intel', 16)
dell = computer('amd', 8)

lenovo.parts()
dell.parts()