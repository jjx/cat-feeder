from __future__ import absolute_import

from flask import Blueprint, render_template, request
import random
import time

from app.main.config import AppConfig
from app.main.lib import run_shell_command
from app.main.lib.gpio import Gpio
from app.main.lib.string import to_boolean
from app.main.vendor.slack import Slack

cat_feeder_blueprint = Blueprint('cat_feeder_blueprint', __name__)

GREETINGS = ['नमस्ते!', 'Bonjour!', 'Halo!', 'Hello!', 'Hola!',
             'こんにちは!', '你好!', 'Ola!', 'cześć!']
THANKS = ['thx', 'thanks', 'danku', 'tanks']


@cat_feeder_blueprint.route('/')
def index():
    try:
        git_ref, _, _ = run_shell_command(
            ['git', 'rev-parse', '--short', 'HEAD'])
        version_msg = 'version {}'.format(str(git_ref.decode().strip()))
    except OSError:
        version_msg = ''
    return render_template('index.html', version_message=version_msg)


@cat_feeder_blueprint.route('/meal')
def meal():
    dispense_food = to_boolean(request.args.get('food'))
    dispense_water = to_boolean(request.args.get('water'))
    food_and_water_for_the_kitty(dispense_food=dispense_food,
                                 dispense_water=dispense_water)
    notify(dispense_food=dispense_food, dispense_water=dispense_water)
    return 'OK', 200


def food_and_water_for_the_kitty(dispense_food, dispense_water):
    # Respect AppConfig flags
    dispense_food = AppConfig.FOOD_DISPENSER_ENABLED and dispense_food
    dispense_water = AppConfig.WATER_DISPENSER_ENABLED and dispense_water

    if dispense_food:
        Gpio.set_out(AppConfig.FOOD_DISPENSER_PIN)
        Gpio.write_0(AppConfig.FOOD_DISPENSER_PIN)
        time.sleep(AppConfig.FOOD_DISPENSE_DURATION_SECONDS)
        Gpio.write_1(AppConfig.FOOD_DISPENSER_PIN)

    if dispense_water:
        Gpio.set_out(AppConfig.WATER_DISPENSER_PIN)
        Gpio.write_0(AppConfig.WATER_DISPENSER_PIN)
        time.sleep(AppConfig.WATER_DISPENSE_DURATION_SECONDS)
        Gpio.write_1(AppConfig.WATER_DISPENSER_PIN)


def notify(dispense_food, dispense_water):
    if not dispense_food and not dispense_water:
        return

    message = '{} {} 4 the '.format(random.choice(GREETINGS),
                                    random.choice(THANKS))
    if dispense_food:
        message += '#food'
        if dispense_water:
            message += ' and '

    if dispense_water:
        message += '#water'

    message = message.strip() + '\n- MeowBot'

    if AppConfig.CAT_FEEDER_SLACK_ENABLED:
        Slack.general(message)
