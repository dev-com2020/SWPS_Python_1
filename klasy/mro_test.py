class AAA:
    def speak(self):
        print("AAA")


class BBB(AAA):
    def speak(self):
        print("BBB")
        super().speak()


class CCC(AAA):
    def speak(self):
        print("CCC")
        super().speak()


class DDD(CCC, BBB):
    def speak(self):
        BBB.speak(self)


d = DDD()
d.speak()

print(DDD.__mro__)
