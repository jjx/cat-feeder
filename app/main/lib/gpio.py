from __future__ import absolute_import

from app.main.lib import is_mac
from app.main.lib.legacy_gpio import LegacyGpio

try:
    use_legacy = False
    import RPi.GPIO as GPIO
except ImportError:
    use_legacy = True


class Gpio(object):

    @staticmethod
    def set_out(pin):
        if is_mac():
            return 0

        pin = int(pin)
        if use_legacy:
            LegacyGpio.set_out(pin)
        else:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(pin, GPIO.OUT)

    @staticmethod
    def set_in(pin, pull_up=None):
        if is_mac():
            return 0

        pin = int(pin)
        if use_legacy:
            LegacyGpio.set_in(pin)
        else:
            GPIO.setmode(GPIO.BCM)
            if pull_up is not None:
                GPIO.setup(pin, GPIO.IN,
                           pull_up_down=GPIO.PUD_UP if pull_up else GPIO.PUD_DOWN)
            else:
                GPIO.setup(pin, GPIO.IN)

    @staticmethod
    def write_0(pin):
        if is_mac():
            return 0

        pin = int(pin)
        if use_legacy:
            return LegacyGpio.write_0(pin)
        else:
            return GPIO.output(pin, False)

    @staticmethod
    def write_1(pin):
        if is_mac():
            return 0

        pin = int(pin)
        if use_legacy:
            return LegacyGpio.write_1(pin)
        else:
            return GPIO.output(pin, True)

    @staticmethod
    def read(pin):
        pin = int(pin)
        if use_legacy:
            return LegacyGpio.read(pin)
        else:
            return GPIO.input(pin)
