import unittest
from src.tabnet import TabFile

class TestTabnetParser(unittest.TestCase):
    def test_parser_metadata(self):
        file_name = 'lib/idb2012.tab'
        tab_file = TabFile.parse(file_name)

        self.assertEqual("A.1 População Total", tab_file.titulo)
        self.assertEqual("População por Ano segundo Capital", tab_file.subtitulo)
        self.assertTupleEqual(('1990', '2012'), tuple(tab_file.rodape))

    def test_parser_group_by_year(self):
        file_name = 'lib/idb2012.tab'
        tab_file = TabFile.parse(file_name)

        self.assertEqual(69370416, tab_file.sumByYear(1990))
        self.assertEqual(80924144, tab_file.sumByYear(2000))
        self.assertEqual(92453380, tab_file.sumByYear(2012))
