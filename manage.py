#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'collectWeb.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # args = sys.argv
    # if "runserver" in args:
    #     args.append("--noreload")
    execute_from_command_line(sys.argv)

    #自启动服务器
    # from django.core.management import call_command
    # call_command('runserver', '127.0.0.1:8000')

if __name__ == '__main__':
    main()
