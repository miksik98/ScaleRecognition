from typing import List
from scale_input.ChoosePrimeStrategy import ChoosePrimeStrategy, ExplicitStrategy
from music21.note import Note
from pygame.midi import *
import time


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


class NameKeyboardInput(ScaleInput):
    def listen_for_scale(self, choose_prime_strategy: ChoosePrimeStrategy) -> List[int]:
        print("Type names, then press ENTER.")
        midis = []
        while True:
            name = input()
            if name == '':
                break
            midi = Note(name).pitch.midi
            midis.append(midi)
        if len(midis) > 0:
            prime = choose_prime_strategy.apply(midis)
            midis = [(m + 120 - prime) % 12 for m in midis]
            midis = list(sorted(set(midis)))
        return midis

    def listen_for_prime(self) -> int:
        return Note(input()).pitch.midi

    def __str__(self):
        return "Name Keyboard"


init()
_id = get_default_input_id()
_input = Input(_id)


class MIDIDeviceInput(ScaleInput):
    def __init__(self):
        self.id = _id
        self.input = _input

    def read(self):
        return midis2events(self.input.read(100), self.id)

    def listen_for_scale(self, choose_prime_strategy: ChoosePrimeStrategy) -> List[int]:
        print("Play notes on MIDI device, then press ENTER.")
        input()
        events = self.read()
        if len(events) == 0:
            return []
        midis = []
        for event in events:
            if event.status == 144:
                midis.append(event.data1)
        if len(midis) > 0:
            prime = choose_prime_strategy.apply(midis)
            midis = [(m + 120 - prime) % 12 for m in midis]
            midis = list(sorted(set(midis)))
        print(midis)
        return midis

    def listen_for_prime(self) -> int:
        while not Input.poll(self.input):
            time.sleep(.01)
        events = self.read()
        if len(events) == 0:
            return -1
        return events[0].data1

    def __str__(self):
        return "MIDI Device"
