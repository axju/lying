from lying.utils.dispatch import Dispatchers
from lying.utils.misc import setup_root_logger


setup_root_logger()


dispatcher = Dispatchers()
print(dict(dispatcher))
for name, cls in dispatcher:
    print(name, dispatcher[name, 'kwargs'])
