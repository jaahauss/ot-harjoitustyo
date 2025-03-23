import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassassa_rahaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassassa_rahaa_euroina_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_lounaita_ei_myyty(self):
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat, 0)

    def test_osta_edullisesti_kateisella(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_osta_edullisesti_kateisella_maksu_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_osta_maukkaasti_kateisella(self):
        self.kassapaate.syo_maukkaasti_kateisella(450)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_osta_maukkaasti_kateisella_maksu_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_osta_edullisesti_kortilla(self):
        onnistuminen = self.kassapaate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(onnistuminen, True)
        self.assertEqual(self.kortti.saldo_euroina(), 7.6)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_osta_edullisesti_kortilla_ei_rahaa(self):
        kortti = Maksukortti(100)
        onnistuminen = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(onnistuminen, False)
        self.assertEqual(kortti.saldo_euroina(), 1.0)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_osta_maukkaasti_kortilla(self):
        onnistuminen = self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(onnistuminen, True)
        self.assertEqual(self.kortti.saldo_euroina(), 6.0)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_osta_maukkaasti_kortilla_ei_rahaa(self):
        kortti = Maksukortti(100)
        onnistuminen = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(onnistuminen, False)
        self.assertEqual(kortti.saldo_euroina(), 1.0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_lataa_rahaa_kortille(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
        self.assertEqual(self.kortti.saldo_euroina(), 20.0)
    
    def test_lataa_rahaa_kortille_negatiivinen(self):
    	self.kassapaate.lataa_rahaa_kortille(self.kortti, -1000)
    	self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    	self.assertEqual(self.kortti.saldo_euroina(), 10.0)

