from analysis.entropy import EntropyAnalyzer
from analysis.classification import DeviceClassifier


class BehaviorAnalyzer:
    def __init__(self, window_size=5):
        self.window_size = window_size
        self.samples = []
        self.classifier = DeviceClassifier()

    def add_sample(self, registers):
        """
        Add a register snapshot.
        Returns analysis result only when window is full.
        Otherwise returns None.
        """
        self.samples.append(registers)

        # Not enough data yet
        if len(self.samples) < self.window_size:
            return None

        result = self._analyze_window()

        # Reset window (fixed window mode)
        self.samples = []

        return result

    def _analyze_window(self):
        # **Indented the body of _analyze_window**
        # Flatten values for entropy calculation
        all_values = [] 
        for sample in self.samples:
            all_values.extend(sample)

        # Entropy
        entropy = EntropyAnalyzer(all_values).calculate()

        # Behavior metric
        change_rate = self._calculate_change_rate()

        behavior_result = {
            "change_rate": change_rate
        }

        # Classification
        classification_result = self.classifier.classify(
            entropy,
            behavior_result
        )

        return {
            "classification": classification_result["classification"],
            "confidence": classification_result["confidence"],
            "entropy": entropy,
            "change_rate": change_rate
        }

    def _calculate_change_rate(self):
        changes = 0
        total = 0

        for i in range(1, len(self.samples)):
            prev = self.samples[i - 1]
            curr = self.samples[i]

            for a, b in zip(prev, curr):
                total += 1
                if a != b:
                    changes += 1

        if total == 0:
            return 0.0

        return changes / total