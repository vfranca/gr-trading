"""
scripts python
Copyright 2022 Valmir França da Silva

grupo de comandos gr (gerenciamento de risco)
"""
import click


# Importa os comandos
from gr_tk.em import em
from gr_tk.be import be
from gr_tk.ta import ta
from gr_tk.po import po


# Cria o grupo de comandos gr
@click.group()
def cli():
    """grupo de comandos gr (gernciamento de risco)."""
    pass


# Adiciona os comandos
cli.add_command(em)
cli.add_command(be)
cli.add_command(ta)
cli.add_command(po)


if __name__ == "__main__":
    cli()
