import time
import shodan
import requests
import threading



ips = []
api = "ENTER YOUR API KEY HERE"
print(">> [*] API Authenticating")
try:
	auth = shodan.Shodan(api)
	print(">> [*] API Authentication Success")
except Exception:
	print(">> [-] API Authentication Failed")

print(">> [*] Searching For Possibly Vulnerable Servers.....")
resp = auth.search("apache version 2")
for match in resp['matches']:
	ips.append(match['ip_str'])

ipss = set(ips)

print(">> [+] Found Possibly Vulnerable Servers in Total of : " + str(len(ipss)))
print(">> [*] Checking if one of these Possibly Vulnerable Servers is indeed Vulnerable.....")


def check():
	try:
		r = requests.get("http://" + str(ip))
		server = r.headers['server']
		if("Apache/2." in server and "Apache/2.4" not in server):
			print(">> [+] Possibly Vulnerable WebServer: " + str(ip))
		else:
			pass
	except Exception:
		pass



for ip in ipss:
	t = threading.Thread(target=check)
	t.start()
	time.sleep(1)


'''def check():
	for ip in ipss:
		try:
			r = requests.get("http://" + str(ip))
			server = r.headers['server']
			if("/" in server):
				splitt = server.split("/")
				splittt = splitt.split(".")
				combined = (str(splittt[0]) + "." + str(splitt[1]))
				print(combined)
			else:
				pass
		except Exception:
			pass'''







