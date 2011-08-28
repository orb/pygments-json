from setuptools import setup, find_packages
setup(
    name = "pygments-json",
    version = "0.1",
    packages = ['pygson',],
    install_requires = ['Pygments'],
    author = "Norman Richards",
    author_email = "orb@nostacktrace.com",
    description = "Pygments JSON formatter",

    entry_points={
          'pygments.lexers': ['release = pygson.json_lexer:JSONLexer', ]
    },
    
)