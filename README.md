# 🖥️ Linux System Monitor  
> Gerçek zamanlı • Animasyonlu • Gösterişli sistem izleme aracı

<p align="center">
  <img src="https://img.shields.io/badge/Linux-System%20Monitor-black?style=for-the-badge&logo=linux">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Real--Time-Animated-green?style=for-the-badge">
</p>

---

## 🚀 Proje Tanımı

**Linux System Monitor**, Linux sistemlerde  
CPU, bellek, disk ve ağ kullanımını  
**gerçek zamanlı ve animasyonlu grafiklerle** izleyen hafif ama etkili bir sistem izleme uygulamasıdır.

Veriler saniyede bir güncellenir ve grafikler son **50 veri noktası** ile dinamik olarak kaydırılır.

---

## ✨ Özellikler

- 🧠 **CPU Kullanımı** – Anlık CPU kullanım yüzdesi  
- 🧮 **Bellek Kullanımı** – Toplam RAM kullanım oranı  
- 💾 **Disk Kullanımı** – Disk doluluk yüzdesi  
- 🌐 **Ağ Kullanımı** – Gönderilen & alınan veri (MB)  
- 🎥 **Animasyonlu Grafikler**  
- ⏱️ **1 saniyede bir güncelleme**

---

## 📊 İzlenen Kaynaklar

| Kaynak | Açıklama |
|------|---------|
| CPU | Gerçek zamanlı kullanım (%) |
| RAM | Bellek kullanım oranı |
| Disk | Toplam disk doluluk yüzdesi |
| Network | Gönderilen / alınan veri (MB) |

---

## 🧰 Gereksinimler

Aşağıdaki kütüphaneler gereklidir:

- **psutil** – Sistem bilgilerini almak için  
- **matplotlib** – Grafik ve animasyonlar  
- **tkinter** – (Opsiyonel) GUI arayüzü  

### 📦 Kurulum

```bash
pip install psutil matplotlib
```

---

## ▶️ Çalıştırma

Uygulamayı başlatmak için:

```bash
python system_monitor.py
