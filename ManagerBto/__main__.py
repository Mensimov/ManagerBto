import glob
from pathlib import Path
from ManagerBto.utils import load_plugins
import logging
from . import klent

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "ManagerBto/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Bot başladı!")
if __name__ == "__main__":
    klent.run_until_disconnected()
