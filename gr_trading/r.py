# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando r
@click.command()
@click.argument("risco", type=float)
@click.argument("capital", type=float)
def r(risco, capital):
    """comando r (risco) calcula o risco do capital por trade."""
    r_percentual = risco / capital * 100
    click.echo("%.1f%% de risco" % r_percentual)


if __name__ == "__main__":
    r()
