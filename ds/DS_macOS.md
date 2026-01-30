# Docker Kurulum talimatları

## Docker 🐋

Docker, uygulama geliştirme, paketleme ve çalıştırma için açık bir platformdur.

_Eğer bilgisayarınızda zaten Docker yüklüyse, lütfen en son sürüme güncelleyin._

### Docker'ı Yükleme

[Docker](https://docs.docker.com/get-docker/)  web sitesine gidin ve işletim sisteminizi seçin:

![](../images/docker.png)

Ardından kurulum talimatlarını takip edin ve masaüstü uygulamasını kurun.

Kurulum tamamlanıp başlatıldıktan sonra Docker'ın çalıştığını doğrulayın:

```bash
docker info
```

Şuna benzer bir çıktı almalısın:

![](../images/docker_info.png)



## `gcloud` CLI

Google Cloud Platform hesabımızı kurmadan önce `gcloud` CLI'yi yapılandıralım (Google Cloud Platform için komut satırı arayüzü). Aşağıdakileri çalıştırın ve terminal istemlerini takip ederek $PATH'inizi güncelleyin ve `.zshrc` dosyası için komut tamamlama özelliğini etkinleştirin:

```bash
brew install --cask google-cloud-sdk
```

Daha sonra şunu çalıştırabilirsin:

```bash
$(brew --prefix)/share/google-cloud-sdk/install.sh
```

<details>
  <summary><code>no such file or directory</code> hatası alıyorum?</summary>

  Şunu deneyin:

```bash
$(brew --prefix)/Caskroom/google-cloud-sdk/latest/google-cloud-sdk/install.sh
```

Eğer bu işe yaramazsa, Slack'ten #data-yardım kanalından yardım isteyin.

</details>


## Google Cloud Platform kurulumu

[GCP](https://cloud.google.com/), Machine Learning tabanlı ürünlerinizi production ortamına deploy etmek için kullanacağınız bir cloud çözümüdür.


🚨 Daha önceden google cloud için free trial özelliğini 3 ay boyunca kullanmıştınız. Yeni bir google hesabı ile tekrar 3 aylık süre için $300 değerinde ücretsiz kredi alabilirsiniz. Yeni bir sanal kart numarası ve başka bir telefon numarası(Örn: anne/baba/kardeş v.b.) ile kayıt oluşturabilirsiniz. Hesabı aktifleştirdikten ve 2 adımlı girişi aktifleştirdikten sonra da telefon numarasını hesaptan silebilirsiniz. 🙅‍♂️

### Project Kurulumu

- [Google Cloud](https://console.cloud.google.com/) adresine gidin ve henüz bir hesabınız yoksa bir hesap oluşturun.
- Cloud Console’da, proje listesinden bir Cloud project seçin veya yeni bir tane oluşturun.


![](../images/ds/gcp-1.png)

![](../images/ds/gcp-2_new_project.png)

- Örneğin `science-s20` gibi bir isim verin
- ❗ ÖNEMLİ: *Location* alanının *No organization* olarak ayarlandığını kontrol edin ❗
- Proje için otomatik olarak oluşturulan `ID`’yi not edin, örneğin `science-s20-123456`


![](../images/ds/gcp-3-new_project_details.png)



### Google Hesabı Dilini Ayarlama

Eğitim sırasında talimatları daha kolay takip edebilmek için GCP hesap ayarlarınızı açın:

https://myaccount.google.com/language

Eğer *preferred language* aşağıdakiler değil ise:
- **English**
- **United States**

İngilizce olarak değiştirin:
- Kalem simgesine tıklayın
- **English** seçin
- **United States** seçin
- **Select**'e tıklayın.

### Billing Account Ayarlama

Hesabınızı şimdi kredi kartınıza bağlayacaksın. Bu adım zorunludur; aksi takdirde GCP tarafından sunulan hizmetleri kullanamazsınız. Endişelenmeyin eğitim süresince çoğu GCP hizmetini ücretsiz kredi ile kullanabileceksin.

![](../images/ds/gcp-5-billing.png)

- **Billing**'e tıklayın
- **MANAGE BILLING ACCOUNTS**'a tıklayın
- **ADD BILLING ACCOUNT**'a tıklayın
- Billing hesabınıza bir isim verin, örn. `My Billing Account`
- "I have read..." kutusunu işaretleyin ve terms of service'i kabul edin
- **CONTINUE**'ya tıklayın
- Hesap türünüzü seçin: `Individual`
- Adınızı ve adresinizi girin

![](../images/ds/gcp-5-billing2.png)
90 gün bayunca geçerli 300$ krediniz olduğunu görmelisiniz.

- Card details'a tıklayın
- Kredi kartı bilgilerinizi girin
- **START MY FREE TRIAL**'a tıklayın

![](../images/ds/gcp-5-billing3.png)

Bu işlem tamamlandığında, billing hesabınızın GCP projenize bağlı olduğunu doğrulayın.

- Projenizi seçin
- **Billing**'e gidin
- **LINK A BILLING ACCOUNT**'u seçin
- `My Billing Account`'u seçin
- **SET ACCOUNT**'a tıklayın

![](../images/ds/gcp-5-billing4.png)

Aşağıdaki gibi bir yazı görmelisiniz:

```
Free trial status: $300 credit and 91 days remaining - with a full account, you'll get unlimited access to all of Google Cloud Platform.
```

<details>
  <summary>👉 Google'dan "Urgent: your billing account XXXXXX-XXXXXX-XXXXXX has been suspended" başlıklı bir email veya uyarı alrısanız. 👈</summary>

Bu özellikle sanal kart kullandı iseniz, bu karttan validation için para çekemedi ise veya aynı telefon numarası ile kayıt yaptırdıysanız olabiliyor.

- PROCEED TO VERIFICATION'a tıklayın
- Sanal kredi kartınızın ekran görüntüsünü gönderebilirsiniz (ekran görüntüsünden geçerlilik tarihini kaldırmayı unutmayın)
- Bir eğitime katıldığınızı, GCP'yi öğrenme amacıyla bir proje oluşturduğunuzu ve eğitim aşamasında beklenmedik bir fatura ile karşılaşmamak adına sanal kart kullanmak istediğinizi belirtin.

30 dakika içinde doğrulama veya ek bilgi talepleri alabilirsiniz veya sizden 500₺ gibi bir ödeme yapmanız istenebilir. Bu ödeme, hesabınızın doğrulanması içindir. Deneme süresi bitene kadar iade isteyebilirsiniz. Genelde 90 gün sonunda iade edilir ama buna güvenmeyin iade istiyorsanız kendiniz talep edin. Büyük ihtimalle o parayı google'da kullanmayı tarcih edeceksiniz 😉

Doğrulama tamamlandığında, "Your Google Cloud Platform billing account XXXXXX-XXXXXX-XXXXXX has been fully reinstated and is ready to use." başlıklı bir e-posta almanız gerekir.

</details>

### GCP service'lerini etkinleştirme

- Google Cloud projeniz için Billing(faturalama) hesabınının etkin olduğundan emin olun

ℹ️ Google Cloud kaynakları için kullanabileceğiniz **300$ kredi**'niz var; bu eğitim için fazlasıyla yeterli olacaktır.

- [BigQuery ve Compute Engine API'larını etkinleştirin](https://console.cloud.google.com/flows/enableapi?apiid=bigquery,compute) (Bu adım birkaç dakika sürebilir)

### Cloud sdk ayarları

- GCP için kullandığınız Google hesabıynızla `gcloud` CLI'da kimlik doğrulaması yapın:

```bash
gcloud auth login
```

- Web tarayıcınızda açılan yeni sekmede Google hesabınıza giriş yapın
- 👀 KONTROL: Etkin hesabınızı listeleyerek GCP için kullandığınız e-posta adresinin listede olduğunu doğrulayın
```bash
gcloud auth list
```

- Geçerli projenizi ayarlayın (`PROJECT_ID`'yi projenizin `ID`si ile değiştirin, örn. `science-s20-123456`)
```bash
gcloud config set project PROJECT_ID
```

- 👀 KONTROL: Etkin hesabınızı ve geçerli projenizi listeleyin ve projenizin listede olduğunu doğrulayın
```bash
gcloud config list
```

### Servis Account Key oluşturma 🔑

Artık bir `GCP account` ve bir `project` (PROJECT_ID ile tanımlanmış) oluşturduğunuza göre, kodunuzun hangi eylemleri (API çağrılarını) gerçekleştirmesine izin vereceğimizi yapılandıralım:

<details>
  <summary>🤔 Neden bir Servis Account Key'ine ihtiyacımız var?</summary>

  HATIRLATMA: Böyle bir key'i daha önce DBT için oluşturmuştuk.

  GCP hesabını kredi kartına bağladın. Hesabın, Google Cloud Platform kaynaklarını kullanımına göre faturalandırılacaktır. Ücretsiz deneme süresi bittikten sonra ya da deneme süresi içindeki harcama limitini aştığında fatura kesilecektir.

  Hesabında bir `GCP project` oluşturmuş bulunuyorsunuz; bu proje `PROJECT_ID` ile tanımlanır. `GCP project`'leri, GCP kaynaklarını tüketiminizi daha iyi organize edip izleyebilmenizi sağlar. Eğitim kapsamında tek bir proje oluşturacağız.

  Kodumuzun bir proje içindeki hangi kaynakları kullanabileceğini belirtmemiz gerekiyor. Kodumuz GCP kaynaklarına API çağrıları yoluyla erişecek.

  API çağrıları ücretsiz olmadığından, kodumuzun hangi API'leri nasıl kullanacağına dikkatle karar vermeliyiz. Eğitim süresince kısıtlama uygulamadan GCP API'lerini kullanmamıza izin vereceğiz.

  Bir GCP hesabına bağlı birden çok proje olabileceği gibi, bir proje de birden çok servise sahip olabilir (herhangi bir kod paketi veya servisi, GCP API çağrılarına ihtiyaç duyabilir).

  GCP, API çağrısı yapan servislerin platformda kayıtlı olmasını ve kimlik bilgilerinin bir `service account` aracılığıyla yapılandırılmasını istiyor.

  Şimdilik tek bir servis kullanacağız ve buna karşılık gelen `service account`'u oluşturacağız.
</details>

`service account` uygulamanızı (dolayısıyla GCP billing hesabınızı ve kredi kartınızı) tanımladığı için, bir sonraki adımlarda dikkatli olmalıyız!.

⚠️ **Servis hesabı json dosyanızı paylaşmayın 🔑** ⚠️ Dosyayı masaüstünde saklamayın, git deposuna koymayın (repo private olsa bile), veya sosyal medyada paylaşmayın. Ne derler bilirsiniz "Babanıza bile güvenmeyin" 😂.

#### Servis Accounts sayfasına gidin

Servis hesapları sayfasına şu bağlantı ile hızlıca açabilirsin: https://console.cloud.google.com/apis/credentials/serviceaccountkey

- İstendiğinde son projeler listesinden projenizi seçin.
- Eğer istenmiyorsa, sayfanın üstündeki proje seçicisinden doğru proje seçili olduğundan emin olun!.

Servis Accounts sayfasına alternatif olarak şu yoldan da ulaşabilirsin:

![Service Account Sayfasını Açma Adımları](../images/ds/gcp-5-service_account.png "Service Account Sayfasını Açma Adımları")


#### Servis Account oluşturma

- **CREATE SERVICE ACCOUNT**'a tıklayın.

![](../images/ds/gcp-5-service_account2.png "Service Account Oluşturma")


- Servis account'unuza bir isim, id ve açıklama verin, ardından **CREATE AND CONTINUE**'e tıklayın.

![](../images/ds/gcp-5-service_account3.png "Service Account'u İsimlendirme")


- **Select a role**'e tıklayın ve `Basic` altından **`Owner`** rolünü seçin; bu, servis account'unuzun proje kaynaklarına tam erişim izni verir.

![](../images/ds/gcp-5-service_account4.png "BigQuery için izinleri verme")


- Bu pencerenin altındaki mavi **DONE** butonuna tıklayın. *Grant your users access to this service account* bölümüne şimdilik gerek yok.

![](../images/ds/gcp-5-service_account5.png "Servis Account Oluşturmayı Tamamlama")


#### Bu servis account için JSON key'i oluşturma 🔑

- Servis accounts sayfasında, az önce oluşturduğun servis account'unun e-posta adresine tıklayın.

![](../images/ds/gcp-5-json_key.png "Servis Account'u Seçme")


- Sayfanın üst kısmındaki **KEYS** sekmesine tıklayın.

![](../images/ds/gcp-5-json_key2.png "Keys Sekmesini Açma")


- **ADD KEY**'e tıklayın, ardından **Create new key**'i seçin.

![](../images/ds/gcp-5-json_key3.png "Yeni Key Ekleme")


- **JSON**'i seçin ve **CREATE**'e tıklayın.

![](../images/ds/gcp-5-json_key4.png "JSON Key Oluşturma")


- Tarayıcı, oluşturduğunuz json dosyasını indirme klasörünüze kaydedecektir (dosya ismi servis accountunuzun adına göre oluşur, ör. `science-s20-123456789abc.json`).


- Servis account json dosyasını hatırlayacağınız bir yerde saklayın, tavsiye olarak git projelerini koyduğunuz yere `code/GITHUB_NICKNAME/gcp/` dizinine taşıyın:

``` bash
/Users/MACOS_USERNAME/code/GITHUB_NICKNAME/gcp/SERVICE_ACCOUNT_JSON_KEY_DOSYASI.json
```

- `JSON` dosyasının **mutlak yolunu** bir ortam değişkeni olarak kaydedin: (aşağıdaki komutta `'/path/to/the/SERVICE_ACCOUNT_JSON_KEY_DOSYASI.json'` kısmını json dosyanızın mutlak yolu ile değiştirmeyi unutmayın)

``` bash
echo 'export GOOGLE_APPLICATION_CREDENTIALS=/path/to/the/SERVICE_ACCOUNT_JSON_KEY_DOSYASI.json' >> ~/.zshrc
```

**Not:** Bu komutu her çalıştırdığınızda, aynı satır `~/.zshrc` dosyanıza ayrı ayrı eklenecektir. Hata yaptıysanız dosyayı açıp satırı düzenlemeniz/silmeniz en iyisidir.

Bunu yapmak için şu komutu kullanabilirsin:

```bash
code ~/.zshrc
```

Terminal'de tabii ki! 😄


<details>
  <summary>ℹ️ Bir dosyanın mutlak yolunu nasıl bulurum?</summary>

  Dosyayı terminale sürükleyip bırakarak bulabilirsin 😉.

</details>

**Terminalinizi quit edin ve tekrar başlatın** ve şu komutu çalıştırın:

``` bash
echo $GOOGLE_APPLICATION_CREDENTIALS
```

Çıktı şu şekilde olmalıdır:

```bash
/some/absolute/path/to/your/gcp/SERVICE_ACCOUNT_JSON_KEY_DOSYASI.json
```

Şimdi servis account json dosyanızın yolunun doğru olduğunu doğrulayalım:

``` bash
cat $(echo $GOOGLE_APPLICATION_CREDENTIALS)
```

👉 Bu komut servis account json dosyanızın içeriğini göstermelidir. Göstermezse Slack'ten #data-yardım kanalından yardım isteyin. 🙏

Kodunuz ve araçlarınız artık GCP hesabınızdaki kaynaklara erişebilecek.

Son yapılandırma adımlarına geçelim...

- Aktif hesabınıza ve geçerli projenize ait servis hesaplarını listeleyin
```bash
gcloud iam service-accounts list
```

- Servis hesabı e-posta adresini alın, ör. `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`
- CLI'dan servis hesabının rollerini listeleyin (PROJECT_ID ve SERVICE_ACCOUNT_EMAIL ile değiştirin)
```bash
gcloud projects get-iam-policy PROJECT_ID \
--flatten="bindings[].members" \
--format='table(bindings.role)' \
--filter="bindings.members:SERVICE_ACCOUNT_EMAIL"
```
- Servis hesabınızın `roles/owner` rolüne sahip olduğunu görmelisiniz

<details>
  <summary>Sorun giderme</summary>

- `AccessDeniedException: 403 The project to be billed is associated with an absent billing account.`
  - GCP projeniz için billing'in etkin olduğundan emin olun: https://cloud.google.com/billing/docs/how-to/modify-project
</details>

🏁 GCP kurulumu tamamlandı. Şimdi onlar düşünsün!
