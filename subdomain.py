import requests 
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Subdomain Scanner")
print(ascii_banner)
print("by Shoumik Chandra")

discovered_subdomains = []

domain = input ("Enter the Domain : ")
s_file = open("subdomain.txt")
content= s_file.read()
subdomains = content.splitlines()

for subdomain in subdomains : 
	url = f"http://{subdomain}.{domain}"
	try :
		requests.get(url)
	except requests.ConnectionError : 
		pass
	else :
		print(f"Discovered subdomain : {url}")
		discovered_subdomains.append(url)
