# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from gr_trading.gr import gr

run = CliRunner()


def test_calcula_uma_compra_apenas_com_risco_definido():
    res = run.invoke(gr, ["t", "114500", "--risco", "300"])
    assert res.output == "114800 tp\n114500 e\n114200 sl\n"


def test_calcula_uma_compra_com_stop_loss_definido():
    res = run.invoke(gr, ["t", "114500", "--stop-loss", "114300"])
    assert res.output == "114700 tp\n114500 e\n114300 sl\n"


def test_calcula_uma_compra_com_risco_e_retorno_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "300", "--retorno", "2"])
    assert res.output == "115100 tp\n114500 e\n114200 sl\n"


def test_calcula_uma_compra_com_risco_e_take_profit_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "300", "--take-profit", "115310"])
    assert res.output == "115310 tp\n114500 e\n114200 sl\n"


def test_calcula_uma_venda_apenas_com_risco_definido():
    res = run.invoke(gr, ["t", "114500", "--risco", "-300"])
    assert res.output == "114200 tp\n114500 e\n114800 sl\n"


def test_calcula_uma_venda_com_stop_loss_definido():
    res = run.invoke(gr, ["t", "114500", "--stop-loss", "114700"])
    assert res.output == "114300 tp\n114500 e\n114700 sl\n"


def test_calcula_uma_venda_com_risco_e_retorno_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "-300", "--retorno", "2"])
    assert res.output == "113900 tp\n114500 e\n114800 sl\n"


def test_calcula_uma_venda_com_risco_e_take_profit_definidos():
    res = run.invoke(gr, ["t", "114500", "--risco", "-300", "--take-profit", "113810"])
    assert res.output == "113810 tp\n114500 e\n114800 sl\n"


# def test_calcula_um_trade_com_entrada_risco_e_retorno():
# res = run.invoke(gr, ["t", "114500", "-r", "250", "-rr", "2"])
# assert (
# res.output
# == "115000 =2x\n114750 =1x\n114000 =entrada\n113750 =stoploss\n250 =risco\n2.0 = retorno\n"
# )
