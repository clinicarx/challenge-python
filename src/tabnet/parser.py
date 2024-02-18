from collections import namedtuple


Periodo = namedtuple('Periodo', ['inicio', 'fim'])

class TabFile:
    def __init__(self, titulo, subtitulo, rodape, dataframe):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.rodape = rodape
        self.dataframe = dataframe

    def __repr__(self):
        return f'Tipo: {self.titulo}, Subtitulo: {self.subtitulo}, Rodape: {self.rodape}'

    @staticmethod
    def parse(file_name):
        titulo1 = None
        titulo2 = None
        rodape = None
        periodo = None
        dataframe = None

        return TabFile(titulo1, titulo2, periodo, dataframe)

    def sumByYear(self, year):
        total_by_year = None
        return total_by_year
