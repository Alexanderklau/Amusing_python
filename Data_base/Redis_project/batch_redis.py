# coding: utf-8
__author__ = 'lau.wenbo'


class Token(object):
    def __init__(self, value):
        if isinstance(value, Token):
            value = value.value
            self.value = value

    def __repr__(self):
        return self.value


    def __str__(self):
        return self.value

def b(x):
    return x


SYM_STAR = b('*')
SYM_DOLLAR = b('$')
SYM_CRLF = b('\r\n')
SYM_EMPTY = b('')

class RedisProto(object):
    def __init__(self, encoding='utf-8', encoding_errors='strict'):
        self.encoding = encoding
        self.encoding_errors = encoding_errors

    def pack_command(self, *args):
        """将redis命令安装redis的协议编码,返回编码后的数组,如果命令很大,返回的是编码后chunk的数组"""

        output = []
        command = args[0]
        if ' ' in command:
            args = tuple([Token(s) for s in command.split(' ')]) + args[1:]
        else:
            args = (Token(command),) + args[1:]
        buff = SYM_EMPTY.join((SYM_STAR, b(str(len(args))), SYM_CRLF))

        for arg in map(self.encode,args):
            if len(buff) > 6000 or len(arg) > 6000:
                buff = SYM_EMPTY.join((buff, SYM_DOLLAR, b(str(len(arg))), SYM_CRLF))
                output.append(buff)
                output.append(arg)
                buff = SYM_CRLF
            else:
                buff = SYM_EMPTY.join((buff, SYM_DOLLAR, b(str(len(arg))), SYM_CRLF, arg, SYM_CRLF))
        output.append(buff)
        return output

    def encode(self, value):
        if isinstance(value, Token):
            return b(value.value)
        elif isinstance(value, bytes):
            return value
        elif isinstance(value,int):
            value = b(str(value))
        elif not isinstance(value, str):
            value = str(value)
        if isinstance(value, str):
            value = value.encode(self.encoding, self.encoding_errors)
        return value

if __name__ == '__main__':
    """ python redis_insert.py | redis-cli --pipe """

    commands_args = [('SET', 'Hello', 'World'), ('Set', 'Country', '{"name": 中国"}'),
                     ('HSET', 'Key', 'Name', 'Python'),
                     ('HMSET', 'user', 'name', 'Rsj217', 'Age', '21')]

    commands = ''.join([RedisProto().pack_command(*args)[0] for args in commands_args])
    print commands



