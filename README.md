# 🔥 BZX ULTIMATUM v4.1 - DEWA SPEK PREMIUM 🔥

```

╔══════════════════════════════════════════════════════════════════════════════╗
║    ██████╗ ███████╗██╗  ██╗   ██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗██╗   ██╗███╗   ███╗
║    ██╔══██╗██╔════╝╚██╗██╔╝   ██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██║   ██║████╗ ████║
║    ██████╔╝█████╗   ╚███╔╝    ██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   ██║   ██║██╔████╔██║
║    ██╔══██╗██╔══╝   ██╔██╗    ██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
║    ██████╔╝███████╗██╔╝ ██╗██╗╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
║    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
║                                                                                  ║
║                      DDOS ULTIMATUM v4.1 - DEWA SPEK PREMIUM                      ║
║                  FOR EDUCATIONAL PURPOSES ONLY - BZX EDITION                    ║
║                                                                                  ║
║                      ⚡ LAYER 4 & LAYER 7 ATTACKS ⚡                              ║
║                 🔥 15+ ATTACK METHODS | UNLIMITED THREADS 🔥                   ║
║                 💀 REAL-TIME STATS | AUTO PROXY | BYPASS WAF 💀               ║
╚══════════════════════════════════════════════════════════════════════════════╝

```

