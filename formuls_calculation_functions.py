from math import log10, sqrt, log


class IntervalCalculation():

    def __init__(self, sorted_data):
        self.min_value = None
        self.max_value = None
        self.sorted_data = sorted_data

    @staticmethod
    def _find_divisors(n):
        i = 2
        divisors = []

        while i ** 2 <= n:
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
            i += 1
        divisors.sort()

        return divisors

    def interval_calculation(self):
        self.min_value = self.sorted_data[0]
        self.max_value = self.sorted_data[-1]
        count_elements = len(self.sorted_data)
        scope_of_interval = self.max_value - self.min_value
        test_size_of_interval = int(scope_of_interval / (1 + 3.28 * log(count_elements)))
        real_size_of_interval = self._interval_step_refactor(test_size_of_interval, scope_of_interval)
        return real_size_of_interval, scope_of_interval//real_size_of_interval

    def _check_step(self, size_of_interval):
        current_value = self.min_value
        count_of_steps = 0
        max_element = self.max_value
        while current_value < max_element:
            current_value += size_of_interval
            count_of_steps += 1
            if count_of_steps > 15:
                return False
        return current_value == max_element  # Если шаг равен то возвращает true

    def _interval_step_refactor(self, size_of_interval, scope_of_interval):
        correct_size_interval = size_of_interval

        if self._check_step(correct_size_interval + 1):
            return correct_size_interval + 1

        if self._check_step(correct_size_interval - 1):
            return correct_size_interval - 1

        if not self._check_step(correct_size_interval):
            divisors = self._find_divisors(scope_of_interval)
            for i in divisors:
                correct_size_interval = i
                if self._check_step(correct_size_interval):
                    break

        return correct_size_interval
