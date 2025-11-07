# Ders 1-1: Kurulum ve Temel Bilgiler
## Python ve Yardımcı Araçların Kurulumu

Bilgisayarımızda Python kodlarını ve dosyalarını çalıştırabilmek için Python'u kurmamız gerekiyor.

İşletim sisteminize göre aşağıdaki adımları takip ederek Python'u bilgisayarınıza kurabilirsiniz.

<details>
<summary>Windows 10/11</summary>

1. Bilgisayarınızda halihazırda Python kurulumu olup olmadığını kontrol edin. Bunu yapmak için:

a. Başlat menüsüne gidin ve "powershell" yazarak PowerShell'i açın.

b. Aşağıdaki komutu girin:

   ```
   python --version
   ```
   veya
   ```
   py --version
   ```

Eğer Python yüklüyse, sürüm numarasını göreceksiniz.

Örneğin:

    Python 3.13.9
    

Yüklü değilse, bir hata mesajı alacaksınız.
2. Python yüklü değilse:

[Python'un resmi web sitesinden](https://www.python.org/downloads/windows/) en son sürümü indirin. İndirilen dosyayı çalıştırın ve kurulum sihirbazını takip edin. **"Add Python to PATH" seçeneğini işaretlemeyi unutmayın!!!** Kurulum tamamlandıktan sonra PowerShell'i yeniden açın ve yukarıdaki komutu tekrar girerek Python'un doğru şekilde yüklendiğini doğrulayın.

</details>

<details>
<summary>macOS</summary>
macOS 12.3 sürümünden itibaren Python 2.x sürümü macOS ile birlikte gelmemektedir. Varsayılan olarak gelen Python sürümü resmi Python sürümü değildir ve bazı kısıtlamalar içerebilir. Bu nedenle, Python'un resmi sürümünü kurmanız önerilir.

1. Terminal'i açın. Bunu yapmak için Spotlight'ı açın (Cmd + Space) ve "Terminal" yazın.

2. Aşağıdaki komutu girin:

   ```
   python3 --version
   ```

Eğer Python yüklüyse, sürüm numarasını göreceksiniz.

Örneğin:

    Python 3.13.9

Yüklü değilse, bir hata mesajı alacaksınız.
3. Python yüklü değilse:

   [Python'un resmi web sitesinden](https://www.python.org/downloads/macos/) en son sürümü indirin. İndirilen dosyayı çalıştırın ve kurulum sihirbazını takip edin. Kurulum tamamlandıktan sonra Terminal'i yeniden açın ve yukarıdaki komutu tekrar girerek Python'un doğru şekilde yüklendiğini doğrulayın.

</details>

<details>
<summary>Linux</summary>

1. Terminal'i açın. (Genellikle Ctrl + Alt + T kısayoluyla açılabilir.)

2. Aşağıdaki komutu girin:

   ```
   python3 --version
   ```

Eğer Python yüklüyse, sürüm numarasını göreceksiniz.

Örneğin:

    Python 3.13.9

Yüklü değilse, bir hata mesajı alacaksınız.
3. Python yüklü değilse:

    - Debian/Ubuntu tabanlı sistemlerde:
    
      ```
      sudo apt update
      sudo apt install python3
      ```
    
    - Fedora tabanlı sistemlerde:
    
      ```
      sudo dnf install python3
      ```
    
    - Arch Linux tabanlı sistemlerde:
    
      ```
      sudo pacman -S python
      ```
Kurulum tamamlandıktan sonra Terminal'i yeniden açın ve yukarıdaki komutu tekrar girerek Python'un doğru şekilde yüklendiğini doğrulayın.

</details>

## Kod Editörü Kurulumu

Python kodlarını istediğiniz bir metin editöründe yazabilirsiniz. Ancak, kod yazmayı ve yönetmeyi kolaylaştıran gelişmiş özelliklere sahip bir kod editörü kullanmanız önerilir. Bu derslerde Visual Studio Code (VS Code) editörünü kullanacağız. Dilerseniz PyCharm veya başka bir editör de kullanabilirsiniz.

VS Code'u kurmak için aşağıdaki adımları takip edebilirsiniz:

<details>
<summary>Windows 10/11</summary>

1. [Visual Studio Code'un resmi web sitesine](https://code.visualstudio.com/) gidin.
2. "Download" butonuna tıklayın ve Windows için en son sürümü indirin.
3. İndirilen dosyayı çalıştırın ve kurulum sihirbazını takip edin.
4. Kurulum tamamlandıktan sonra Visual Studio Code'u başlatın.

</details>

<details>
<summary>macOS</summary>

1. [Visual Studio Code'un resmi web sitesine](https://code.visualstudio.com/) gidin.
2. "Download" butonuna tıklayın ve macOS için en son sürümü indirin.
3. İndirilen .zip dosyasını açın ve Visual Studio uygulamasını "Applications" klasörüne sürükleyin.
4. "Applications" klasöründen Visual Studio Code'u başlatın.
</details>

<details>
<summary>Linux</summary>

1. [Visual Studio Code'un resmi web sitesine](https://code.visualstudio.com/docs/setup/linux) gidin.
2. Dağıtımınıza uygun kurulum talimatlarını takip edin. Örneğin, Debian ve Ubuntu için resmi sitedeki .deb paketini indirip aşağıdaki komutları kullanabilirsiniz:

   ```
   sudo apt install ./<dosya_adı>.deb
   ```
3. Kurulum tamamlandıktan sonra terminalden `code` komutunu kullanarak Visual Studio Code'u başlatabilirsiniz.
</details>

VS Code'u kurduktan sonra, Python geliştirme ortamınızı optimize etmek için "Python" uzantısını yüklemenizi önerilir. Bunu yapmak için:

1. Visual Studio Code'u açın.
2. Sol kenar çubuğundaki "Extensions" (Uzantılar) simgesine tıklayın.
3. Arama çubuğuna "Python" yazın ve çıkan sonuçlardan Microsoft'un "Python" uzantısını bulun.
4. "Install" (Yükle) butonuna tıklayarak uzantıyı yükleyin.

Artık Python kodlarını yazmaya ve çalıştırmaya hazırsınız! İlk kodumuzu yazmak için yeni bir dosya oluşturun, uzantısını `.py` olarak ayarlayın (örneğin, `hello.py`) ve aşağıdaki kodu ekleyin:

```python
print("Hello World!")
```
Dosyayı kaydedin ve çalıştırmak için terminalde aşağıdaki komutu kullanın ya da VS Code içindeki Çalıştır butonuna tıklayın:

```
python hello.py
```
