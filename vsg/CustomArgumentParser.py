import argparse
import sys
from gettext import gettext as _


class CustomArgumentParser(argparse.ArgumentParser):
    """
    Custom class derived from argparse to modify the exit code when an error occurs.
    As told in https://www.python.org/dev/peps/pep-0389/#discussion-sys-stderr-and-sys-exit.
    """

    def error(self, message):
        self.print_usage(sys.stderr)
        args = {'prog': self.prog, 'message': message}
        self.exit(1, _('%(prog)s: error: %(message)s\n') % args)
