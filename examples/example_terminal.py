#from io import StringIO
from lying.utils import Terminal


data = [
    {'input': 'ls', 'cls': 'txt', 'kwargs': {'text': 'asdsadasdasd'}},
    {'input': 'cat hello.txt', 'output': {'text': 'hello :)'}},
    {'input': 'cat hello.txt', 'output': {'sleep': 10}},
    {'input': 'cat hello.txt', 'output': {'title': 'lying'}},
    {'input': 'cat hello.txt', 'output': {'progressbar': None}},
    {'input': 'cat hello.txt', 'output': [{'text': 'Create Title'},{'progressbar': None}, {'title': 'lying'}]},
]
terminal = Terminal(prompt='>>> ', width=50, wait=0)
terminal.load(data=data)
terminal.load(data=data)
terminal.run()
