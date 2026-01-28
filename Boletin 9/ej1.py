class Libro:
    def __init__(self, titulo, autor, ano, numPaginas, valoracion):
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_ano(ano)
        self.set_numPaginas(numPaginas)
        self.set_valoracion(valoracion)


    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano

    def get_numPaginas(self):
        return self.__numPaginas

    def get_valoracion(self):
        return self.__valoracion


    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_autor(self, autor):
        self.__autor = autor

    def set_ano(self, ano):
        self.__ano = ano

    def set_numPaginas(self, numPaginas):
        self.__numPaginas = numPaginas

    def set_valoracion(self, valoracion):
        self.__valoracion = valoracion


    titulo = property(get_titulo, set_titulo)
    autor = property(get_autor, set_autor)
    ano = property(get_ano, set_ano)
    numPaginas = property(get_numPaginas, set_numPaginas)
    valoracion = property(get_valoracion, set_valoracion)


    def amosarLibro(self):
        return (
            f"Título: {self.__titulo}\n"
            f"Autor: {self.__autor}\n"
            f"Año: {self.__ano}\n"
            f"Número de páxinas: {self.__numPaginas}\n"
            f"Valoración: {self.__valoracion}/5"
        )


class Principal:
    def main():
        libro1 = Libro("Los picapiedra", "Laidai", 1985, 1417, 5)
        libro2 = Libro("Naruto", "Hermo", 2009, 5000, 8.5)

        print("Información do libro 1:")
        print(libro1.amosarLibro())
        print("\nInformación do libro 2:")
        print(libro2.amosarLibro())



if __name__ == "__main__":
    Principal.main()