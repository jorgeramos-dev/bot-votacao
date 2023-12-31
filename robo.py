import requests
import time

cabecalho = {
	'accept-language': 'pt-BR,pt;q=0.9',
	'content-length': '602',
	'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'cookie': '_ga=GA1.2.493423716.1672238277; _gid=GA1.2.1876199481.1672238277; __cf_bm=vYqDeaSyRNBo6Hx8xDePVCc07Zq8U0RP0jUXnr0EwYo-1672238291-0-AWwqbtOcI4QgWDgSOXtCUeFe17UA2c++Ta4TAsr8oYQh2Tg82QaPhabzGaxH7QaafH6xhCEkGCjkoHjpPtL7E/nmUkEfSn0HHlUGkjF/pivtifFXBBsc3whlg87NpYaCWRsbDAHR9EoQpYh72/kshwQ=',
	'origin': 'https://corridadasblogueiras.com',
	'referer': 'https://corridadasblogueiras.com/',
	'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
	'sec-ch-ua-mobile': '?0',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-site',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

dados = {
	'blogueira':'1',
	'g-recaptcha-response':'03AD1IbLBEGbe533no36jPga2vRgxnpwMZ7vpdVClzdqjSqfrh3UBaO3RdqyVWCJ0Rk1ji1bOMqMy_tfC_L9LFdtSIj44shRByWzyMWZFyUVM73TKaYW1G_6Xv0kYD4vIs-hs1XQMKrRFH_epS2COppmI97-25KWOJQBnow8EK12lT8-d87Sh_81zvkPbQCyVPh38MVYvdyAMazpo5ygO5Xx6zI06SBXHI706CegpLYlZo04B-Y1PdE9Fx7JVc93eXXEWYRUvD403yOu66Ddtco-JTfHTP65ZnD9E2GSd2MFF0UuibbaGzkGBxTV6MoKGvVUCZ1P7w7eTUnKzOLaQ8UV03RtiAcTyXbikOj3I0R3nnEzKx91oMwiqm292XX-PBjx2slLp1QcYFwEfFmGOUyKdkUS3KZZDdNnC00djU_Ts6NYF2A4FgDpoIWcx438n-71n8lRscsONtSoGrZpdMGDv7NRiCmy4cs6YK8CB0QRVu_T5k44LsEsM7SCAEp8v6NXpfoQgre73vE2OA7tba6E1ILUz3-JE-E432FcXPdIoOxwhRqXDP7Jg'
}


with requests.Session() as s:
	while True:
		s.get('https://corridadasblogueiras.com/')
			
		if s.post('https://corridadasblogueiras.com/processa.php', headers=cabecalho, data=dados).status_code == 200:
			print(f'voto computado participante 1')
		else:
			print('voto não aceito')
		time.sleep(9)