# gr-trading
# Copyright 2022 Valmir França da Silva
# http://github.com/vfranca
import click


# Cria o comando e (entrada)
@click.command()
@click.argument("entrada", type=float)
@click.argument("stop-loss", type=float)
@click.argument("take-profit", type=float)
def e(entrada, stop_loss, take_profit):
    """Calcula risco, retorno e payoff da operação."""
    # Calcula o risco da operação em pontos
    risco = abs(entrada - stop_loss)
    # Calcula o take-profit da operação em pontos
    ganho = abs(take_profit - entrada)
    # Calcula o retorno/risco da operação
    rr = ganho / risco
    click.echo("%.2f risco" % risco)
    # Exibe o resultado
    click.echo("%.2f retorno" % ganho)
    click.echo("%.1f retorno/risco" % rr)


if __name__ == "__main__":
    e()
