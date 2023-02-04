# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from gr_trading.gr import gr

run = CliRunner()


def test_calcula_um_trade_com_risco_definido():
    res = run.invoke(gr, ["t", "114500", "--risco", "300"])
    assert res.output == "114800 1x\n114500 e\n114200 sl\n"


# def test_calculaUm_trade_com_risco_e_retorno_definidos():
# def test_calcula_um_trade_com_stop_loss_definido():
# def test_calcula_um_trade_com_stop_loss_e_retorno_definidos():
# def test_calcula_um_trade_com_entrada_risco_e_retorno():
# res = run.invoke(gr, ["t", "114500", "-r", "250", "-rr", "2"])
# assert (
# res.output
# == "115000 =2x\n114750 =1x\n114000 =entrada\n113750 =stoploss\n250 =risco\n2.0 = retorno\n"
# )
