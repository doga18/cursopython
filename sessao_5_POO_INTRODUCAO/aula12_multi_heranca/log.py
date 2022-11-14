# Exemplo de como criar um mixin
class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'info: {msg}')

    def log_error(self, msg):
        self.write(f'error: {msg}')