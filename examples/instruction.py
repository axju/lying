from lying.utils.instruction import Instruction

inst = Instruction({'input': ('cmd', str), 'txt': ('text', str)})

data = ('txt', {'text': 'Hallo'})
inst.load(data)
data = [('txt', {'text': 'Hallo'}), ('txt', {'text': 'Hallo'})]
inst.load(data)
data = ('txt', 'Hallo')
inst.load(data)
data = [('input', 'test'), ('txt', 'Hallo')]
inst.load(data)
data = [('input', 'test'), ('txt', {'text': 'Hallo'})]
inst.load(data)
data = [['input', 'test'], ['txt', {'text': 'Hallo'}]]
inst.load(data, format='list')


for item in inst:
    print(item)
