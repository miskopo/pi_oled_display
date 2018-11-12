from setuptools import setup

setup(
    name='pi_oled_display',
    version='0.0.1',
    packages=['pi_oled_display'],
    entry_points={
        'console_scripts': [
            'pi_oled_display = pi_oled_display.__main__:main'
         ]
    })
