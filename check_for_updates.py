import click
import subprocess
import requests


programs = ['git']
cli = click.Group()

@cli.command(help="Which program you would like to check the version of.")
@click.option(
    "--program", default='git'
)
def check_for_updates(program):
    """Verify the current version of a given program."""
    if (program in programs):
        check_git_version()

def check_git_version():
    version = subprocess.run(['git', 'version'], stdout=subprocess.PIPE).stdout.decode("utf-8")

    response = requests.get('https://git-scm.com/downloads')
    if int(response.status_code) >= 200 and int(response.status_code) < 300:
        current_version = (response.content.decode("utf-8")).split('class="version">\n')[1].split('\n')[0].strip()
        
        if (current_version in version):
            print('Git is all up to date!')
            return
        
        print(f'Git is currently outdated with {version}. Update to {current_version}')
        return

    print("Was unable to retrieve the most up to date version")

@cli.command()
def list():
    print(programs)

if __name__ == "__main__":
    cli()
