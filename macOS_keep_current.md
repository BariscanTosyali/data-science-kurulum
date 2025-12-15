
# Kurulumunuzu güncel tutma

Bu bölüm, kurulumunuzun güncel olduğundan emin olmak için izlemeniz gereken adımları içerir.

Her şeyden önce, iyi koşullarda çalışabilmek için aşağıdakilerden emin olun:

- yüksek hızlı bir internet bağlantısı
- bilgisayarınızda kodunuzu verimli bir şekilde çalıştırabilmek için yeterli bellek (8GB)
- büyük dataset’ler üzerinde çalışabilmek için bilgisayarınızda yeterli disk alanı (30GB)

## git

git komutlarının çalıştığından emin olun

``` bash
git --version
```

👉 git versiyon numarasını aşağıdakine benzer bir şekilde görüyor olmalısınız :

``` bash
git version 2.33.0
```

## GitHub

Github hesabınız olduğundan ve bilgisayarınızdan bu hesaba erişebildiğinizden emin olun.

``` bash
cd ~/code/<YOUR_GITHUB_NICKNAME>/
git clone git@github.com:<YOUR_GITHUB_NICKNAME>/data-setup data-setup
```

👉 Bu repo doğru bir şekilde clone'lanmalı :

``` bash
Cloning into 'data-setup'...
remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (14/14), done.
Receiving objects: 100% (21/21), done.
Resolving deltas: 100% (6/6), done.
remote: Total 21 (delta 6), reused 16 (delta 1), pack-reused 0
```

👉 clone'lanan repo'yu silebilirsiniz.

``` bash
rm -Rf data-setup
```

## pyenv konfigürasyonunuzu kontrol edin

`~/.zprofile` dosyanızın olduğundan emin olun:

``` bash
cat ~/.zprofile
```

👉 Komutu çalıştırdıktan sonra aşağıdaki gibi satırlar görmelisiniz :

``` bash
# Setup the PATH for pyenv binaries and shims
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
type -a pyenv > /dev/null && eval "$(pyenv init --path)"
```

Eğer görmüyorsanız `~/.zprofile` dosyasını kendiniz oluşturun :

``` bash
cd
touch .zprofile
```

Aşağıdaki satırları `~/.zprofile` dosyanıza ekleyin:

``` bash
# Setup the PATH for pyenv binaries and shims
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
type -a pyenv > /dev/null && eval "$(pyenv init --path)"
```

## Bu eğitime özel virtual environment oluşturun

pyenv'ı güncelleyin :

``` bash
brew update && brew upgrade pyenv
```

Python'un güncel versiyonunu yükleyin :

```bash
pyenv install 3.12.9
```

👉 Çalıştırılan komutun sonlanmasını bekleyin ve **terminal'i restart edin**

Önce var olan virtual environment'ı kaldıralım :

```bash
pyenv virtualenv-delete workintech_current
```

Şimdi de yenisini ekleyelim :

```bash
pyenv virtualenv 3.12.9 workintech_current
```

Bunu default olarak ayarlayalım :

```bash
pyenv global workintech_current
```

Artık yeni virtual environment’ın aktif olduğunu görebilmeliyiz :

``` bash
pyenv versions
```

👉 Aşağıdaki gibi bir çıktı görmelisin :

``` bash
  system
  3.12.9
  3.12.9/envs/workintech_current
  3.10.6
  3.10.6/envs/workintech
* workintech_current
  workintech
```

### Eğitimde kullanacağımız paketleri yükleyelim

```bash
pip install -U pip
```

Bilgisayarınız **Apple Silicon** kullanıyorsa, aşağıdaki paragrafı genişlet ve incele. Aksi halde bu adımı atla.

<details>
  <summary>👉&nbsp;&nbsp;Apple Silicon için Kurulum 👈</summary>

``` bash
pip install -r https://raw.githubusercontent.com/workintech/data-science-kurulum/master/specs/releases/apple_silicon.txt
```
</details>

Bilgisayarınız **Apple Intel** kullanıyorsa, aşağıdaki paragrafı genişlet ve incele. Aksi halde bu adımı atla.

<details>
  <summary>👉&nbsp;&nbsp;Apple Intel için Kurulum 👈</summary>

``` bash
pip install -r https://raw.githubusercontent.com/workintech/data-science-kurulum/master/specs/releases/apple_intel.txt
```
</details>

## Docker

Docker uygulamasını açın

Docker'ın hello-world imaj'ını çalıştırdığından emin olun :

``` bash
docker run hello-world
```

👉 Komutun tam olarak çalıştığından/sonlandığından emin olun

Docker uygulamasını kapatın


## Python Kurulum Kontrolü

### Python ve package kontrolü

terminal'i resetleyelim:

```bash
cd ~/code && exec zsh
```

Python versiyonunu aşağıdaki komut ile kontrol edelim:

```bash
zsh -c "$(curl -fsSL https://raw.githubusercontent.com/workintech/data-science-kurulum/master/checks/python_checker.sh)" 3.12.9
```

Gerekli paketlerin yüklendiğini aşağıdaki komut ile kontrol edelim:
```bash
zsh -c "$(curl -fsSL https://raw.githubusercontent.com/workintech/data-science-kurulum/master/checks/pip_check.sh)"
```

Şimdi, bu paketleri yükleyip yükleyemediğinizi kontrol etmek için aşağıdaki komutu çalıştıralım :

```bash
python -c "$(curl -fsSL https://raw.githubusercontent.com/workintech/data-science-kurulum/master/checks/pip_check.py)"
```

### Jupyter Kontrolü

Jupyter'i çalıştırabildiğimizden emin olalım :

```bash
jupyter notebook
```

Tarayıcımız artık `jupyter`'i yeni bir sekmede açmalı :

![jupyter.png](images/jupyter.png)

`New`e tıkla ve dropdown listesinden `Python 3 (ipykernel)`i seç:

![jupyter_new.png](images/jupyter_new.png)

Yeni bir notebook, yeni bir sekmede açılmalı :

![jupyter_notebook.png](images/jupyter_notebook.png)

Notebook’ta doğru python version’ını çalıştırdığınızdan emin olun. Yeni bir `cell`(hücre) oluşturun ve aşağıdaki kodu çalıştırın :

``` python
import sys; sys.version
```

`3.12.9` çıktısını görmelisiniz. Eğer göremiyorsanız ayarlarınızda bir sorun olabilir. Yardım almanız gerekebilir.

Tarayıcınızda notebook pencerelerini kapatarın ve terminalde  `CTRL` + `C` tuş kombinasyonu ile jupyter'i sonlandırın.

Tebrikler, her şey hazır! Tüm Data Science eğitimi boyunca ihtiyaç duyacağınız tüm third-party package’ları içeren eksiksiz bir python virtual environment kurduk.
