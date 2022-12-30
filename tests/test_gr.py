# gr-trading
# Copyright 2022 Valmir França da Silva
from click.testing import CliRunner
from gr_trading.gr import gr

run = CliRunner()


def test_exibe_versao():
    res = run.invoke(gr, ["--version"])
    assert res.output == "gr-trading 0.3\n"
