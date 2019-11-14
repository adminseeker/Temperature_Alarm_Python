import time
import pigpio
import DHT22

pi=pigpio.pi()
s=DHT22.sensor(pi,18)

def dht22_read():
	s.trigger()
	temp='%.2f' % (s.temperature())
	humid='%.2f' % (s.humidity())
	return (temp,humid)

