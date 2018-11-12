from pi_oled_display import display


class ScreenCleaner:

    @staticmethod
    def clear():
        display.begin()
        display.clear()
        display.display()
