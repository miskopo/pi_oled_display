from sh import ls, ErrorReturnCode_2
from logger import logger


class TemperatureController:
    __slots__ = '_temperature'

    def __init__(self):
        self._temperature = 0.0

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        if value < -273.15:
            raise AttributeError("Temperature readout can't be below Absolute Zero")
        self._temperature = value

    def read_temperature(self):
        try:
            wire_devices = ls("/sys/bus/w1/devices")

        except ErrorReturnCode_2:
            logger.error("Path for wire devices doesn't exist")
            return "Enable to read temperature"
        self.temperature = 12
        return self.temperature
