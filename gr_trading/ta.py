# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando ta
@click.command()
@click.argument("acertos", type=int)
@click.argument("erros", type=int)
def ta(acertos, erros):
    """comando ta (taxa de acerto)."""
    trades = acertos + erros
    taxa_acerto = acertos / trades * 100
    click.echo("%i acertos" % acertos)
    click.echo("%i erros" % erros)
    click.echo("%i%% taxa de acerto" % taxa_acerto)


if __name__ == "__main__":
    ta()
