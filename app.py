from flask import Flask
import serial
app = Flask(__name__)

#Using xbee
serial = serial.Serial('/dev/ttyUSB0', 9600)

colors = {
	'red': 'r',
	'green': 'g',
	'blue': 'b',
}

@app.route('/<color>/<int:state>/')
def access_rgb_led(color, state):
	serial_data = "%s%d\n" % (colors[color], state)
	serial.write(serial_data)
	led_state = 'on' if state == 0 else 'off'
	return "%s is %s" % (color, led_state)

if __name__ == '__main__':
	app.run(host='10.0.0.10')
