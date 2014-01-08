import smtplib


def send_text():
	"""
	Sends text message when script finishes running.
	"""
	fromaddr = 'law826@gmail.com'
	toaddrs = '7043406264@vtext.com'
	msg = 'Your script has finished running.'
	username = 'law826'
	password = 'YumWoonsen26???'

	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username, password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()