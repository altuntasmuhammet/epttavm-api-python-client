from typing import List


class VariantAttr(dict):

    def __init__(self, deger, tanim, fiyat, fiyat_farki_mi):
        self.deger = deger
        self.tanim = tanim
        self.fiyat = fiyat
        self.fiyat_farki_mi = fiyat_farki_mi

    def as_request_param(self):
        return {
            'Deger': self.deger,
            'Tanim': self.tanim,
            'Fiyat': self.fiyat,
            'FiyatFarkiMi': self.fiyat_farki_mi
        }


class UrunResim(dict):

    def __init__(self, url, sira):
        self.url = url
        self.sira = sira

    def as_request_param(self):
        return {
            'Url': self.url,
            'Sira': self.sira
        }


class Variant(dict):

    def __init__(self, ana_urun_kodu, durum, guncelleme_sonucu, kayit_degisti,
                 miktar, variant_barkod, attributes: List[VariantAttr]):
        self.ana_urun_kodu = ana_urun_kodu
        self.durum = durum
        self.guncelleme_sonucu = guncelleme_sonucu
        self.kayit_degisti = kayit_degisti
        self.miktar = miktar
        self.variant_barkod = variant_barkod
        self.attributes = attributes

    def as_request_param(self):
        return {
            'AnaUrunKodu': self.ana_urun_kodu,
            'Durum': self.durum,
            'GuncellemeSonucu': self.guncelleme_sonucu,
            'KayitDegisti': self.kayit_degisti,
            'Miktar': self.miktar,
            'VariantBarkod': self.variant_barkod,
            'Attributes': {"VariantAttr": [x.as_request_param() for x in self.attributes]}
        }


class ProductItem(dict):

    def __init__(self, aciklama, aktif, yeni_kategori_id, barkod,
                 desi, durum, garanti_suresi, garanti_veren_firma, iskonto,
                 kdv_oran, kdvli, kategori_bilgisini_guncelle, mevcut, miktar,
                 shop_id, tag, tedarikci_alt_kategori_adi, tedarikci_alt_kategori_id,
                 tedarikci_sanal_kategori_id, urun_adi, urun_id, uzun_aciklama,
                 urun_url, urun_resimleri: List[UrunResim], variant_listesi: List[Variant]):
        self.aciklama = aciklama
        self.aktif = aktif
        self.yeni_kategori_id = yeni_kategori_id
        self.barkod = barkod
        self.desi = desi
        self.durum = durum
        self.garanti_suresi = garanti_suresi
        self.garanti_veren_firma = garanti_veren_firma
        self.iskonto = iskonto
        self.kdv_oran = kdv_oran
        self.kdvli = kdvli
        self.kategori_bilgisini_guncelle = kategori_bilgisini_guncelle
        self.mevcut = mevcut
        self.miktar = miktar
        self.shop_id = shop_id
        self.tag = tag
        self.tedarikci_alt_kategori_adi = tedarikci_alt_kategori_adi
        self.tedarikci_alt_kategori_id = tedarikci_alt_kategori_id
        self.tedarikci_sanal_kategori_id = tedarikci_sanal_kategori_id
        self.urun_adi = urun_adi
        self.urun_id = urun_id
        self.uzun_aciklama = uzun_aciklama
        self.urun_url = urun_url
        self.urun_resimleri = urun_resimleri
        self.variant_listesi = variant_listesi

    def as_request_param(self):
        return {
            'Aciklama': self.aciklama,
            'Aktif': self.aktif,
            'Desi': self.desi,
            'Durum': self.durum,
            'GarantiSuresi': self.garanti_suresi,
            'GarantiVerenFirma': self.garanti_veren_firma,
            'Iskonto': self.iskonto,
            'KDVOran': self.kdv_oran,
            'KDVli': self.kdvli,
            'KategoriBilgisiGuncelle': self.kategori_bilgisini_guncelle,
            'Mevcut': self.mevcut,
            'Miktar': self.miktar,
            'ShopId': self.shop_id,
            'Tag': self.tag,
            'TedarikciAltKategoriAdi': self.tedarikci_alt_kategori_adi,
            'TedarikciAltKategoriId': self.tedarikci_alt_kategori_id,
            'TedarikciSanalKategoriId': self.tedarikci_sanal_kategori_id,
            'UrunAdi': self.urun_adi,
            'UrunId': self.urun_id,
            'UzunAciklama': self.uzun_aciklama,
            'UrunUrl': self.urun_url,
            'UrunResimleri': {"UrunResim": [x.as_request_param() for x in self.urun_resimleri]},
            'VariantListesi': {"Variant": [x.as_request_param() for x in self.variant_listesi]}
        }
