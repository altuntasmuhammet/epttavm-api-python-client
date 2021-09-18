from zeep import Client, Settings
from zeep.wsse.username import UsernameToken
from zeep.helpers import serialize_object
from epttavm_sdk.objects import ProductItem


class EPttAVMClient:
    BASE_URL = "https://ws.pttavm.com:93/service.svc/service?wsdl"
    CLIENT_SETTINGS = Settings(
        strict=False, xml_huge_tree=True, xsd_ignore_sequence_order=True)

    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self._client = Client(self.BASE_URL, wsse=UsernameToken(
            self.api_key, self.api_secret), settings=self.CLIENT_SETTINGS)
        self._service = self._client.service

    def barkod_kontrol(self, shop_id, barkod):
        response = serialize_object(
            self._service.BarkodKontrol(ShopId=shop_id, Barkod=barkod))
        if not response['UrunId'] == 0:
            return response
        else:
            return None

    def ana_kategori_listesi(self):
        response = serialize_object(self._service.GetMainCategories())
        return response['main_category']['category']

    def kategori_detayi(self, kategori_id):
        response = serialize_object(self._service.GetCategory(id=kategori_id))
        if response['category']['id']:
            return response['category']

    def kategori_agaci(self, kategori_id):
        response = serialize_object(
            self._service.GetCategoryTree(parent_id=kategori_id))
        return response['category_tree']['Category']

    def siparis_kontrol_listesi_v2(self, baslangic_tarihi: str, bitis_tarihi: str, aktif_siparisler: int):
        response = serialize_object(self._service.GetCategoryTree(
            BaslangicTarihi=baslangic_tarihi, BitisTarihi=bitis_tarihi, aktif_siparisler=aktif_siparisler))
        return response

    def stok_guncelle_v2(self, product_item: ProductItem):
        response = serialize_object(
            self._service.GetCategoryTree(product_item.as_request_param()))
        return response

    def stok_fiyat_guncelle_v3(self, shop_id, barkod, fiyat=None, miktar=None, kdv_oran=None, iskonto=None):
        data = {}
        if fiyat:
            data['Fiyat'] = fiyat
        if miktar:
            data['Miktar'] = miktar
        if kdv_oran:
            data['KDVOran'] = kdv_oran
        if iskonto:
            data['Iskonto'] = iskonto
        if data:
            response = serialize_object(self._service.GetCategoryTree(
                shop_id=shop_id, barkod=barkod, **data))
            return response

    def stok_kontrol_listesi(self, shop_id, search_kategori_id=None, search_alt_kategori_id=None, 
            search_urun_adi=None, search_barkod=None, search_aktif_pasif=None, search_mevcut=None):
        data = {
            "ShopId": shop_id
        }
        if search_kategori_id:
            data['SearchKategoriId'] = search_kategori_id
        if search_alt_kategori_id:
            data['SearchAltKategoriId'] = search_alt_kategori_id
        if search_urun_adi:
            data['SearchUrunAdi'] = search_urun_adi
        if search_barkod:
            data['SearchBarkod'] = search_barkod
        if search_aktif_pasif:
            data['SearchAktifPasif'] = search_aktif_pasif
        if search_mevcut:
            data['SearchMevcut'] = search_mevcut
        response = serialize_object(
            self._service.StokKontrolListesi(**data))
        return response