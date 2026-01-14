
class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def converter(self, data):
        raise NotImplemented()

    def process(self):
        while data := self.reader.readline():
            self.writer.write(self.converter(data))


class UpperCase(Processor):
    def converter(self, data):
        return data.upper()


if __name__ == '__main__':
    import sys
    obj = UpperCase(open("streams.txt"), sys.stdout)
    obj.process()
