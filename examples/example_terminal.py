from io import StringIO
from lying.utils import Terminal


cmds = [
    {'input': 'ls'},
    {'input': 'cat hello.txt', 'output': {'text': 'hello :)'}},
    {'input': 'cat hello.txt', 'output': {'sleep': 10}},
    {'input': 'cat hello.txt', 'output': {'title': 'lying'}},
    {'input': 'cat hello.txt', 'output': {'progressbar': None}},
    {'input': 'cat hello.txt', 'output': [{'text': 'Create Title'},{'progressbar': None}, {'title': 'lying'}]},
]
terminal = Terminal(cmds=[{'input': 'cat hello.txt', 'output': {'title': 'lying'}},], prompt='>>> ', width=50, wait=0)
terminal.run()
