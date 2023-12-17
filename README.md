# CoderSpace-Eagle-Eye

# AutoHack Car Damage Detection Projesi: Mercedes C180 Ön Kısım Hasar Tespiti
## Proje Genel Bakışı
"AutoHack" hackathonunda geliştirdiğimiz bu projemiz, Mercedes C180 model araçların ön kısmındaki hasarları tespit etme ve derecelendirme yeteneğine sahiptir. Gelişmiş görüntü işleme teknolojilerini kullanarak, otomotiv endüstrisi için yenilikçi bir çözüm sunmayı amaçlamaktayız. Proje, kodun merkezi olan main.py tarafından yönetilmekte ve ileri düzey görüntü işleme algoritmalarını kullanarak hasar analizi yapmaktadır.

## Arayüz - carDamageGUI.py
Projemizin kullanıcı dostu arayüzü carDamageGUI.py dosyasında yer alır. PyQt5 ve Qt Designer'ın güçlü özellikleri sayesinde, kullanıcıların projeyi kolayca etkileşimde bulunabilecekleri bir ortam sağlar. Bu grafik arayüz, hasar tespiti işlemini başlatmak ve sonuçları görüntülemek için intuitif kontrollere sahiptir.

## Yolo Modeli - YoloModel Klasörü
Derin öğrenme temelli YOLO modeli (bestCarDamageClass.pt), bu projenin çekirdeğini oluşturur. YoloModel klasörü, modelimizin eğitimi için kullanılan scriptleri ve gerekli kütüphaneleri barındırır. Bu klasör, modelimizin doğru bir şekilde çalışmasını ve hasar tespitinin yapılmasını sağlayan altyapıyı içerir.

## Hasar Tespit Modülü - detectDamage.py
Modelimizin hasar tespiti yaptığı ve sonuçları görsel olarak işaretlediği python dosyası detectDamage.pydır. Bu modül, arka planda YOLO modelini çağırır, hasar tespitini gerçekleştirir ve kullanıcı arayüzünde sonuçları görselleştirir.

## Test Görüntüleri - TestImg Klasörü
TestImg klasörü, modelimizin performansını değerlendirmek üzere kullanılan görselleri içerir. Bu görseller hem kendi oluşturduğumuz simülasyon ortamından alınan örnekleri hem de gerçek dünya hasar örneklerini kapsar. Bu klasör, modelimizin doğruluğunu ve güvenilirliğini test etmek için hayati öneme sahiptir.

## Eğitim Süreci
Projemizi geliştirirken, simülasyon ortamında Mercedes C180 model aracına 15 derecelik açılarla hasar vererek ve bu hasarları detaylı bir şekilde etiketleyerek modelimizi eğittik. Bu yöntem, modelimizin çeşitli hasar tiplerini ve derecelerini doğru bir şekilde tanıması ve sınıflandırması için kritik bir öneme sahiptir.

## Ekip
Bu projede ekip adımız Eagle Eye; Doruk Aydoğan, TED Üniversitesi Yazılım Mühendisliği son sınıf öğrencisi; Yücel Çimtay, Dr. Öğr. Üyesi, TED Üniversitesi Bilgisayar Mühendisliği Bölümü öğretim üyesi; ve Ece Selin Adıgüzel, TED Üniversitesi Bilgisayar Mühendisliği son sınıf öğrencisi olarak biz, bilgi ve deneyimlerimizi birleştirerek otomotiv endüstrisindeki hasar tespit süreçlerini iyileştirmeyi hedefledik.

## Kullanım ve Çalıştırma Talimatları
### Ön Koşullar
Bu projeyi çalıştırmak için Python'un yüklü olması gerekmektedir. Ayrıca, projenin bağımlılıklarını yüklemek için gereken requirements.txt dosyası da dahil edilmiştir.

### IDE Üzerinde Çalıştırma
Projemiz, herhangi bir Python IDE'sinde (örneğin, PyCharm) kolaylıkla çalıştırılabilir. Aşağıdaki adımları takip ederek projeyi yerel makinenizde çalıştırabilirsiniz:

+ Projeyi GitHub'dan indirin ve yerel bilgisayarınıza çıkarın.
+ Tercih ettiğiniz Python IDE'sini açın ve Open veya Import Project seçeneği ile indirdiğiniz projeyi seçin.
+ Terminal veya IDE'nin komut satırı aracılığıyla, bağımlılıkları yüklemek için pip install -r requirements.txt komutunu çalıştırın.
+ Projeyi çalıştırmak için main.py dosyasını bulun ve yürütün.

**Kullanım**
main.py yürütüldüğünde, kullanıcı arayüzü otomatik olarak başlayacak ve hasar tespit sürecini başlatmak için gereken talimatları içerecektir. Arayüz üzerinden hasar görmüş araçların görüntülerini yükleyebilir ve hasar tespitini gerçekleştirebilirsiniz. Sonuçlar, arayüzde görsel işaretlemeler ile birlikte gösterilecektir.

**Notlar**
Proje, belirtilen Python sürümü ve bağımlılıklar ile uyumludur. Farklı bir ortamda çalıştırırken uyumluluk sorunları yaşanabilir.
Projenin düzgün çalışması için YoloModel klasöründeki ağırlıkların ve model dosyalarının eksiksiz olduğundan emin olun.

### Modelimizin Eğitimi
Modelimiz, hasarlı araçların sadece hasar görmüş bölgeleri üzerinde eğitilmiştir. Yani, hasarlı araçların görüntülerinden hasarlı bölge kesilerek modele eğitim verilmiştir. Bu yaklaşım, modelimizin sadece hasarın kendisine odaklanmasını ve arka planın etkilerini minimize etmesini sağlamıştır. Dolayısıyla, modelimize daha iyi bir sonuç elde etmek için tüm resmi değil, sadece hasarlı bölgenin resmini vermek daha uygundur.

### İkinci Model ve Kullanımı
Ayrıca, araçların tüm resimleri ile çalışabilen ve kendi simülasyon ortamımızdan edindiğimiz test görüntüleri ile sorunsuz çalışan ikinci bir model daha eğittik. Bu modeli kullanmak için aşağıdaki adımları izleyin:

1. Bu [drive linkinden](https://drive.google.com/drive/folders/1cYJgyQQ-R286k2X-mUiFPlsOqs5eet8d?usp=drive_link) ikinci modelimizi indirin.
2. İndirdiğiniz model dosyasını YOLOModel klasörüne yerleştirin.
3. detectDamage.py dosyasını açın ve 26. satırdaki model yolu kodunu şu şekilde değiştirin:
  model_path = os.path.join(current_directory, r'yoloModel\best.pt')
4. best.pt adını, indirdiğiniz model dosyasının adıyla değiştirmeyi unutmayın.
Bu adımları tamamladığınızda, ikinci modelimizi kullanarak hasar tespiti yapabilirsiniz.

Projemizin başarılı bir şekilde geliştirilmesi ve uygulanması için emek veren herkese teşekkürler. GitHub üzerindeki repomuzu ziyaret ederek projemiz hakkında daha fazla bilgi edinebilir, geliştirme sürecimize katkıda bulunabilirsiniz.
