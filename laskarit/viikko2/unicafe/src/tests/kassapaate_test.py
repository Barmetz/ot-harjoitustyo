import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(500)
    
    def test_pohjustus_raha(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_pohjustus_lounaat(self):
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_kateis_edullinen(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
    
    def test_kateis_edullinen_vaihto(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)
    
    def test_kateis_edullinen_myydyt(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_kateis_edullinen_fail(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(vaihto, 200)

    def test_kateis_maukkas(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_kateis_maukas_vaihto(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto, 100)
    
    def test_kateis_maukas_myydyt(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kateis_maukas_fail(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(vaihto, 200)    
    
    def test_edullinen_kortti(self):
        vastaus = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 260)
        self.assertEqual(vastaus, True)
    
    def test_edullinen_kortti_myydyt(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_edullinen_kortti_fail(self):
        kortti = Maksukortti(200)
        vastaus = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(vastaus, False)

    def test_edullinen_kortti_kassa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_maukkaat_kortti(self):
        vastaus = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)
        self.assertEqual(vastaus, True)
    
    def test_maukkaat_kortti_myydyyt(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_maukkaat_kortti_fail(self):
        kortti = Maksukortti(200)
        vastaus = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(vastaus, False)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_maukkaat_kortti_kassa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortti_lataus(self):
        self.kassa.lataa_rahaa_kortille(self.kortti,200)
        self.assertEqual(self.kortti.saldo, 700)
        self.assertEqual(self.kassa.kassassa_rahaa, 100200)

    def test_kortti_lataus_negatiivinen(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kortti.saldo, 500)
        