import subprocess
import os
import typer

app = typer.Typer()


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}", color=typer.colors.RED)


@app.command()
def add(num1: int, num2: int):
    sum = num1+num2
    typer.echo(typer.style(num1+num2, fg=typer.colors.RED))


@app.command()
def flutterr():
    os.chdir('/home/aaqil/python/projects/experiments/')
    wd = os.getcwd()
    # subprocess.run(['rmdir', 'newfolder'])
    subprocess.run('ls')
    typer.echo(wd)


@app.command()
def dirr(create: bool = True, rename: bool = False):
    os.chdir('/home/aaqil/python/projects/experiments/')
    if create == True and rename == False:
        subprocess.run(['mkdir', 'hello'])
        print(os.getcwd())
    else:
        source = os.path.join(os.getcwd(), 'hello')
        tar = os.path.join(os.getcwd(), 'new')
        subprocess.run(['mv', source, tar])
        subprocess.run(['ls'])

        print(os.getcwd())


if __name__ == '__main__':
    app()
