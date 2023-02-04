# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click
from gr_trading.conf import digits as d


# Cria o comando t (trade)
@click.command()
@click.argument("entrada", type=float)
@click.option("--risco", "-r", type=float)
@click.option("--retorno", "-rr", type=float)
@click.option("--stop-loss", "-sl", type=float)
@click.option("--take-profit", "-tp", type=float)
def t(entrada, risco, retorno, stop_loss, take_profit):
    """Calcula risco, retorno e payoff da operação."""
    # Calcula o risco sem retorno, sem stop loss e sem take profit
    if risco:
        tp = entrada + risco
        sl = entrada - risco
    click.echo("%.{0}f 1x".format(d) % tp)
    click.echo("%.{0}f e".format(d) % entrada)
    click.echo("%.{0}f sl".format(d) % sl)


if __name__ == "__main__":
    t()
