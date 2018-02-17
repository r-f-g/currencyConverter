# currency converter

## Data source

- **ECB** - European Central Bank

## Used packages

- `flask`
- `fire`
- `requests`
- `django`
- `xml`

## Parameters

- `amount` - amount which we want to convert - float
- `input_currency` - input currency - 3 letters name or currency symbol
- `output_currency` - requested/output currency - 3 letters name or currency symbol
- `dec` - number of decimal places used in output

## Functionality

- if output_currency param is missing, convert to all known currencies

## Output

- json with following structure.

```
{
    "input": { 
        "amount": <float>,
        "currency": <3 letter currency code>
    }
    "output": {
        <3 letter currency code>: <float>
    }
}
```

## Usage

### CLI

```
./currency_converter.py --amount XXX --input_currency XXX --output_currency XXX --dec XXX
```

### django

add lines to `urls.py`

```
from currencyConverter.moduls.api import djangoAPI
urlpatterns = [
	url(r'^currency_converter$', djangoAPI.get, name='currency_converter'),
]
```

### Flask

```
./currency_converter.py --flask --port XXX --host XXX
```


## Examples

### CLI 
```
./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
{   
    "input": {
        "amount": 100.0,
        "currency": "EUR"
    },
    "output": {
        "CZK": 2707.36, 
    }
}
```
```
./currency_converter.py --amount 10.92 --input_currency £ 
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "EUR": 14.95,
        "USD": 17.05,
        "CZK": 404.82,
        .
        .
        .
    }
}
```
### API
```
GET /currency_converter?amount=0.9&input_currency=¥&output_currency=AUD HTTP/1.1
{   
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20, 
    }
}
```

```
GET /currency_converter?amount=10.92&input_currency=£ HTTP/1.1
{
    "input": {
        "amount": 10.92,
        "currency": "GBP"
    },
    "output": {
        "EUR": 14.95,
        "USD": 17.05,
        "CZK": 404.82,
        .
        .
        .
    }
}
```