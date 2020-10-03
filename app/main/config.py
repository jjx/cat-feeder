from __future__ import absolute_import


class AppConfig(object):
    FOOD_DISPENSER_PIN = 1
    FOOD_DISPENSE_DURATION_SECONDS = 2
    FOOD_DISPENSER_ENABLED = True
    WATER_DISPENSER_PIN = 1
    WATER_DISPENSE_DURATION_SECONDS = 3
    WATER_DISPENSER_ENABLED = True
    CAT_FEEDER_SLACK_ENABLED = True


class Config(object):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = True


config_by_name = dict(
    dev=DevelopmentConfig,
    prod=ProductionConfig
)
