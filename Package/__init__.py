__author__ = 'aaugustyniak'

# The only solution is for the package author to provide an explicit index of the package. The import statement uses the following convention: if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered. It is up to the package author to keep this list up-to-date when a new version of the package is released. Package authors may also decide not to support it, if they don’t see a use for importing * from their package. For example, the file sound/effects/__init__.py could contain the following code:
#
# __all__ = ["echo", "surround", "reverse"]
# This would mean that from sound.effects import * would import the three named submodules of the sound package.
#
# If __all__ is not defined, the statement from sound.effects import * does not import all submodules from the package sound.effects into the current namespace; it only ensures that the package sound.effects has been imported (possibly running any initialization code in __init__.py) and then imports whatever names are defined in the package. This includes any names defined (and submodules explicitly loaded) by __init__.py. It also includes any submodules of the package that were explicitly loaded by previous import statements. Consider this code:
#
# import sound.effects.echo
# import sound.effects.surround
# from sound.effects import *


# import os
#
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
#
# engine = create_engine(os.environ['DATABASE_URL'])
# Session = sessionmaker(bind=engine)

all__ = ['SubModB']
from SubModA import *
