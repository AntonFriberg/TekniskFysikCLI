"""
TekniskFysikCLI

Usage:
    TekniskFysikCLI entire
    TekniskFysikCLI hello
    TekniskFysikCLI -h | --help
    TekniskFysikCLI --version

Options:
  -h --help                         Show this screen.
  ---version                        Show version.

Examples:
    TekniskFysikCLI hello

Help:
    For help using this tool, please open an issue on the Github repository:
    https://github.com/AntonFriberg/TekniskFysikCLI
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION

def main():
    """Main CLI entrypoint."""
    import TekniskFysikCLI.commands
    # __doc__ is a special variable that references this file's docstring.
    options = docopt(__doc__, version=VERSION)

    # Try to dynamically match the command the user is trying to run with a
    # pre-defined command already created.
    for (k, v) in options.items():
        if hasattr(TekniskFysikCLI.commands, k) and v:
            module = getattr(TekniskFysikCLI.commands, k)
            TekniskFysikCLI.commands = getmembers(module, isclass)
            command = [command[1] for command in TekniskFysikCLI.commands if
                       command[0] != 'Base'][0]
            command = command(options)
            command.run()
