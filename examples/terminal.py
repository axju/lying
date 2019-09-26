from lying.terminal import Terminal
from lying.utils.misc import setup_root_logger


data = [
    {'input': {'cmd': 'ls'}},
    {'input': 'cat hello.txt', 'output': {'text': 'hello :)'}},
    {'input': 'cat hello.txt', 'output': {'sleep': 10}},
    {'input': 'cat hello.txt', 'output': {'title': 'lying'}},
    {'input': 'cat hello.txt', 'output': {'progressbar': None}},
    {'input': 'cat hello.txt', 'output': [
        {'text': 'Create Title'}, {'progressbar': None}, {'title': 'lying'}
    ]},
]
data = [
    {'input': {'cmd': 'ls'}},
]

setup_root_logger(50)

terminal = Terminal(prompt='>>> ', width=50, wait=200)
terminal.load(data=data)
terminal.run()
