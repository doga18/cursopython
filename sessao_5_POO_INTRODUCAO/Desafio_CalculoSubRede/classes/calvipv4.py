import re

class CalcIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo

        self._set_broadcast()
        self._set_rede()

    # Getters
    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @property
    def rede(self):
        return self._rede

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def get_numero_ips(self):
        return self._get_numero_ips()

    # Setters
    @ip.setter
    def ip(self, value):
        # self._valida_ip(value)
            if not self._valida_ip(value):
                print(f"Erro ao tentar validar o valor recebido: {value} IP inválido.")

            self._ip = value
            self._ip_bin = self._ip_to_bin(value)
            print()
            print(f'IP {value} Recebido a registrado com sucesso.')
            print()

    @mascara.setter
    def mascara(self, value):
        if not value:
            return

        if not self._valida_ip(value):
            raise ValueError('Máscara Inválida')
        self._mascara = value
        self._mascara_bin = self._ip_to_bin(value)
        if not hasattr(self, 'prefixo'):
            self.prefix = self._mascara_bin.count('1')

    @prefixo.setter
    def prefixo(self, value):
        if not value:
            return

        if not isinstance(value, int):
            raise TypeError('Prefixo precisa ser inteiro')

        if value > 32:
            print(f'Insira um prefixo válido, prefixo informado {value}')

        self._prefixo = value
        self._mascara_bin = (value * '1').ljust(32, '0')
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin)

    @staticmethod
    def _valida_ip(value):
        regex = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regex.search(value):
            return True
        return False

    @staticmethod
    def _ip_to_bin(value):
        blocos = value.split('.')
        blocos_binarios = [bin(int(x))[2:].zfill(8) for x in blocos]
        # print(''.join(blocos_binarios))
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(value):
        n = 8
        blocos = [str(int(value[i:n+i], 2)) for i in range(0, 32, n)]
        # print(blocos)
        return '.'.join(blocos)

    def _set_broadcast(self):
        hosts_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (hosts_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        hosts_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (hosts_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        # print(self._rede)
        return self._rede

    def _get_numero_ips(self):
        calc_1 = 2 ** ((32 - self.prefixo))
        return calc_1 - 2