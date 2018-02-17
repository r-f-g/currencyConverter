import fire
from moduls.currency import Exchange
from moduls.api import flaskAPI

def manager(flask=None, **kwargs):
	if flask == None:
		return Exchange().ECB(**kwargs)
	else:
		flaskAPI.app.run(**kwargs)

if __name__ == '__main__':
	fire.Fire(component=manager)
	