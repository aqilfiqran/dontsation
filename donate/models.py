from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.conf import settings
# Create your models here.


class DonateArticle(models.Model):
    title = models.CharField(_('Judul Berita'), max_length=100)
    ctype = (
        ('Disabilitas', 'disabilitas'),
        ('Panti Asuhan', 'panti asuhan'),
        ('Panti Jompo', 'panti jompo'),
    )
    category = models.CharField(_("Kategori"), max_length=100, choices=ctype)
    categoryslug = models.SlugField(editable=False)
    target = models.IntegerField(_('Donasi yang diperlukan'))
    receive = models.IntegerField(_('Donasi yang diterima'), editable=False)
    image = models.ImageField(_("Gambar"), upload_to='donate')
    description = models.TextField(_("Deskripsi"))
    slug = models.SlugField(editable=False)
    update = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default=1)

    def save(self):
        self.slug = slugify(self.title)
        self.categoryslug = slugify(self.category)
        super(DonateArticle, self).save()

    def __str__(self):
        return '{}. {}'.format(self.id, self.title)


class Donate(models.Model):
    name = models.CharField(_("Nama"), max_length=100)
    email = models.EmailField(_('Email'), unique=True)
    donation = models.IntegerField(_("Donasi"))
    confirmation = models.IntegerField(_("Konfirmasi"), editable=False)
    verify = models.IntegerField(_("Verifikasi Email"), editable=False)
    donateArticle = models.ForeignKey(
        DonateArticle, on_delete=models.CASCADE, editable=False)
    barcode = models.CharField(_("QrCode"), max_length=200)

    def __str__(self):
        return '{}. {} mendonasikan Rp.{}'.format(self.id, self.name, self.donation)
