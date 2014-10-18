import sys
print type(int(sys.argv[1]))
if (len(sys.argv) != 2) or (type(int(sys.argv[1])) != long):
	sys.exit("Please provide with a valid Railway PNR as a parameter")
	
else:
	import requests
	from BeautifulSoup import BeautifulSoup

	with requests.Session() as c:
		url = 'http://ipnrstatus.in/pnr-result.php' 
		c.get(url) 
		req_data = dict(lccp_pnrno1=sys.argv[1], submitpnr="Get PNR Status")
		page = c.post(url, data=req_data, headers={"Origin":"http://ipnrstatus.in", "Referer":"http://ipnrstatus.in/"}) 

		soup = BeautifulSoup(page.text)
		print soup.title.text

		tab = soup.findAll('table')

		print tab[1].fetch('b')[2].text