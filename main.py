import requests
import time
import concurrent.futures
from colorama import Fore, Style, init

# Initialize Colorama for cool terminal colors
init(autoreset=True)

class OSINTTracer:
    def __init__(self):
        self.banner()
        self.target = ""
        self.websites = {
            "Instagram": "https://www.instagram.com/{}",
            "Facebook": "https://www.facebook.com/{}",
            "Twitter": "https://twitter.com/{}",
            "GitHub": "https://github.com/{}",
            "Reddit": "https://www.reddit.com/user/{}",
            "TikTok": "https://www.tiktok.com/@{}",
            "Pinterest": "https://www.pinterest.com/{}",
            "Steam": "https://steamcommunity.com/id/{}",
            "Telegram": "https://t.me/{}",
            "Medium": "https://medium.com/@{}"
        }

    def banner(self):
        print(Fore.RED + Style.BRIGHT + """
   ____  _____ ___ _   _ _____   _____ ____      _    ____ _____ ____  
  / __ \| ____|_ _| \ | |_   _| |_   _|  _ \    / \  / ___| ____|  _ \ 
 | |  | |  _|  | ||  \| | | |     | | | |_) |  / _ \| |   |  _| | |_) |
 | |__| | |___ | || |\  | | |     | | |  _ <  / ___ \ |___| |___|  _ < 
  \____/|_____|___|_| \_| |_|     |_| |_| \_\/_/   \_\____|_____|_| \_\\
                                                    v1.0.0 | @devnand-47
              https://github.com/devnand-47/devnand-47/blob/main/README.md
        """ + Style.RESET_ALL)

    def check_site(self, site, url):
        """Checks a single website for the username"""
        formatted_url = url.format(self.target)
        try:
            response = requests.get(formatted_url, timeout=5)
            if response.status_code == 200:
                print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.GREEN}FOUND{Style.RESET_ALL}: {site} -> {formatted_url}")
            elif response.status_code == 404:
                # 404 usually means not found, but we hide it to keep output clean
                pass 
            else:
                print(f"[{Fore.YELLOW}?{Style.RESET_ALL}] {Fore.YELLOW}ERROR{Style.RESET_ALL}: {site} (Status: {response.status_code})")
        except Exception:
            pass # Connection errors are ignored for speed

    def run(self):
        self.target = input(f"[{Fore.RED}>{Style.RESET_ALL}] Enter Username to Trace: ")
        print(f"\n[{Fore.CYAN}*{Style.RESET_ALL}] Initializing Search Threads for: {Fore.RED}{self.target}{Style.RESET_ALL}...\n")
        
        # Using ThreadPoolExecutor for fast, concurrent scanning
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(self.check_site, site, url) for site, url in self.websites.items()]
            concurrent.futures.wait(futures)
        
        print(f"\n[{Fore.CYAN}*{Style.RESET_ALL}] Scan Complete.")

if __name__ == "__main__":
    app = OSINTTracer()
    app.run()