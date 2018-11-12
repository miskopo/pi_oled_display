from pi_oled_display.controllers.temperature_controller import TemperatureController


class CurrentTemperature:
    __slots__ = 'temp_ctl'

    def __init__(self):
        self.temp_ctl = TemperatureController()

    def __str__(self):
        thermometer = u"\U0001F321"
        temperature = self.temp_ctl.read_temperature()
        return "{symbol}{value}".format(symbol=thermometer, value=temperature)
