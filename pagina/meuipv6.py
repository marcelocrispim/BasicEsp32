from requests import Session

requests = Session()

ipv6 = requests.get('http://v6.ident.me/').text
key = 'RDqpkcz-R2fq99tRa_KxNzAPTuF8mf'
host = 'crispim.dns.army'
url = 'http://dynv6.com/api/update'
payload = dict(token=key, hostname=host, ipv6=ipv6)
print(requests.get(url=url, params=payload).content.decode())
