"""Gunicorn config files."""

# for more directives see:
# http://gunicorn-docs.readthedocs.io/en/latest/settings.html#config-file

# The socket to bind.
bind = '0.0.0.0:8000'

# Numer of worker processes generally in the 2-4 x $(NUM_CORES) range.
workers = 5

# print access/error lines to stdout
accesslog = '-'
errorlog = '-'
