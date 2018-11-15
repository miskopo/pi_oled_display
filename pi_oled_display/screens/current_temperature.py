from pi_oled_display.controllers.temperature_controller import TemperatureController


class CurrentTemperature:
    __slots__ = 'temp_ctl'

    def __init__(self):
        self.temp_ctl = TemperatureController()

    def __str__(self):
        """
        Render text for screen, e.g.
        (THERMOMETER SYMBOL) 12℃
        :return: String (THERMOMETER SYMBOL) TEMPERATURE℃
        """
        thermometer = u"\U0001F321"
        temperature = self.temp_ctl.read_temperature()
        return "{symbol}{value}u\u2103".format(symbol=thermometer, value=temperature)
