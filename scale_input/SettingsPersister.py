import json
from scale_input import *

_scale_input = "scale_input"
_prime_strategy = "choose_prime_strategy"
_settings_file_name = "settings.json"


def get_choose_prime_strategy_from_str(s):
    lowest_strategy = LowestStrategy()
    first_strategy = FirstStrategy()
    last_strategy = LastStrategy()
    explicit_strategy = ExplicitStrategy()
    if s == str(lowest_strategy):
        return lowest_strategy
    elif s == str(first_strategy):
        return first_strategy
    elif s == str(last_strategy):
        return last_strategy
    elif s == str(explicit_strategy):
        return explicit_strategy
    else:
        raise Exception(f"Unknown choose prime strategy: {s}")


def get_scale_input_from_str(s):
    midi = MIDIKeyboardInput()
    name = NameKeyboardInput()
    if s == str(midi):
        return midi
    elif s == str(name):
        return name
    else:
        raise Exception(f"Unknown  scale input strategy: {s}")


class ScaleRecognitionSettings:
    def __init__(self, scale_input: ScaleInput, choose_prime_strategy: ChoosePrimeStrategy):
        self.scale_input = scale_input
        self.choose_prime_strategy = choose_prime_strategy

    def persist(self):
        j = json.JSONEncoder().encode(o={
            _scale_input: str(self.scale_input),
            _prime_strategy: str(self.choose_prime_strategy)
        })
        with open(_settings_file_name, "w") as f:
            f.write(j)


def get_settings() -> ScaleRecognitionSettings:
    with open(_settings_file_name, "r") as f:
        s = json.JSONDecoder().decode(f.readline())
        return ScaleRecognitionSettings(get_scale_input_from_str(s[_scale_input]), get_choose_prime_strategy_from_str(s[_prime_strategy]))
