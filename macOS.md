# Kurulum Adımları

Başlayalım :rocket:

## Apple Silicon İçin

Bilgisayarınızı 2020’nin sonlarından sonra satın aldıysanız, büyük ihtimalle Intel bir işlemci yerine yeni bir Apple silicon çipine sahiptir.

Bilgisayarınız **Apple Silicon** kullanıyorsa, aşağıdaki paragrafı genişlet ve incele. Aksi halde bu adımı atla.

<details>
  <summary>👉&nbsp;&nbsp;Apple Silicon için Kurulum 👈</summary>

Terminal’i, Intel bir bilgisayara sahipmişsiniz gibi kullanmanızı sağlayan bir yöntem olan Rosetta’yı kullanmadığınızdan emin olalım :

`Cmd` + `Space` kombinasyonu ile spotlight'ı açın ve `terminal`i aratın ve tıklayıp açın.

Terminal uygulaması açıkken ekranınızın sol üstünde apple logosunun yanındaki Terminal'e tıklkayın ve Settings'e tıklayın. Burada general'in içinde "Open using Rosetta"nın **seçili olmadığından** emin olun.

Görmüyorsanız devam edebilirsiniz.
</details>

🚨 Kurulumun ilerleyen aşamalarında, bilgisayarınızın bir Apple Silicon çipi mi kullandığını yoksa Apple Intel sürümü mü olduğunu hatırlamanız gerekecek. Bunu aklınızda tutun.


## İpucu: Mac’te uygulamaları kapatma

Mac’te bir uygulama penceresinin sol üst köşesindeki küçük kırmızı çarpıya tıklamak uygulamayı gerçekten kapatmaz, sadece aktif pencereyi kapatır. Uygulamadan gerçekten çıkmak için, uygulama aktifken `Cmd + Q` tuşlarına basın ya da menü çubuğunda(ekranınızın en üstündeki) `APP_NAME` -> `Quit` yolunu izleyin.

![](images/macos_quit.png)

Bu kurulum sırasında **uygulamalardan çıkmanız ve yeniden açmanız** birden fazla kez istenecek; lütfen bunu doğru şekilde yaptığından emin ol :pray:

## Command Line Tools

Yeni bir terminal açın, aşağıdaki komutu kopyalayıp yapıştırın ve `Enter`a basın:

```bash
xcode-select --install
```

Aşağıdaki mesajı alırsanız, bu adımı atlayabilir ve bir sonraki adıma geçebilirsin.

```bash
# command line tools are already installed, use "Software Update" to install updates
```

Bu mesaj görünmez ise, bazı yazılımları yüklemek isteyip istemediğinizi soran bir pencere açılacak: “Install” seçeneğine tıklay ve bitmesini bekle.


