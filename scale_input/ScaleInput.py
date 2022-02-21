from typing import List
from scale_input.ChoosePrimeStrategy import ChoosePrimeStrategy, ExplicitStrategy


class ScaleInput:
    def listen(self, choose_prime_strategy: ChoosePrimeStrategy) -> List[int]:
        if isinstance(choose_prime_strategy, ExplicitStrategy):
            print("Provide prime explicitly:\n")
            choose_prime_strategy.set_prime(self.listen_for_prime())
        return self.listen_for_scale(choose_prime_strategy)

    def listen_for_scale(self, choose_prime_strategy) -> List[int]:
        pass

    def listen_for_prime(self) -> int:
        pass


class MIDIKeyboardInput(ScaleInput):
    def listen_for_scale(self, choose_prime_strategy: ChoosePrimeStrategy) -> List[int]:
        print("Type midi values, then press ENTER.")
        midis = []
        while True:
            i = input()
            if i == '':
                break
            midi = int(i)
            midis.append(midi)
        if len(midis) > 0:
            prime = choose_prime_strategy.apply(midis)
            midis = [(m + 120 - prime) % 12 for m in midis]
            midis = list(sorted(set(midis)))
        return midis

    def listen_for_prime(self) -> int:
        return int(input())

    def __str__(self):
        return "MIDI Keyboard"
