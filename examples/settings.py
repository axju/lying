from lying.utils import Settings
from lying.utils.misc import setup_root_logger

setup_root_logger()

settings = Settings(prompt='Hallo')
print(settings.prompt)
print(settings['prompt'])
