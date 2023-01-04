# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click
from gr_trading import __version__


# Importa os comandos
from gr_trading.em import em
from gr_trading.be import be
from gr_trading.ta import ta
from gr_trading.po import po


# Cria o grupo de comandos gr
@click.group(invoke_without_command=True)
@click.option("--version", "-v", is_flag=True, help="Show the version and exit.")
def gr(version):
    """grupo de comandos gr (gerenciamento de risco para trading)."""
    if version:
        click.echo("gr-trading %s" % __version__)
    else:
        click.echo("Digite gr --help para ajuda")


# Adiciona os comandos
gr.add_command(em)
gr.add_command(be)
gr.add_command(ta)
gr.add_command(po)


if __name__ == "__main__":
    gr()
