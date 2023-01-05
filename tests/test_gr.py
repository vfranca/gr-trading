# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from gr_trading.gr import gr

run = CliRunner()


def test_exibe_versao():
    res = run.invoke(gr, ["--version"])
    assert res.output == "gr-trading 0.5.0\n"


@mark.skip()
def test_exibe_aviso_sem_comando():
    res = run.invoke(gr)
    assert res.output == "Digite gr --help para ajuda\n"


def test_calcula_o_risco_do_capital_por_trade():
    res = run.invoke(gr, ["r", "50", "1000"])
    assert res.output == "5.0% de risco\n"


def test_calcula_o_risco_retorno_da_operacao():
    res = run.invoke(gr, ["e", "20", "10", "40"])
    assert res.output == "10.00 risco\n20.00 retorno\n2.0 retorno/risco\n"
