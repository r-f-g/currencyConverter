try:
	from .moduls.currency import ECB
except:
	from moduls.currency import ECB
import fire
from django.http import JsonResponse

def django(request):
	if request.method == 'GET':
		argv = {}
		argv['amount'] = float(request.GET['amount'])
		argv['input_currency'] = request.GET['input_currency']
		if 'output_currency' in request.GET: argv['output_currency'] = request.GET['output_currency']
		if 'dec' in request.GET: argv['dec'] = int(request.GET['dec'])
		return JsonResponse(ECB().exchange(**argv))
	else:
		return JsonResponse({'ERROR': 'wrong method'})

if __name__ == '__main__':
	fire.Fire(component=ECB().exchange)