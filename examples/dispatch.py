from lying.utils.dispatch import Dispatchers

dispatcher = Dispatchers()
print(dict(dispatcher))
for name, cls in dispatcher:
    print(name, dispatcher[name, 'kwargs'])

print(dispatcher.defaults())
print(dispatcher.defaults())
print(dispatcher.defaults())
print(dispatcher.defaults())
