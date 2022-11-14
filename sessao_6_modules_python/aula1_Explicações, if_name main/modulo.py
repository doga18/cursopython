def soma(x: float, y: float) -> float:
    return x + y

# A técnica abaixo, serve para poder testar arquivos Py, sem afetar a produção, rodando somente se esse arquivo for
# executado.


def main() -> None:
    print(__name__)
    print(soma(1, 2))
    print(soma(3, 1))


if __name__ == "__main__":
    # print(__name__)
    # print(soma(1, 2))
    # print(soma(3, 1))
    main()