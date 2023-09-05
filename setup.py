from distutils.core import setup
import py2exe

setup(
    name='YouTube Video Downloader',
    author='Aswin Menon',
    version='1.0.0',
    description='Application to download YouTube videos',
    data_files=[('',['favicon.ico'])],
    options={
        'py2exe': {
            'bundle_files': 1,
            'compressed': True,
            'optimize': 2,
            'dll_excludes': ['w9xpopen.exe'],
        }
    },
    windows=[{
        'script': 'YouTube Video Downloader.py',
        'icon_resources': [(1, 'favicon.ico')]
    }],
    zipfile=None,
)