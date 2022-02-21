from art import tprint
from consolemenu import *
from consolemenu.items import *
from estimator import Estimator
import tabulate
from scale_input import *
from typing import Optional

_settings = get_settings()

input_strategy: ScaleInput = _settings.scale_input
choose_prime_strategy: ChoosePrimeStrategy = _settings.choose_prime_strategy


def estimate():
    pitches = input_strategy.listen(choose_prime_strategy)
    estimator = Estimator()
    most_accurate_scales = estimator.most_accurate_scales(pitches)
    scales = [list(item) for item in list(most_accurate_scales.items())[:10]]
    scales.insert(0, ["name", "diff"])
    print("Top 10 most accurate scales")
    print(tabulate.tabulate(scales))


def change_settings(si: Optional[ScaleInput] = None, cps: Optional[ChoosePrimeStrategy] = None):
    global input_strategy, choose_prime_strategy
    if si is not None:
        input_strategy = si
        print(f"Set input strategy: {input_strategy}")
    if cps is not None:
        choose_prime_strategy = cps
        print(f"Set choose prime strategy: {choose_prime_strategy}")
    ScaleRecognitionSettings(input_strategy, choose_prime_strategy).persist()


def choose_keyboard_midi():
    change_settings(si=MIDIKeyboardInput())


def choose_keyboard_name():
    change_settings(si=NameKeyboardInput())


def prime_last():
    change_settings(cps=LastStrategy())


def prime_first():
    change_settings(cps=FirstStrategy())


def prime_lowest():
    change_settings(cps=LowestStrategy())


def prime_explicit():
    change_settings(cps=ExplicitStrategy())


def subtitle():
    return f"Choose prime strategy: {choose_prime_strategy}\nInput strategy: {input_strategy}"


def main():
    tprint('Scale Recognition')

    menu = ConsoleMenu("Main Menu", subtitle)

    estimate_item = FunctionItem("Estimate", estimate)

    choose_keyboard_midi_item = FunctionItem("Keyboard MIDI", choose_keyboard_midi)
    choose_keyboard_name_item = FunctionItem("Keyboard Name", choose_keyboard_name)
    input_strategy_menu = ConsoleMenu("Input Strategy")
    input_strategy_menu.append_item(choose_keyboard_midi_item)
    input_strategy_menu.append_item(choose_keyboard_name_item)
    submenu_input_strategy = SubmenuItem("Input Strategy", input_strategy_menu, menu)

    choose_prime_strategy_menu = ConsoleMenu("Choosing Prime Strategy")
    first_item = FunctionItem("First", prime_first)
    last_item = FunctionItem("Last", prime_last)
    lowest_item = FunctionItem("Lowest", prime_lowest)
    explicit_item = FunctionItem("Explicit", prime_explicit)
    choose_prime_strategy_menu.append_item(first_item)
    choose_prime_strategy_menu.append_item(last_item)
    choose_prime_strategy_menu.append_item(lowest_item)
    choose_prime_strategy_menu.append_item(explicit_item)
    submenu_choose_prime = SubmenuItem("Choosing Prime Strategy", choose_prime_strategy_menu, menu)

    menu.append_item(estimate_item)
    menu.append_item(submenu_input_strategy)
    menu.append_item(submenu_choose_prime)

    menu.show()


if __name__ == "__main__":
    main()
