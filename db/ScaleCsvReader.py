import csv
from model import Scale
import functools

class ScaleCsvException(Exception):
    pass


class ScaleCsvReader:
    def __init__(self):
        self.problems = []

    def read(self):
        scales = []
        names = []
        with open('scales.csv') as f:
            csvreader = csv.reader(f)
            next(csvreader)  # skip header
            for row in csvreader:
                assert len(row) == 2
                name = row[0]
                pitches = row[1].split()
                contains_ints = True
                for pitch in pitches:
                    if not pitch.isnumeric():
                        self.problems.append(f"\tScale \'{name}\' contains invalid steps")
                        contains_ints = False
                        break
                if contains_ints:
                    pitches = list(map(lambda x: int(x), pitches))
                    if min(pitches) != 0:
                        self.problems.append(f"\tScale \'{name}\' not starting with 0")
                    if max(pitches) > 11:
                        self.problems.append(f"\tScale \'{name}\' contains value greater than 11")
                    if len(set(pitches)) != len(pitches):
                        self.problems.append(f"\tScale \'{name}\' contains duplicates in steps")
                    if sorted(pitches) != pitches:
                        self.problems.append(f"\tScale \'{name}\' contains not sorted steps")
                    scales.append(Scale(name, pitches))
                names.append(name)

        duplications = []
        for i in range(len(names)):
            current_name = names[i]
            if current_name not in duplications:
                for j in range(i+1, len(names)):
                    if names[j] == current_name:
                        duplications.append(current_name)
                        break
        if len(duplications) > 0:
            self.problems.append(f"\tThere are duplicated scales by name: {duplications}")
        if len(self.problems) > 0:
            raise ScaleCsvException("\n" + functools.reduce(lambda a, b: a + "\n" + b, self.problems))
        return scales
