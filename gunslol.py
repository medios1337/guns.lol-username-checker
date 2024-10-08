import requests
import random
import string
import time

# Renk kodları tanımları
RED = '\033[91m'
GREEN = '\033[92m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

def random_letters(n):
    """Rastgele harflerden oluşan bir string oluşturur."""
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))

def check_user_status(letter_count, interval):
    """Kullanıcının belirlediği harf sayısı ve aralık ile kullanıcı durumunu kontrol eder."""
    base_url = "guns.lol/"
    while True:
        # Rastgele harf sayısına göre URL oluştur
        random_suffix = random_letters(letter_count)
        url = base_url + random_suffix

        try:
            # Web sitesine istek gönder
            response = requests.get(f"https://{url}")

            if "This user is not claimed" in response.text:
                status = f"{GREEN}unclaimed{RESET}"
            else:
                status = f"{RED}claimed{RESET}"

            # URL'yi mor renkte ve diğer kısmı varsayılan renkte yazdır
            print(f"URL: {MAGENTA}{base_url}{RESET}{random_suffix} - Status: {status}")

        except Exception as e:
            print(f"Error accessing https://{url}: {e}")

        # Kullanıcının belirlediği saniye aralığına göre bekle
        time.sleep(interval)

# Kullanıcıdan harf sayısı ve kontrol aralığı bilgilerini al
try:
    letter_count = int(input("How many letter usernames should be checked? (Example: 5): "))
    if letter_count <= 0:
        print("Harf sayısı pozitif bir sayı olmalıdır.")
    else:
        interval = float(input("Delay (in seconds): "))
        if interval <= 0:
            print("Saniye aralığı pozitif bir sayı olmalıdır.")
        else:
            # Fonksiyonu kullanıcıdan alınan harf sayısı ve aralık ile çalıştır
            check_user_status(letter_count, interval)
except ValueError:
    print("Lütfen geçerli bir sayı girin.") 