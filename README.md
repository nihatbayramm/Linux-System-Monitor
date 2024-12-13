# Linux System Monitor

Bu proje, Linux sisteminin temel kaynaklarını izleyen bir araçtır. Kullanıcılar, CPU, bellek, disk ve ağ kullanımını görsel grafiklerle takip edebilirler. Program, bu verileri gerçek zamanlı olarak toplar ve animasyonlu grafiklerde gösterir.

## Özellikler

- **CPU Kullanımı**: Gerçek zamanlı CPU kullanım yüzdesi.
- **Bellek Kullanımı**: Sistemdeki toplam bellek kullanım oranı.
- **Disk Kullanımı**: Diskteki toplam kullanım oranı.
- **Ağ Kullanımı**: Gönderilen ve alınan ağ verisi miktarı (MB cinsinden).

Veriler, her saniye güncellenir ve grafikler, son 50 veri noktasıyla güncel tutulur. Yüzde değerleri, her grafik üzerine eklenir.

## Gereksinimler

Proje çalıştırmak için aşağıdaki kütüphanelerin yüklü olması gerekmektedir:

- **psutil**: Sistem bilgilerini toplamak için.
- **matplotlib**: Verilerin görselleştirilmesi için.
- **tkinter**: GUI arayüzü (bu proje için opsiyonel).

Aşağıdaki komutla gerekli kütüphaneleri yükleyebilirsiniz:

```bash
pip install psutil matplotlib
