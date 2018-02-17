from flask import Flask, jsonify, request
from django.http import JsonResponse
from .currency import Exchange

class flaskAPI:
	app = Flask(__name__)
	EX = Exchange()

	@app.route('/currency_converter')
	def get():
		argv = {}
		argv['amount'] = float(request.args.get('amount'))
		argv['input_currency'] = request.args.get('input_currency')
		if 'output_currency' in request.args: argv['output_currency'] = request.args.get('output_currency')
		if 'dec' in request.args: argv['dec'] = int(request.args.get('dec'))
		return jsonify(flaskAPI.EX.ECB(**argv))

class djangoAPI:
	EX = Exchange()

	def get(request):
		argv = {}
		argv['amount'] = float(request.GET['amount'])
		argv['input_currency'] = request.GET['input_currency']
		if 'output_currency' in request.GET: argv['output_currency'] = request.GET['output_currency']
		if 'dec' in request.GET: argv['dec'] = int(request.GET['dec'])
		return JsonResponse(djangoAPI.EX.ECB(**argv))