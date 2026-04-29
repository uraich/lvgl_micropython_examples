# hw_esp32_s3_fh4r2.py: defines all the hardware connections of the
# esp32-s3_fh4r2 CPU
# Copyright (c) U. Raich, Feb. 2024
# This file is part of the course on TinyML at the
# University of Cape Coast, Ghana
# It is released under the MIT license

from micropython import const

# neopixel
NEOPIXEL          = const(42)
NO_OF_NEOPIXELS   = const(1)
INTENSITY         = const(0x1f)
GRB               = True

# user switch
USER_SWITCH       = const(0)

# I2C
SCL               = const(15) # external I2C bus
SDA               = const(16)

# Touch screen
TS_FREQ           = const(100000)
TS_RESET          = const(18)

# microphone
MIC_WS            = const(26)
MIC_SCK           = const(22)
MIC_SD            = const(21)

# SPI
SPI_SCK           = const(12)
SPI_MISO          = const(13)
SPI_MOSI          = const(11)

# LCD
LCD_BL            = const(45)  # back light
LCD_CS            = const(10)  # chip select
LCD_DC            = const(46)


TS_INT            = const(17)

# Micro_SD
SDIO_CLK          = const(38)
SDIO_CMD          = const(40)
SDIO_D0           = const(39)
SDIO_D1           = const(41)
SDIO_D2           = const(48)
SDIO_D3           = const(47)

# audio
# AUDIO_EN          = const(01)

I2S_M_CLK         = const(4)
I2S_BUS_CLK       = const(5) # bit clock
I2S_DATA_OUT      = const(6) # to speaker
I2S_LRCK          = const(7) # left right clock
I2S_DATA_IN       = const(8) # from microphone                   

# uart
RX_DO             = const(43)
TX_D0             = const(44)

# battery
BAT               = const(9) # ADC channel to control battery charge

# external GPIO

IO2               = const(2)
IO3               = const(3)
IO14              = const(14)
IO21              = const(21)
