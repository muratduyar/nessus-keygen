# Nessus Subscription Key Generator / Nessus Abonelik Anahtarı

**Geliştirici:** Murat Duyar

Bu proje, Nessus abonelik anahtarlarını (Nessus Professional ve Nessus Expert) oluşturmak için kullanılan bir Python betiğidir. Proje, Tenable Nessus'un deneme sürüm anahtarlarını üretmek için otomatik bir işlem yapmaktadır.

This project is a Python script used to generate Nessus subscription keys (Nessus Professional and Nessus Expert). The project automates the process of generating trial keys for Tenable Nessus.

---

## Özellikler / Features

- **Nessus Professional Key Generator:** Nessus Professional sürümü için deneme abonelik anahtarları üretir.
- **Nessus Expert Key Generator:** Nessus Expert sürümü için deneme abonelik anahtarları üretir.
- Rastgele kullanıcı bilgileri (isim, e-posta, telefon, şirket adı) oluşturulur.
- API üzerinden yapılan işlemler, sahte bir tarayıcı kimliği (User-Agent) ile yapılır.
- Kullanıcı dostu arayüz ile kolay kullanım.

---

## Gereksinimler / Requirements

- Python 3.x
- `requests` modülü

Bu projeyi çalıştırmadan önce Python 3.x'in bilgisayarınızda yüklü olduğundan emin olun. Eğer `requests` modülü yüklü değilse, şu komut ile yükleyebilirsiniz:

Before running the project, make sure Python 3.x is installed on your computer. If the `requests` module is not installed, you can install it with the following command:

```bash
pip install requests
```

---

## Kurulum ve Kullanım / Installation and Usage

1. **Projeyi İndirin / Clone the Project**

   GitHub reposunu bilgisayarınıza klonlayın veya ZIP olarak indirin.

   Clone the GitHub repository or download the ZIP file.

   ```bash
   git clone https://github.com/muratduyar/nessus-keygen.git
   ```

2. **Python Betiğini Çalıştırın / Run the Python Script**

   Projeyi klonladıktan sonra, komut satırında `nessus-keygen.py` dosyasını çalıştırabilirsiniz.

   After cloning the project, you can run the `nessus-keygen.py` script from the command line.

   ```bash
   python nessus-keygen.py
   ```

   Veya Python 3 ile çalıştırıyorsanız:

   Or, if you are using Python 3:

   ```bash
   python3 nessus-keygen.py
   ```

3. **Kullanıcı Seçenekleri / User Options**

   Programı çalıştırdıktan sonra, aşağıdaki seçenekleri sunar:

   After running the script, the following options will be presented:

   ```
   [+] Welcome to Nessus Subscription Key Generator
   1. Nessus Professional Key
   2. Nessus Expert Key
   0. Exit
   ```

   - **1**: Nessus Professional anahtarını oluşturur. / Generates the Nessus Professional key.
   - **2**: Nessus Expert anahtarını oluşturur. / Generates the Nessus Expert key.
   - **0**: Programdan çıkmanızı sağlar. / Exits the program.

4. **Anahtarın Başarıyla Oluşturulması / Successful Key Generation**

   Program, başarıyla bir anahtar oluşturduğunda aşağıdaki gibi bir mesaj görüntüler:

   When the key is successfully generated, a message like the following will be displayed:

   ```
   [✓] Nessus Subscription Key Generated Successfully!
   --------------------------------------
   Email: generated_email@example.com
   Nessus Professional Activation Code: ABCD-EFGH-IJKL-MNOP
   --------------------------------------
   ```

   Eğer bir hata meydana gelirse, hata mesajı şu şekilde olacaktır:

   If there is an error, the error message will be as follows:

   ```
   [✗] Failed to retrieve Nessus Activation Code. Please try again later.
   ```

---

## Hata Ayıklama / Troubleshooting

- Eğer HTTP hatası alırsanız (örneğin, **400 Bad Request**), bu genellikle Tenable API'sindeki geçici bir sorun olabilir. Bir süre sonra tekrar deneyin.

   If you get an HTTP error (e.g., **400 Bad Request**), this is usually due to a temporary issue with the Tenable API. Try again after some time.

- İnternet bağlantınızda herhangi bir sorun olmadığından emin olun.

   Make sure your internet connection is stable and working properly.

---

## Lisans / License

Bu proje, [MIT Lisansı](LICENSE) ile lisanslanmıştır.

This project is licensed under the [MIT License](LICENSE).

---

## Katkı Sağlama / Contributing

Eğer projeye katkıda bulunmak isterseniz, lütfen önce bir "Issue" açın ve ardından bir "Pull Request" gönderin. Katkılarınız için teşekkür ederim!

If you want to contribute to the project, please open an "Issue" first and then submit a "Pull Request". Thanks for your contributions!

---

## İletişim / Contact

- GitHub: [https://github.com/muratduyar](https://github.com/muratduyar)

