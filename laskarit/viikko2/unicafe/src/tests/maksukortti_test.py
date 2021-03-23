import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_lataus(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(str(self.maksukortti), "saldo: 0.2")
    
    def test_otto(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(str(self.maksukortti), "saldo: 0.05")
    
    def test_otto_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
    
    def test_otto_bool(self):
        boolean = self.maksukortti.ota_rahaa(5)
        self.assertEqual(boolean, True)
    
    def test_otto_ei_mene_negatiiviseksi_bool(self):
        boolean = self.maksukortti.ota_rahaa(20)
        self.assertEqual(boolean, False)