from time import sleep
from random import randint
from lying.utils.misc import Output


class OutputMixin():

    def __init__(self, conf):
        super().__init__(conf)
        self.output = Output(self.conf.stdout)


class WaitMixin():

    DEFAULT_WAIT = 1000
    DEFAULT_RANDOM = 0.2

    def wait(self):
        if self.conf.fast:
            return
        wait = getattr(self.kwargs, 'wait', self.DEFAULT_WAIT)
        rand = getattr(self.kwargs, 'random', self.DEFAULT_RANDOM)
        dts = round(wait * rand)
        msec = randint(wait-dts, wait+dts)
        self.logger.debug('Wait %i ms', msec)
        sleep(msec/1000)
