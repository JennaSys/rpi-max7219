from setuptools import setup

setup(
    name='rpi-max7219',
    version='0.1.0',
    description='Raspberry Pi driver for MAX7219 with 7-segment modules.',
    long_description=open('README').read(),
    url='https://github.com/JennaSys/rpi-max7219',
    author='John Sheehan',
    author_email='jennasyseng@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Hardware',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='RPi MAX7219 SPI interface',
    py_modules=['max7219', 'seven_segment_ascii'],
    install_requires=['spidev'],
)
