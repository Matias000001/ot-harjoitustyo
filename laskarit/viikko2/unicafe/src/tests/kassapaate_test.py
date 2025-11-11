import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)


    def test_luodun_kassapaatteen_rahamaara_ja_myytyjen_lounaiden_määrä_on_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.0)

    def test_kateisosto_toimii_seka_edullisten_etta_maukkaiden_lounaiden_osalta(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)

        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100640)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kateisosto_ei_riittavalla_maksulla_edullinen_etta_maukas_lounas(self):
        vaihtoraha = self.kassa.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)

        vaihtoraha = self.kassa.syo_maukkaasti_kateisella(300)
        self.assertEqual(vaihtoraha, 300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)



    def test_korttiosto_toimii_edullisten_lounaiden_osalta(self):
        onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertTrue(onnistui)
        self.assertEqual(self.kortti.saldo, 760)
        self.assertEqual(self.kassa.edulliset, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkaiden_lounaiden_osalta(self):
        onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertTrue(onnistui)
        self.assertEqual(self.kortti.saldo, 600)
        self.assertEqual(self.kassa.maukkaat, 1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_korttiosto_epaonnistuu_edullisen_lounaan_osalta(self):
        kortti = Maksukortti(200)
        onnistui = self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_korttiosto_epaonnistuu_maukkaan_lounaan_osalta(self):
        kortti = Maksukortti(200)
        onnistui = self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertFalse(onnistui)
        self.assertEqual(kortti.saldo, 200)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 500)
        self.assertEqual(self.kortti.saldo, 1500)
        self.assertEqual(self.kassa.kassassa_rahaa, 100500)

    def test_kortille_ei_voi_ladata_negatiivista_summaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -500)
        self.assertEqual(self.kortti.saldo, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_saldo_euroina(self):
        self.assertEqual(self.kortti.saldo_euroina(), 10.0)