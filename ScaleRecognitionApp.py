from art import tprint
from consolemenu import *
from consolemenu.items import *
from estimator import Estimator
import tabulate
from scale_input import *

input_strategy: ScaleInput = None
choose_prime_strategy: ChoosePrimeStrategy = None


def estimate():
    assert input_strategy is not None
    assert choose_prime_strategy is not None
    pitches = input_strategy.listen(choose_prime_strategy)
    estimator = Estimator()
    most_accurate_scales = estimator.most_accurate_scales(pitches)
    scales = [list(item) for item in list(most_accurate_scales.items())[:10]]
    scales.insert(0, ["name", "diff"])
    print("Top 10 most accurate scales")
    print(tabulate.tabulate(scales))


def choose_keyboard_midi():
    global input_strategy
    input_strategy = MIDIKeyboardInput()
    print(f"Set input strategy: {input_strategy}")


def prime_last():
    global choose_prime_strategy
    choose_prime_strategy = LastStrategy()
    print(f"Set choose prime strategy: {choose_prime_strategy}")


def prime_first():
    global choose_prime_strategy
    choose_prime_strategy = FirstStrategy()
    print(f"Set choose prime strategy: {choose_prime_strategy}")


def prime_lowest():
    global choose_prime_strategy
    choose_prime_strategy = LowestStrategy()
    print(f"Set choose prime strategy: {choose_prime_strategy}")


def subtitle():
    return f"Choose prime strategy: {choose_prime_strategy}\nInput strategy: {input_strategy}"


def main():
    tprint('Scale Recognition')

    menu = ConsoleMenu("Main Menu", subtitle)

    estimate_item = FunctionItem("Estimate", estimate)

    choose_keyboard_midi_item = FunctionItem("Keyboard MIDI", choose_keyboard_midi)
    input_strategy_menu = ConsoleMenu("Input Strategy")
    input_strategy_menu.append_item(choose_keyboard_midi_item)
    submenu_input_strategy = SubmenuItem("Input Strategy", input_strategy_menu, menu)

    choose_prime_strategy_menu = ConsoleMenu("Choosing Prime Strategy")
    first_item = FunctionItem("First", prime_first)
    last_item = FunctionItem("Last", prime_last)
    lowest_item = FunctionItem("Lowest", prime_lowest)
    choose_prime_strategy_menu.append_item(first_item)
    choose_prime_strategy_menu.append_item(last_item)
    choose_prime_strategy_menu.append_item(lowest_item)
    submenu_choose_prime = SubmenuItem("Choosing Prime Strategy", choose_prime_strategy_menu, menu)

    menu.append_item(estimate_item)
    menu.append_item(submenu_input_strategy)
    menu.append_item(submenu_choose_prime)

    menu.show()


if __name__ == "__main__":
    main()
