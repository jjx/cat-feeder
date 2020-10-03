from __future__ import absolute_import

from app.main.lib import run_shell_command


class LegacyGpio(object):

    GPIO = '/usr/local/bin/gpio'
    ZERO = '0'
    ONE = '1'
    OUT_MODE = 'out'
    IN_MODE = 'in'

    GPIO_MODE_ARGS = [GPIO, 'mode']
    GPIO_WRITE_ARGS = [GPIO, 'write']
    GPIO_READ_ARGS = [GPIO, 'read']

    @staticmethod
    def set_out(pin):
        pin = str(pin)
        run_shell_command(LegacyGpio.GPIO_MODE_ARGS +
                          [pin, LegacyGpio.OUT_MODE])

    @staticmethod
    def set_in(pin):
        pin = str(pin)
        run_shell_command(LegacyGpio.GPIO_MODE_ARGS +
                          [pin, LegacyGpio.IN_MODE])

    @staticmethod
    def write_0(pin):
        pin = str(pin)
        return run_shell_command(
            LegacyGpio.GPIO_WRITE_ARGS + [pin, LegacyGpio.ZERO])

    @staticmethod
    def write_1(pin):
        pin = str(pin)
        return run_shell_command(
            LegacyGpio.GPIO_WRITE_ARGS + [pin, LegacyGpio.ONE])

    @staticmethod
    def read(pin):
        pin = str(pin)
        return run_shell_command(LegacyGpio.GPIO_READ_ARGS + [pin])
