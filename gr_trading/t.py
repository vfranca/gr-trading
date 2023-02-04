# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click
from gr_trading.conf import digits as d


# Cria o comando t (trade)
@click.command()
@click.argument("entrada", type=float)
@click.option("--risco", "-r", type=float)
@click.option("--retorno", "-rr", type=float, default=1)
@click.option("--stop-loss", "-sl", type=float)
@click.option("--take-profit", "-tp", type=float)
def t(entrada, risco, retorno, stop_loss, take_profit):
    """Calcula o trade."""
    # Calcula o trade com stop loss definido
    if stop_loss:
        risco = entrada - stop_loss
    # Calcula o trade apenas com risco definido
    tp = entrada + risco
    sl = entrada - risco
    # Calcula o trade com retorno e risco definidos
    if retorno:
        tp = entrada + risco * retorno
    # Calcula o trade com take profit e risco definidos
    if take_profit:
        tp = take_profit
        retorno = (take_profit - entrada) / risco
    # Exibe o stop loss
    click.echo("%.{0}f sl".format(d) % sl)
    # Exibe o preço de entrada
    click.echo("%.{0}f e".format(d) % entrada)
    # Exibe a(s) parcial(is)
    if retorno > 1:
        for i in range(int(retorno)):
            i += 1
            if i == retorno:
                continue
            rp = entrada + risco * i
            click.echo("%.{0}f %ix".format(d) % (rp, i))
    # Exibe o take profit
    click.echo("%.{0}f tp".format(d) % tp)


if __name__ == "__main__":
    t()
