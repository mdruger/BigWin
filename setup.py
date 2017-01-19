from setuptools import setup, find_packages

setup(
    name="Lucky",
    version="0.1",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    scripts=[
        'lucky.py',
        'billionaire.py'.
        'speculator.py',
        'powerball.py',
        'gambler.py',
        'game.py',
        'validator_name.py',
        'validator_numbers.py'
    ],

    # metadata for upload to PyPI
    author="Mike Druger",
    author_email="mdruger@yahoo.com",
    description="This is a package submittal",
    license="PSF",
)