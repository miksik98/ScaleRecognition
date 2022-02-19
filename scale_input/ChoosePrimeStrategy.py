class ChoosePrimeStrategy:
    def apply(self, pitches) -> int:
        pass


class LowestStrategy(ChoosePrimeStrategy):
    def apply(self, pitches) -> int:
        return min(pitches)

    def __str__(self):
        return "Lowest"


class FirstStrategy(ChoosePrimeStrategy):
    def apply(self, pitches) -> int:
        return pitches[0]

    def __str__(self):
        return "First"


class LastStrategy(ChoosePrimeStrategy):
    def apply(self, pitches) -> int:
        return pitches[-1]

    def __str__(self):
        return "Last"
