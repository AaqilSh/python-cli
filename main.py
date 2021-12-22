import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}", color=typer.colors.RED)


if __name__ == '__main__':
    app()
