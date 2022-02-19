from typing import List
from scale_input.ChoosePrimeStrategy import ChoosePrimeStrategy


class ScaleInput:
    def listen(self, choose_prime_strategy: ChoosePrimeStrategy) -> List[int]:
        pass


class MIDIKeyboardInput(ScaleInput):
    def listen(self, choose_prime_strategy: ChoosePrimeStrategy) -> List[int]:
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

    def __str__(self):
        return "MIDI Keyboard"
