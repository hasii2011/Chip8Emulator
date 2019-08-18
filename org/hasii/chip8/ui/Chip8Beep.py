
from array import array

from pygame.mixer import Sound
from pygame.mixer import get_init


class Chip8Beep(Sound):
    """
    From https://gist.github.com/nekozing/5774628
    """
    def __init__(self, frequency, volume=.1):
        self.frequency = frequency
        super().__init__(self.build_samples())
        # Sound.init(self, buffer=self.build_samples())
        self.set_volume(volume)

    def build_samples(self):
        period = int(round(get_init()[0] / self.frequency))
        samples = array("h", [0] * period)
        amplitude = 2 ** (abs(get_init()[1]) - 1) - 1
        for time in range(period):
            if time < period / 2:
                samples[time] = amplitude
            else:
                samples[time] = -amplitude
        return samples
