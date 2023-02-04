# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from gr_trading.gr import gr

run = CliRunner()


def test_calcula_uma_compra_apenas_com_risco_definido():
    res = run.invoke(gr, ["t", "114500", "--risco", "300"])
    assert res.output == "114200 sl\n114500 e\n114800 tp\n"


def test_calcula_uma_compra_com_stop_loss_definido():
    res = run.invoke(gr, ["t", "114500", "--stop-loss", "114300"])
    assert res.output == "114300 sl\n114500 e\n114700 tp\n"


def test_calcula_uma_compra_com_risco_e_retorno_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "300", "--retorno", "2"])
    assert res.output == "114200 sl\n114500 e\n114800 1x\n115100 tp\n"


def test_calcula_uma_compra_com_risco_e_take_profit_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "300", "--take-profit", "115310"])
    assert res.output == "114200 sl\n114500 e\n114800 1x\n115100 2x\n115310 tp\n"


def test_calcula_uma_venda_apenas_com_risco_definido():
    res = run.invoke(gr, ["t", "114500", "--risco", "-300"])
    assert res.output == "114800 sl\n114500 e\n114200 tp\n"


def test_calcula_uma_venda_com_stop_loss_definido():
    res = run.invoke(gr, ["t", "114500", "--stop-loss", "114700"])
    assert res.output == "114700 sl\n114500 e\n114300 tp\n"


def test_calcula_uma_venda_com_risco_e_retorno_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "-300", "--retorno", "2"])
    assert res.output == "114800 sl\n114500 e\n114200 1x\n113900 tp\n"


def test_calcula_uma_venda_com_risco_e_take_profit_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "-300", "--take-profit", "113810"])
    assert res.output == "114800 sl\n114500 e\n114200 1x\n113900 2x\n113810 tp\n"


def test_exibe_uma_compra_com_retorno_maior_que_1():
    res = run.invoke(gr, ["t", "114500", "--risco", "300", "--retorno", "2"])
    assert res.output == "114200 sl\n114500 e\n114800 1x\n115100 tp\n"
