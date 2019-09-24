from lying.utils.instruction import Instruction

data = {'txt': {'text': 'Hallo'}}
data = [{'txt': 'asdasd'}, {'cmd': 'asdasd'}, {'txt': 'asdasd'}]

inst = Instruction()
inst.load(data)
for item in inst:
    print(item)
