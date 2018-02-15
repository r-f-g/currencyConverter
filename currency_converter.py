from moduls.currency import ECB
import fire


if __name__ == '__main__':
	fire.Fire(component=ECB().exchange)