## 📋 DAFTAR ISI
- [TENTANG TOOL](#tentang-tool)
- [FITUR UTAMA](#fitur-utama)
- [DISCLAIMER PENTING](#disclaimer-penting)
- [INSTALASI](#instalasi)
- [CARPAKAI](#carpakai)
- [ATTACK METHODS](#attack-methods)
- [AUTO PROXY](#auto-proxy)
- [CONFIGURATION](#configuration)
- [TROUBLESHOOTING](#troubleshooting)
- [LICENSE](#license)

## ⚡ TENTANG TOOL

**BZX ULTIMATUM** adalah tool penetration testing untuk simulasi DDoS attack dengan **15+ metode serangan** mencakup Layer 4 dan Layer 7. Dilengkapi dengan **Auto Proxy Manager** yang otomatis fetch proxy dari berbagai sumber.

### 🎯 Tujuan:
- ✅ Penetration Testing
- ✅ Keamanan Jaringan
- ✅ Educational Purpose
- ✅ Stress Testing Server Sendiri

## 🔥 FITUR UTAMA

| No | Fitur | Keterangan |
|----|-------|------------|
| 1 | **Layer 4 Attacks** | UDP Flood, SYN Flood, ICMP Flood |
| 2 | **Layer 7 Attacks** | HTTP Flood, HTTPS Flood, POST Flood, Slowloris |
| 3 | **Advanced Attacks** | Random Path, WAF Bypass, Mixed Mode |
| 4 | **Auto Proxy Manager** | Fetch otomatis dari 10+ sumber proxy |
| 5 | **Proxy Tester** | Test dan filter proxy yang hidup |
| 6 | **Multi-threading** | Support hingga 9999 thread |
| 7 | **Real-time Stats** | Packets, bandwidth, speed, failed attempts |
| 8 | **Custom Delay/PPS** | Atur kecepatan serangan |
| 9 | **WAF Bypass** | Header random, IP spoofing, encoding |
| 10 | **Cross Platform** | Linux, Termux, Windows (WSL) |

## ⚠️ DISCLAIMER PENTING

```diff
- [!] TOOL INI HANYA UNTUK TUJUAN PENDIDIKAN DAN PENETRATION TESTING!
- [!] DILARANG KERAS DIGUNAKAN UNTUK SERANGAN ILEGAL!
- [!] HANYA BOLEH DIGUNAKAN DI SERVER SENDIRI / LAB!
- [!] MELANGGAR UU ITE = PIDANA PENJARA (Pasal 30-36)!
- [!] DEVELOPER TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN!
```

Dengan menggunakan tool ini, Anda menyetujui disclaimer di atas.

📦 INSTALASI

✅ Persyaratan

· Python 3.6+
· Pip
· Koneksi internet (untuk auto proxy)

📥 Install Dependencies

```bash
# Clone repo
git clone https://github.com/bzdev1/bzx-ultimatum.git
cd bzx-ultimatum

# Install requirements
pip install -r requirements.txt

# Jalankan
python3 bzx_ultimatum_v41.py
```

📱 Termux (Android)

```bash
pkg update && pkg upgrade -y
pkg install python git -y
git clone https://github.com/bzdev1/bzx-ultimatum.git
cd bzx-ultimatum
pip install -r requirements.txt
python bzx_ultimatum_v41.py
```

🖥️ VPS/Cloud Server

```bash
apt update && apt upgrade -y
apt install python3 python3-pip git -y
git clone https://github.com/bzdev1/bzx-ultimatum.git
cd bzx-ultimatum
pip3 install -r requirements.txt
python3 bzx_ultimatum_v41.py
```

🚀 CARPAKAI

Menu Utama

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                            BZX ULTIMATUM v4.1 - MENU UTAMA                         │
├──────────────────────────────────────────────────────────────────────────────────┤
│  1. Set Target (IP/URL)                  8. Layer 7 - HTTP Flood                  │
│  2. Set Port (default: 80)                9. Layer 7 - HTTPS Flood                │
│  3. Set Threads (1-9999)                 10. Layer 7 - Slowloris                  │
│  4. Set Duration (detik)                  11. Layer 7 - POST Flood                │
│  5. Set Delay/PPS                         12. Layer 7 - Random Path               │
│  6. AUTO PROXY MANAGER                    13. Layer 7 - WAF Bypass Mode           │
│  7. Layer 4 - UDP Flood                   14. MIXED MODE - All Attacks            │
├──────────────────────────────────────────────────────────────────────────────────┤
│ 15. Layer 4 - SYN Flood                   16. Layer 4 - ICMP Flood                │
│ 17. Show Current Config                   18. 🔥 START ULTIMATUM 🔥                │
│ 19. Stop Attack                            0. Exit                                │
└──────────────────────────────────────────────────────────────────────────────────┘
```

Langkah Cepat

```bash
# 1. Set target
Pilih menu 1 → masukkan IP/URL

# 2. Atur proxy (opsional tapi recommended)
Pilih menu 6 → 3 (Fetch + Test) → 6 (Toggle ON)

# 3. Pilih metode serangan
Pilih menu 7-16 sesuai kebutuhan

# 4. START!
Pilih menu 18
```

⚔️ ATTACK METHODS

Layer 4 Attacks (Network Layer)

Method Port Description
UDP Flood Any Mengirim UDP packet random, membanjiri bandwidth
SYN Flood TCP Membuka koneksi TCP tanpa completing handshake
ICMP Flood - Ping flood, menghabiskan CPU target

Layer 7 Attacks (Application Layer)

Method Target Description
HTTP Flood Port 80/443 GET request dengan random user-agent
HTTPS Flood Port 443 HTTP Flood dengan SSL
POST Flood Port 80/443 POST request dengan random data
Slowloris Port 80/443 Keep connections open, habiskan koneksi
Random Path Port 80/443 Request ke random path (contoh: /wp-admin, /api)
WAF Bypass Port 80/443 Bypass WAF dengan header spoofing

Advanced Mode

Method Description
MIXED MODE Random attack setiap thread (UDP/HTTP/POST/dll)

🧦 AUTO PROXY

Fitur Auto Proxy Manager:

· ✅ Fetch dari 10+ sumber proxy (ProxyScrape, GitHub, dll)
· ✅ Auto test proxy yang hidup
· ✅ Live proxy pool
· ✅ Auto refresh jika proxy habis
· ✅ Statistik lengkap
· ✅ Simpan/load ke file

Cara Pakai Auto Proxy:

```
1. Pilih menu 6 (AUTO PROXY MANAGER)
2. Pilih menu 3 (Fetch + Test Sekaligus)
3. Tunggu sampai selesai (biasanya dapet 50-200 proxy hidup)
4. Pilih menu 6 (Toggle Proxy) untuk mengaktifkan
5. Selesai!
```

Menu Auto Proxy:

```
══════════════════════════════════════════════════════════
                    AUTO PROXY MANAGER
══════════════════════════════════════════════════════════
1. Fetch Proxy dari Internet
2. Test Semua Proxy (cari yang hidup)
3. Fetch + Test Sekaligus
4. Simpan ke File (proxies.txt)
5. Load dari File
6. Toggle Proxy (current: OFF)
7. Auto Refresh (current: ON)
8. Lihat Statistik Proxy
9. Hapus Semua Proxy
0. Kembali
══════════════════════════════════════════════════════════
```

⚙️ CONFIGURATION

Settings yang bisa diatur:

Setting Range Default Keterangan
Threads 1-9999 100 Jumlah thread parallel
Duration 1-∞ 60 detik Lama serangan
Delay 0-1 0.001 Delay antar packet (pps)
Packet Size 64-65507 1024 Ukuran packet (UDP/ICMP)
Port 1-65535 80 Port target
Proxy ON/OFF OFF Gunakan proxy
Auto Refresh ON/OFF ON Auto refresh proxy

📂 STRUKTUR FILE

```
bzx-ultimatum/
├── bzx_ultimatum_v41.py    # Main tool
├── requirements.txt         # Dependencies
├── README.md               # Dokumentasi
├── LICENSE                 # MIT License
└── proxies.txt             # Auto generated (proxy list)
```

🔧 DEPENDENCIES

File requirements.txt:

```txt
requests>=2.28.0
colorama>=0.4.6
```

📊 REAL-TIME STATS

Saat attack berjalan, akan tampil:

```
[🔥] ATTACK RUNNING - 45s remaining
Packets: 15234 | Speed: 338 pps
Bandwidth: 1.24 MB/s | Total: 55.67 MB
Failed: 23
```

🧠 TIPS & TRIK

Tips Keterangan
🚀 Thread 200-500 Optimal untuk Layer 4
🌐 Thread 50-100 Optimal untuk Layer 7 (biar gak timeout)
🧦 Proxy WAJIB Untuk Layer 7 biar IP gak kena banned
🔄 Auto Refresh ON Biar proxy gak habis
⏱️ Delay 0 Max speed, tapi bisa bikin stabilo
🛡️ WAF Bypass Gunakan menu 13 untuk site pake CloudFlare
🎯 Mixed Mode Susah dideteksi karena random attack

❗ TROUBLESHOOTING

Masalah Solusi
ModuleNotFoundError pip install -r requirements.txt
Proxy mati semua Fetch ulang (menu 6 → 3)
Kena rate limit Naikin delay, turunin thread
SSL Error Tool pake verify=False, aman
Slowloris gagal Turunin thread, naikin delay
WAF bypass gagal Coba pake proxy residential
Connection refused Target mungkin down atau block IP

🔄 UPDATE

```bash
cd ~/bzx-ultimatum
git pull origin main
pip install -r requirements.txt --upgrade
```

📜 LICENSE

MIT License - Bebas dimodifikasi dan didistribusikan.

🗿 CREATOR

```
Author  : bzdev1 / Bzx
GitHub  : https://github.com/bzdev1/bzx-ultimatum
```

Dibuat dengan ☕, 🍺, dan amarah.

⭐ SUPPORT

· ⭐ Star repo ini di GitHub
· 🍴 Fork kalau mau modifikasi
· 🐛 Report issue kalau nemu bug
· 💀 Jangan lupa jadi hacker yang bijak

---

```
╔══════════════════════════════════════════════════════════════════════════════╗
║  © 2026 bzdev1 - BZX ULTIMATUM v4.1 - Dewa Spek Premium                     ║
║  "Hanya untuk pendidikan, jangan jadi bego"                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

