from requests import get


class CurrentWeather:
    __slots__ = 'url', 'city'

    def __init__(self, city=None):
        self.url = "http://wttr.in/"
        self.city = city

    def obtain_weather(self) -> str:
        """

        :return:
        """
        try:
            with get("{}{}".format(self.url, self.city if not None else "")) as response:
                if response.ok:
                    return "\n".join(response.text.split("\n")[1:7])
                else:
                    raise ConnectionError
        except ConnectionError:
            # Unable to connect
            return "Unable to connect"
