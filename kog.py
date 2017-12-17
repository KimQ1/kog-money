# -*- coding: utf-8 -*-


import logging
import os
from time import sleep

# 屏幕分辨率
device_x, device_y = 1920, 1080

# 是否已完整通关
already_pass = True

# 各步骤等待间隔
step_wait = [3, 13, 55, 3, 3]

# 刷金币次数
repeat_times = 50

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)


def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x, base_y = 1920, 1080
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))


def do_money_work():
    if not already_pass:
        logging.debug('#0 start the game')
        tap_screen(1600, 970)
        sleep(step_wait[0])

    logging.debug('#1 ready, go!!!')
    tap_screen(1450, 910)
    sleep(step_wait[1])

    logging.debug('#2 auto power on!')
    tap_screen(1780, 40)
    sleep(step_wait[2])

    logging.debug('#3 well done!')
    tap_screen(940, 1000)
    sleep(step_wait[3])

    logging.debug('#4 do it again...\n')
    tap_screen(1430, 980)
    sleep(step_wait[4])


if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('round #{}'.format(i + 1))
        do_money_work()