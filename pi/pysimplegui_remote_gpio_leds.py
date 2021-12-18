import PySimpleGUI as psg
from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

host_pi = '192.168.1.166'

led1 = LED(4, pin_factory=PiGPIOFactory(host='192.168.1.166'))
led2 = LED(18, pin_factory=PiGPIOFactory(host=host_pi))
led3 = LED(24, pin_factory=PiGPIOFactory(host=host_pi))
led4 = LED(11, pin_factory=PiGPIOFactory(host=host_pi))
led5 = LED(12, pin_factory=PiGPIOFactory(host=host_pi))
led6 = LED(7, pin_factory=PiGPIOFactory(host=host_pi))
led7 = LED(16, pin_factory=PiGPIOFactory(host=host_pi))
led8 = LED(6, pin_factory=PiGPIOFactory(host=host_pi))

# make items list in code
led_list = []
i = 0
while i < 9:
    if i == 0:
        i = i + 1
    else:
        led_num = 'led' + str(i)
        led_list.append([psg.Text(led_num, click_submits=True)])
        i = i + 1

layout = [
    [psg.Text('Click an item to turn on corresponding LED.')],
    [psg.Text('Click button to reset.')],
    [psg.Column(layout=led_list, size=(50, 100), scrollable=True,
                background_color='light grey')],
    [psg.Button('Turn All LEDs\' Off', key='all_off')],
]

window = psg.Window('Control Pi led by IP', layout,
                    size=[400, 250], resizable=True)

while True:
    event, values = window.Read()

    if event == 'all_off':
        if led1.is_active:
            led1.off()
            print('led1 off')
        if led2.is_active:
            led2.off()
            print('led2 off')
        if led3.is_active:
            led3.off()
            print('led3 off')
        if led4.is_active:
            led4.off()
            print('led4 off')
        if led5.is_active:
            led5.off()
            print('led5 off')
        if led6.is_active:
            led6.off()
            print('led6 off')
        if led7.is_active:
            led7.off()
            print('led7 off')
        if led8.is_active:
            led8.off()
            print('led8 off')

    elif event == 'led1':
        led1.on()
        print('led1 on')
    elif event == 'led2':
        led2.on()
        print('led2 on')
    elif event == 'led3':
        led3.on()
        print('led3 on')
    elif event == 'led4':
        led4.on()
        print('led4 on')
    elif event == 'led5':
        led5.on()
        print('led5 on')
    elif event == 'led6':
        led6.on()
        print('led6 on')
    elif event == 'led7':
        led7.on()
        print('led7 on')
    elif event == 'led8':
        print('led8 on')
        led8.on()

    elif event is None:
        break

led1.close()
led2.close()
led3.close()
led4.close()
led5.close()
led6.close()
led7.close()
led8.close()
window.Close()
print('done')
