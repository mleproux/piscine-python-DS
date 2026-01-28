# <ins>FTPACKAGE</ins>

ft_package is a small python package including 2 functions
## Functions :

### censor_text(text: str) -> str
Return a censored version of the provided string using *

### double_string(text:str) -> str
Return a duplicated version of the provided string

## installation :

### build the package

`python -m build`

### Install the package

`pip install ./dist/ft_package-0.0.1.tar.gz`

or

`pip install ./dist/ft_package-0.0.1-py3-none-any.whl`

## Basic usage :

```python
from ft_package import censor_text
from ft_package import double_string

print(censor_text("Bonjour"))
print(double_string("cou"))
```