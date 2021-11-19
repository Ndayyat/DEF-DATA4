class Dog:


    energy = "high"


    def speak(self):
        print("noor")


havoc = Dog()

havoc.speak()
print(havoc.energy)

clifford = Dog()

clifford.speak()
clifford.energy = "large"
print(clifford.energy)


