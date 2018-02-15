import requests, json, os
import xml.etree.ElementTree as ET

class Symbols:
	def load():
		with open(os.path.dirname(os.path.realpath(__file__))+'/currency_symbols.json', 'r') as f:
			symbols_json = json.load(f)
		return {''.join([chr(c) for c in symbols_json[s]]):s for s in symbols_json}
	
	symbols = load()

class ECB(Symbols):
	def __init__(self):
		self.__url = 'http://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'

	def __getRates(self):
		status = '000'
		try:
			response = requests.get(self.__url)
			status = response.status_code
			currency = {tag.attrib['currency']:float(tag.attrib['rate']) for tag in ET.fromstring(response.text).iter() if 'currency' in tag.attrib}
			currency['EUR'] = 1
			return currency, status
		except:
			return {}, status

	def exchange(self, amount, input_currency, output_currency=None, dec=2):
		rates, status = self.__getRates()
		inputC = Symbols.symbols[input_currency] if input_currency in Symbols.symbols else input_currency
		#test if input_currency is in rates
		if inputC not in rates: return {'ERROR': 'input_currency "{0}" is not in rates'.format(inputC)}
		if output_currency != None:
			outputC = Symbols.symbols[output_currency] if output_currency in Symbols.symbols else output_currency
			#test if output_currency is in rates
			if outputC not in rates: return {'ERROR': 'output_currency "{0}" is not in rates'.format(outputC)}
			if inputC == outputC: return {inputC:1}
			return {'input': {'amount':amount, 'currency':inputC}, 'output':{outputC:round((amount*(1/rates[inputC])*rates[outputC]),dec)}}
		else:
			return {'input': {'amount':amount, 'currency':inputC}, 'output':{c:round((amount*(1/rates[inputC])*rates[c]),dec) for c in rates if c != inputC}}