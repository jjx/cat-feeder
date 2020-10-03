from __future__ import absolute_import

import subprocess
import sys


EXIT_CODE_SUCCESS = 0
HASH = '#'


def run_shell_command(args, stdin=None):
    process = subprocess.Popen(args, stdin=stdin, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    std_out, std_err = process.communicate()
    return std_out, std_err, process.returncode


def get_hostname():
    hostname, _, _ = run_shell_command(['hostname'])
    return hostname.strip()


def is_mac():
    return sys.platform == 'darwin'


def prepend_hash(s):
    if s.startswith(HASH):
        return s
    else:
        return HASH + s
