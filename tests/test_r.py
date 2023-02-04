# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from gr_trading.gr import gr

run = CliRunner()


def test_calcula_o_risco_do_capital_por_trade():
    res = run.invoke(gr, ["r", "50", "1000"])
    assert res.output == "5.0% de risco\n"
