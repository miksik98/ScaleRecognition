from db.ScaleCsvReader import ScaleCsvReader
from utils import levenshtein

class Estimator:
    def __init__(self):
        self.scales = {scale.name: scale for scale in ScaleCsvReader().read()}

    def most_accurate_scales(self, pitches):
        scales_scores = {scale.name: levenshtein(scale.steps[1:], pitches[1:]) for scale in self.scales.values()}
        scales_scores = {k: v for k, v in sorted(scales_scores.items(), key=lambda item: item[1])}
        return scales_scores

scales = Estimator().most_accurate_scales([0, 2, 3, 5, 6, 8, 10])
print(scales)