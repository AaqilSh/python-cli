import click
import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}", color=typer.colors.RED)


@app.command()
def add(num1: int, num2: int):
    sum = num1+num2
    typer.echo(typer.style(num1+num2, fg=typer.colors.RED))


if __name__ == '__main__':
    app()
