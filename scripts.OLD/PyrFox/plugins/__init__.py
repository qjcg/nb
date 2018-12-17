import importlib
import os
from glob import iglob

mods = {}
for mod in iglob('plugins/[A-Za-z]*.py'):
    mod = 'plugins.' + os.path.basename(mod).replace('.py', '')
    print(mod)
    mods[mod] = importlib.import_module(mod, package=None)
