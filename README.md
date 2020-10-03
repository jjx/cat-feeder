Simple python flask cat feeder application that runs on top of the Raspberry Pi.

Hardware Setup
- Raspberry Pi (any will do - eg. https://www.amazon.com/Raspberry-Pi-MS-004-00000024-Model-Board/dp/B01LPLPBS8)
- Relay 2 channel min (used to control the motor driving the food dispenser and the water pump)
- High torque, low RPM motor (eg. https://www.amazon.com/Greartisan-Electric-Reduction-Eccentric-Diameter/dp/B071KFSM8V/)
- Water pump (eg. https://www.amazon.com/VIVOSUN-Submersible-Fountain-Aquarium-Hydroponics/dp/B07L54HB83)
- Cereal dispenser (eg. https://www.amazon.com/KCH-06134-Compact-Dispenser-Control-Chrome/dp/B0057BBKEW)
- Motor coupler (used to attach the motor to the cereal dispenser knob)
- PVC soft tubing (used to direct water from the water pump to the water bowl)

Before you run the application
- Look at the AppConfig class in app/main/config.py and update any of the pins and enable flags.
- Run bin/setup.sh, this sets up the application environment. The python app has been tested against 3.7.7, but it should work for 3.5+.knob

How to run
./bin.setup.sh
source env/bin/activate
python manage.py run_app

How to test
curl 'localhost:5000/meal?water=1'
curl 'localhost:5000/meal?food=1'
curl 'localhost:5000/meal?food=1&water=1'
