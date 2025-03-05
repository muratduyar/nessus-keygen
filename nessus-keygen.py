import requests
import random
import string
import time
import json

# ASCII Art - Giriş ekranı
def display_welcome_message():
    print(r"""
| \ | | ___  ___ ___ _   _ ___  | |/ /___ _   _  __ _  ___ _ __  
|  \| |/ _ \/ __/ __| | | / __| | ' // _ \ | | |/ _` |/ _ \ '_ \ 
| |\  |  __/\__ \__ \ |_| \__ \ | . \  __/ |_| | (_| |  __/ | | |
|_| \_|\___||___/___/\__,_|___/ |_|\_\___|\__, |\__, |\___|_| |_|
                                          |___/ |___/           
""")
    print("==== Developed by Murat Duyar ====")
    time.sleep(1)

# Rastgele string üretme
def generate_random_string(length, chars=string.ascii_letters):
    return ''.join(random.choices(chars, k=length))

# Rastgele telefon numarası üretme
def generate_random_phone():
    return ''.join(random.choices(string.digits, k=10))

# Rastgele şirket ismi üretme
def generate_random_company_name():
    return generate_random_string(random.randint(5, 10))

# Rastgele e-posta adresi üretme
def generate_email():
    return generate_random_string(15) + "@" + generate_random_company_name() + random.choice([".com", ".in", ".co", ".org", ".net"])

# Nessus API ile key üretme fonksiyonu
def generate_nessus_key(app_type):
    app_config = {
        "nessus": {
            "tempProductInterest": "Tenable Nessus Professional",
            "gtm_category": "Nessus Pro Eval"
        },
        "expert": {
            "tempProductInterest": "Tenable Nessus Expert",
            "gtm_category": "Nessus Expert Eval"
        }
    }

    if app_type not in app_config:
        print("[✗] Invalid product type selected.")
        return

    user_data = {
        "skipContactLookup": "true",
        "product": app_type,
        "first_name": generate_random_string(random.randint(5, 10)),
        "last_name": generate_random_string(random.randint(4, 8)),
        "email": generate_email(),
        "phone": generate_random_phone(),
        "title": "Security Analyst",
        "company": generate_random_company_name(),
        "companySize": "10-49",
        "country": "US",
        "apps": [app_type],
        "tempProductInterest": app_config[app_type]["tempProductInterest"],
        "gtm": {"category": app_config[app_type]["gtm_category"]}
    }
    
    headers = {
        'User-Agent': f"Mozilla/5.0 (Windows NT {random.randint(10, 12)}.{random.randint(0, 9)}) AppleWebKit/{random.randint(500, 600)} (KHTML, like Gecko) Chrome/{random.randint(50, 90)}.0 Safari/{random.randint(500, 600)}"
    }
    
    try:
        response = requests.post('https://www.tenable.com/evaluations/api/v2/trials', json=user_data, headers=headers)
        response.raise_for_status()

        try:
            response_data = response.json()
            activation_code = response_data.get("code")

            if activation_code:
                print("\n[✓] Nessus Subscription Key Generated Successfully!")
                print("--------------------------------------")
                print(f"Email: {user_data['email']}")
                print(f"Nessus {app_type.replace('-', ' ').capitalize()} Activation Code: {activation_code}")
                print("--------------------------------------")
            else:
                print("[✗] Failed to retrieve Nessus Activation Code. Please try again later.")

        except json.JSONDecodeError:
            print("[✗] Response could not be parsed as JSON. Unexpected response format.")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"[✗] HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"[✗] Request failed: {err}")

# Ana program döngüsü
def main():
    display_welcome_message()

    while True:
        print("\n[+] Welcome to Nessus Subscription Key Generator")
        print("1. Nessus Professional Key")
        print("2. Nessus Expert Key")
        print("0. Exit")
        
        choice = input("Please Select Your Subscription: ").strip()
        
        if choice == "1":
            print("[+] Generating Nessus Professional Key...")
            generate_nessus_key("nessus")
        elif choice == "2":
            print("[+] Generating Nessus Expert Key...")
            generate_nessus_key("expert")
        elif choice == "0":
            print("[*] Exiting the program. Goodbye!")
            break
        else:
            print("[!] Invalid input. Please try again.")

if __name__ == '__main__':
    main()
