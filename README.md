# epttavm-api-python-client
Unofficial ePttAVM Python Client

## Kurulum

```sh
pip3 install epttavm-api-python-client
```

## Kullanım
```sh
from epttavm_sdk.api import EPttAVMApiClient
api = EPttAVMApiClient(api_key="<EPTTAVM_API_KEY>", api_secret="<EPTTAVM_API_SECRET>")
# Urun kontrol
product = api.barkod_kontrol(shop_id="<SHOP_ID>", barkod="<BARKOD>")
# Urun Yukleme
from epttavm_sdk.objects import VariantAttr, UrunResim, Variant, ProductItem
urun_resim_list = [UrunResim(url="http://img.epttavm.com/prodotti/592/019/752/19752454_0.jpg", sira=1)]
variant_list = [
    Variant(ana_urun_kodu="123456ex", durum="Yeni", kayit_degisti=1, miktar=2, variant_barkod="123456ex-4780", attributes=[VariantAttr(deger="BYZ-YEŞİL", fiyat=0, fiyat_farki_mi=False, tanim="Renk"), VariantAttr(deger="XXL", fiyat_farki_mi=True, fiyat=28, tanim="Beden")], guncelleme_sonucu=None)
]
product_item = ProductItem(aciklama="", aktif=True, yeni_kategori_id=763, barkod="123456ex", desi=0.5, durum="Yeni", garanti_suresi=0, garanti_veren_firma=None, iskonto=0, kdv_oran=18, kdvsiz=55.56, kategori_bilgisini_guncelle=0, mevcut=True, miktar=2, shop_id=1111, tag="top,futbol,spor", tedarikci_alt_kategori_adi=None, tedarikci_alt_kategori_id=0, tedarikci_sanal_kategori_id=0, urun_adi="Futbol Topu", urun_id=0, uzun_aciklama="Örnek Kod", urun_url=None, urun_resimleri=urun_resim_list, variant_listesi=variant_list)
api.stok_guncelle_v2(product_item=product_item)
```