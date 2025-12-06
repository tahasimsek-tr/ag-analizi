**Dair Ağ Trafiği Analiz Aracı**

Dair, basit bir Python tabanlı ağ tarama aracıdır. ICMP (ping) ve belirli TCP portlarını tarayarak ağınızdaki cihazların durumunu kontrol etmenizi sağlar. Bu araç, siber güvenlik analizleri ve ağ yönetimi için faydalıdır.

**Kurulum**

Gereksinimler

Python 3.x

os, platform, socket, subprocess gibi standart Python kütüphaneleri (varsayılan olarak mevcuttur).


**Kullanım**

Uygulama çalıştırıldığında, tarama yapmak istediğiniz IP adresini girmeniz istenecektir. Ardından, ICMP kontrolü yapılacak ve belirli TCP portları üzerinde tarama gerçekleştirilecektir.


**IP Adresi Formatı**

_Lütfen geçerli bir IP adresi girin. Örneğin:_

192.168.1.10

10.0.0.1


**Notlar**

Uygulama, ağınıza bağlı cihazları taramak için ping ve TCP bağlantılarını kullanır. Bu nedenle ağda yer alan cihazların güvenlik ayarlarını ve izinlerini göz önünde bulundurmanız önemlidir.
Tarama işlemleri, hedef ağ üzerinde herhangi bir olumsuz etki yaratması durumunda kullanılmamalıdır. Tarama izni almadan ağ üzerinde bu tür işlemler gerçekleştirmek, yasal sonuçlar doğurabilir.
Sadece kendi ağlarınızda ve izin verdiğiniz sistemlerde kullanılması önerilir.


**Lisans**

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyin.
