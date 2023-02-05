# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
from click.testing import CliRunner
from pytest import mark
from gr_trading.gr import gr

run = CliRunner()


def test_exibe_versao():
    res = run.invoke(gr, ["--version"])
    assert res.output == "gr-trading 0.6\n"


@mark.skip()
def test_exibe_aviso_sem_comando():
    res = run.invoke(gr)
    assert res.output == "Digite gr --help para ajuda\n"