![macOS'ta xcode-select'i yükleme](https://github.com/workintech/data-science-kurulum/images/macos_xcode_select_install.png)

:heavy_check_mark: “The software was installed” mesajını görüyorsanız, her şey yolunda demektir. :+1:

:x: `xcode-select --install` komutu başarısız olursa tekrar dene; bazen Apple sunucuları yoğun olabiliyor.

:x: "Xcode is not currently available from the Software Update server" mesajını görürseniz, software update catalog’unu güncellemen gerekir:

```bash
sudo softwareupdate --clear-catalog
```

Bu işlem tamamlandıktan sonra, yeniden yüklemeyi deneyebilirsin.


## Homebrew
### 1. Yükleme:

Mac’te bir Package Manager olan [Homebrew](http://brew.sh/)'i yüklemeniz gerekir.
Bazı yazılımları kurmamız gerektiğinde bunu kullanacağız.

Homebrew'i yüklemek için Terminal’i açın ve şunu çalıştırın:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Onayınızı isteyecek (`Enter`a bas) ve **macOS kullanıcı hesabınızın şifresini** girin (Macbook'unuzu yeniden başlattığınızda girdiğiniz [log in](https://support.apple.com/en-gb/HT202860) şifreniz).
:warning: Terminal’de bir parola yazarken görsel bir geri bildirim (örneğin `*****`) almazsınız, bu **normaldir!!** Parolayı yazın ve Enter tuşuna basarak onaylayın.

<details>
  <summary>🛠 Şuna benzer bir hata alırsanız: <code>Error: Not a valid ref: refs/remotes/origin/master</code></summary>


Tam hali bu şekilde :

``` bash
Error: Not a valid ref: refs/remotes/origin/master :
fatal: ambiguous argument 'refs/remotes/origin/master': unknown revision or path not in the working tree.
```

Çözebilmek için aşağıdaki kodu çalıştırın :

``` bash
rm -fr $(brew --repo homebrew/core)
brew tap homebrew/core
```

</details>

Eğer Homebrew zaten yüklüyse, size bunu söyleyecektir; bu sorun değil, devam edin.

### 2. Güncelleme: En güncel sürümü kullandığınızdan emin olun:

```bash
brew update
```

<details>
  <summary>🛠 Eğer bu hatayı alırsanız : <code>/usr/local must be writable</code> </summary>

Bu kodu çalıştırın :

``` bash
sudo chown -R $USER:admin /usr/local
brew update
```

</details>

### 3. Ardından bazı faydalı yazılımları yükleyin:

Terminal’de aşağıdakileri çalıştırmaya devam edin (tüm satırları tek seferde kopyalayıp yapıştırabilirsin).

```bash
brew upgrade git         || brew install git
brew upgrade gh          || brew install gh
brew upgrade wget        || brew install wget
brew upgrade imagemagick || brew install imagemagick
brew upgrade jq          || brew install jq
brew upgrade openssl     || brew install openssl
brew upgrade tree        || brew install tree
brew upgrade ncdu        || brew install ncdu
brew upgrade xz          || brew install xz
brew upgrade readline    || brew install readline
```


## Visual Studio Code

### Yükleme

[Visual Studio Code](https://code.visualstudio.com) text editor'ünü yükleyin.

Aşağıdaki kodu terminal'inze kopyala (`Cmd` + `C`) ve yapıştır (`Cmd` + `V`) yapın :

```bash
brew install --cask visual-studio-code
```

Ardından, terminalde aşağıdaki komutu çalıştırarak VS Code’u başlatın:

```bash
code
```

:heavy_check_mark: Eğer VS Code açıldı ise her şey yolunda :+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## VS Code Eklentileri

### Yükleme

Bazı yararlı eklentileri VS Code uygulamamıza yükleyelim.

```bash
code --install-extension ms-vscode.sublime-keybindings
code --install-extension emmanuelbeziat.vscode-great-icons
code --install-extension MS-vsliveshare.vsliveshare
code --install-extension ms-python.python
code --install-extension KevinRose.vsc-python-indent
code --install-extension ms-python.vscode-pylance
code --install-extension ms-toolsai.jupyter
code --install-extension alexcvzz.vscode-sqlite
```

Neler yükledik? kendi sayfalarına bir göz atabilirsiniz:
- [Sublime Text Keymap and Settings Importer](https://marketplace.visualstudio.com/items?itemName=ms-vscode.sublime-keybindings)
- [VSCode Great Icons](https://marketplace.visualstudio.com/items?itemName=emmanuelbeziat.vscode-great-icons)
- [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare)
- [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Python Indent](https://marketplace.visualstudio.com/items?itemName=KevinRose.vsc-python-indent)
- [Pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance)
- [Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)
- [SQLite](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)


## Oh-my-zsh

`zsh` plugin'ini yükleyelim: [Oh My Zsh](https://ohmyz.sh/).

Terminal'de aşağıdaki komutu çalıştırın :

```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

"Do you want to change your default shell to zsh?" sorusu gelince `Y` tuşuna basın.

Kurulum bitince aşağıdaki gibi bir ekran ile karşılaşacaksınız:

![](images/oh_my_zsh.png)


:heavy_check_mark: Benzer bir ekran görüyorsanız, her şey yolunda demektir. Diğer adımlarla devam edebilirsiniz. :+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## direnv

[direnv](https://direnv.net/) bir shell extension’dır. Proje bazında environment variable’larla çalışmayı kolaylaştırır. Bu, kodunuzun davranışını özelleştirmek için faydalı olacak.

``` bash
brew install direnv
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```


## GitHub CLI

CLI [Command-line Interface](https://en.wikipedia.org/wiki/Command-line_interface)'in kısaltmasıdır.

Bu bölümde, GitHub ile doğrudan terminal üzerinden etkileşim kurmak için [GitHub CLI](https://cli.github.com/) kullanacağız.

Önceki adımlar sayesinde bilgisayarınızda zaten yüklenmiş olması gerekir.

GitHub’a SSH kullanarak bağlanmak için GitHub CLI (`gh`) kullanacağız. SSH, bilinen kullanıcı adı/parola ikilisi yerine SSH key’leri kullanarak giriş yapmayı sağlayan bir protokoldür.

İlk olarak **login** olmak için, aşağıdaki komutu terminalinize kopyalayıp yapıştırın:

:warning: **Dikkat: `email` kelimesini değiştiremeyin!!!**

```bash
gh auth login -s 'user:email' -w --git-protocol ssh
```

`gh` size bazı sorular soracak :

- `Generate a new SSH key to add to your GitHub account?` sorulunca `Enter`'a basın. Sizin için SSH key oluşturacak.

  Eğer zaten SSH key’leriniz varsa, bunun yerine `Upload your SSH public key to your GitHub account?` mesajını göreceksin. Ok tuşlarıyla public key dosya yolunu seçin ve `Enter` tuşuna basın.

- `Enter a passphrase for your new SSH key (Optional)`: Hatırlayabileceğiniz bir parola yazın. Bu, hard drive’ınızda saklanan private key’i korumak için kullanılan bir paroladır. Ardından `Enter` tuşuna basın.

- `Title for your SSH key`. "GitHub CLI" olarak bırakabilirsin, `Enter` tuşuna basın.

Aşağıdakine benzer bir çıktı alacaksın :

```bash
! First copy your one-time code: 0EF9-D015
- Press Enter to open github.com in your browser...
```

Ekrandaki kodu kopyalayın ve yapıştırın (Bu örnek çıktıda kod:`0EF9-D015`), sonra `Enter` tuşuna basın.

Tarayıcınız açılacak ve GitHub CLI’nin GitHub hesabınızı kullanmasına izin vermenizi isteyecektir. Kabul edin ve biraz bekleyin.

Ardından terminale geri dönün, tekrar `Enter` tuşuna basın ve işlem tamamdır.

Doğru şekilde bağlandığınızı kontrol etmek için şunu yazın:

```bash
gh auth status
```

:heavy_check_mark: `Logged in to github.com as <YOUR USERNAME> ` mesajını alıyorsak her şey yolunda demektir ve sonraki adımlarla ilerleyebiliriz :+1:

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## Dotfiles

Bazı uygulamalarımızın configuration dosyalarını değiştirerek özel ayarlarımızı yükleyelim. Bunun için dotfile'ları güncelleyeceğiz.

> Dotfiles, Unix tabanlı işletim sistemlerinde kullanıcıların konfigürasyon ayarlarını saklamaya yarayan gizli dosyalardır.

dotfile'ları yükleyelim:

```bash
cd ~/code/$GITHUB_USERNAME/data-science-kurulum/dotfiles && zsh install.sh
```

Şimdi de sanal ortamımız için git ayarlarını güncelleyelim:

```bash
cd ~/code/$GITHUB_USERNAME/data-science-kurulum/dotfiles && zsh git_setup.sh
```

☝️ Bu işlem sizden adınızı (**Adınız Soyadınız**) ve e-posta adresinizi isteyecektir.

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

Şimdi terminal'i quit edelim.


## Python Yükleme ([`pyenv`](https://github.com/pyenv/pyenv) ile )

### `conda`yı uninstall edin

Python version’ımızı kurmak ve yönetmek için `pyenv` kullandığımızdan, daha önce [Anaconda](https://www.anaconda.com/) yüklediyseniz bilgisayarınızda bulunabilecek başka bir package manager olan [`conda`](https://docs.conda.io/projects/conda/en/latest/)’yı kaldırmamız gerekiyor. Böylece ileride oluşabilecek olası Python version sorunlarını önlemiş oluruz.

Bilgisayarınızda `conda` yüklü olup olmadığını kontrol edin:

```bash
conda list
```

Eğer `zsh: command not found: conda` mesajını alırsanız, conda kaldırma adımını **atlayabilir** ve bir sonraki bölümü geçebilirsin.


### Install pre-requisites

Python’ı yüklemeden önce, `xz` version’ınızı aşağıdaki komutla kontrol edin:

```bash
brew info xz
```

5.2.0 sürümünden daha yeni olmalı; değilse aşağıdaki komutu çalıştırabilirsin:

```bash
sudo rm -rf /usr/local/opt/xz
brew upgrade
brew install xz
```

sonra bu kodu çalıştırın:

```bash
brew install readline
```

### `pyenv` Yüklemesi

macOS, kullanmak istemediğimiz eski bir Python sürümüyle birlikte gelir. Daha önce Python ve Data Science package’larıyla denemeler yapmak için Anaconda ya da başka bir şey yüklemiş olabilirsiniz. Bunların hiçbiri aslında önemli değil; çünkü Python için profesyonel bir kurulum yapacağız ve bu sayede terminalde `python` yazdığınızda hangi version’ı kullanmak istediğinizi dilediğiniz zaman değiştirebileceksiniz.

Önce, aşağıdaki kodu terminalde kullanarak `pyenv` yükleyelim :

```bash
brew install pyenv
exec zsh
```

### Python'ı Yükleme

Eğitim boyunca aynı şeyleri yapabilemek için en güncel ve stable(kararlı) Python sürümünü yükleyelim:

```bash
pyenv install 3.12.9
```

Bu biraz zaman alacaktır. Bu çok normal. Bir kahve alıp gelebilirsiniz...

<details>
  <summary>🛠 `pyenv` bulunamadı hatası alırsanız</summary>

`Command 'pyenv' not found` hatasını alırsanız aşağıdaki satırı çalıştırın :

```bash
source ~/.zprofile
```

Sonra python'u tekrar yüklemeyi deneyin :

```bash
pyenv install 3.12.9
```

:x: Hala hata almaya devam ediyorsanız slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

</details>

<details>
  <summary>🛠  `zlib` hatası alırsanız</summary>

`pyenv` ile python yüklerken  `zlib` hatası alırsanız:

```txt
zipimport.ZipImportError: can't decompress data; zlib not available
```

`zlib` yükleyin:

```bash
brew install zlib
export LDFLAGS="-L/usr/local/opt/zlib/lib"
export CPPFLAGS="-I/usr/local/opt/zlib/include"
```

Sonra python yüklemeyi tekrar deneyin:

```bash
pyenv install 3.12.9
```

`bzip2` ile ilgili hata alırsanız bunu dikkate almayın ve sonraki adımlarla devam edin.

</details>

<details>
  <summary>🛠 <code>BUILD FAILED</code> hatası alırsanız: </summary>

Bu kodu çalıştırın :

``` bash
sudo rm -rf /Library/Developer/CommandLineTools
```

Sonra python yüklemeyi tekrar deneyin:

```bash
pyenv install 3.12.9
```

:x: Hala hata almaya devam ediyorsanız slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.

</details>


<br>

Bu adım tamamlandığında bu versiyonu default kullanmak istediğimizi  Python **by default**. This is done with:

```bash
pyenv global 3.12.9
exec zsh
```

Çalıştığından emin olmak için `python --version` kodunu çalıştırın. `3.12.9` görüyorsanız, her şey yolunda demektir!

:x: Aksi durumda slack'te **Data-Yardım** kanalından yardım isteyebilirsiniz.


## Python Sanal Ortamı

İlgili Python package’larını yüklemeye başlamadan önce, eğitim için olan kurulumu özel (dedicated) bir virtual environment içine izole edeceğiz. Bunun için `pyenv`nin [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv) adlı bir plugin’ini kullanacağız.

### virtualenv kurulumu

Önce plugin'i yükleyelim:

```bash
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
exec zsh
```

Eğitim boyunca kullanacağımız environment'ı oluşturalım :

```bash
pyenv virtualenv 3.12.9 workintech
```

Default virtual environment'ımızı yeni oluşturduğumuz yapalım:

```bash
pyenv global workintech
```

Harika! Ne zaman bir Python package’ı yükleyecek olursak, bunu bu environment içinde yapacağız.


### Python packages

Artık tertemiz bir `workintech` virtual environment’ımız olduğuna göre, içine bazı package’ları yükleme zamanı geldi.

Öncelikle, Python package’larını [pypi.org](https://pypi.org) üzerinden yüklememizi sağlayan araç olan `pip`i güncelleyelim. `workintech` virtualenv’inin aktif olduğu en son terminalde aşağıdakini çalıştırın:

```bash
pip install --upgrade pip
```

Ardından programın ilk haftaları için bazı package’ları yükleyelim:

Bilgisayarınız **Apple Silicon** kullanıyorsa, aşağıdaki paragrafı genişletin ve inceleyin. Aksi halde bunu yok sayabilirsiniz.

<details>
  <summary>👉&nbsp;&nbsp;Apple Silicon için kurulumlar👈</summary>

``` bash
pip install -r https://raw.githubusercontent.com/workintech/data-science-kurulum/master/specs/releases/apple_silicon.txt
```
</details>

Bilgisayarınız **Apple Intel** kullanıyorsa, aşağıdaki paragrafı genişletin ve inceleyin. Aksi halde bunu yok sayabilirsiniz.

<details>
  <summary>👉&nbsp;&nbsp;Apple Intel için kurulumlar👈</summary>

``` bash
pip install -r https://raw.githubusercontent.com/workintech/data-science-kurulum/master/specs/releases/apple_intel.txt
```
</details>


## Jupyter Notebook tweaking

Notebook’larınızda [`details` disclosure elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details) görünümünü iyileştirelim.

Jupyter config dizininizde bir `custom.css`stylesheet’i oluşturmak için aşağıdaki satırları çalıştırın:

```bash
LOCATION=$(jupyter --config-dir)/custom
SOURCE=https://raw.githubusercontent.com/workintech/data-science-kurulum/refs/heads/master/specs/jupyter/custom.css
mkdir -p $LOCATION
curl $SOURCE > $LOCATION/custom.css
```
