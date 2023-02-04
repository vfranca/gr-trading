# gr-trading
# Copyright 2023 Valmir França da Silva
# http://github.com/vfranca
from os import getenv

# Dígitos da moeda
digits = getenv("DIGITOS")
if digits == None:
    digits = 0
digits = int(digits)
