import ledtest
import temptest
import time
import smtplib

ledt=ledtest
tempt=temptest

def mail_sender(email,password,result):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,result)
    server.quit()

email="email"
password="password"

def alarm_sound_on():
	ledt.buzz_on()
def alarm_sound_off():
	ledt.buzz_off
def reset_alarm():
	ledt.buzz_off()
        ledt.led_off(ledt.red)
        ledt.led_off(ledt.yellow)
        ledt.led_off(ledt.green)

data=""
(temp,humid)=tempt.dht22_read()
while True:
	data=raw_input("Enter Command: ")
	if(data=="start alarm"):
		data1=0
		data2=0
		check=""
		data1=raw_input("Highest temperature allowed: ")
		data2=raw_input("Medium temperature allowed: ")
		while True:
			try:
				time.sleep(5)
				(temp,humid)=tempt.dht22_read()
				result="Temperature : "+str(temp)+" Humidity: "+str(humid)+"%"
				print(result)
				if(temp>=data1):
					ledt.buzz_on()
					ledt.led_on(ledt.red)
					#result1=" DANGER!!! RED ALERT"
					mail_sender(email,password,"DANGER!!! RED ALERT")
					ledt.led_off(ledt.yellow)
					ledt.led_off(ledt.green)
				elif(temp>=data2 and temp<data1):
					ledt.led_on(ledt.yellow)
					ledt.buzz_on()
					#result2=" ALERT!!! MEDIUM TEMPERATURE EXCEEDED"
                                        mail_sender(email,password,"ALERT!!! MEDIUM TEMPERATURE LIMIT EXCEEDED")
					ledt.led_off(ledt.red)
					ledt.led_off(ledt.green)
				elif(temp<data2):
					ledt.led_on(ledt.green)
					ledt.led_off(ledt.red)
					ledt.led_off(ledt.yellow)
					ledt.buzz_off()
			except:
				reset_alarm()
				print("exception raised")
				exit()

	elif(data=="reset alarm"):
		reset_alarm()

	elif(data=="display temperature"):
		time.sleep(3)
                (temp,humid)=tempt.dht22_read()
                print("Temperature: "+str(temp)+" Humidity: "+str(humid)+"%")

	elif(data=="exit"):
		reset_alarm()
		exit()
