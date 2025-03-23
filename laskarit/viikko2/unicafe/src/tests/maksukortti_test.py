import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataa_rahaa(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_ota_rahaa_saldo_riittaa(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 9.0)
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_ota_rahaa_saldo_ei_riita(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

        
