from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'includes': 'cairo, pango, pangocairo, atk, gobject'}},
    windows = [{'script': "ctrl.py"}],
    data_files = [('.', ['unsaved.glade'])],
    zipfile = None,
)