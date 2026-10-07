from django.db import models
from django.utils.text import slugify


# ========================================================




class Conference(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    type = models.CharField(max_length=100)
    content = models.TextField()
    img = models.ImageField(upload_to='imgs/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



# ========================================================


class Shoba(models.Model):
    conference = models.ForeignKey(
        Conference,
        on_delete=models.CASCADE,
        related_name='shobalar'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    img = models.ImageField(upload_to='imgs/')
    maqola_soni = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title



class AboutShoba(models.Model):
    shoba = models.ForeignKey(
        Shoba,
        on_delete=models.CASCADE,
        related_name='about'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    maqola_soni = models.IntegerField(default=0)
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


# ========================================================

class Maqola(models.Model):
    shoba = models.ForeignKey(
        Shoba,
        on_delete=models.CASCADE,
        related_name='maqolalar'
    )
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    yaratilgan_sana = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True)
    word_bet = models.IntegerField(default=0)
    word_fayl = models.FileField(upload_to='word_files/')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class AboutMaqola(models.Model):
    maqola = models.ForeignKey(
        Maqola,
        on_delete=models.CASCADE,
        related_name='about_maqolalar'
    )
    shoba_malumot = models.ForeignKey(
            Shoba,
            on_delete=models.CASCADE,
            related_name='shoba_malumot'
    )
    muallif = models.CharField(max_length=255)
    konfrensiya = models.TextField()
    yaratilgan_sana = models.DateTimeField(auto_now_add=True)
    yangilanish = models.DateTimeField(auto_now=True)
    word_bet = models.IntegerField(default=0)
    word_fayl = models.FileField(upload_to='word_files/')

    def __str__(self):
        return self.maqola.title


# ========================================================

import os
from django.db import models
from .text_from_img import ImageToText  


class WordPart(models.Model):
    conference = models.ForeignKey(
        'Conference',
        on_delete=models.CASCADE,
        related_name='word_parts'
    )
    maqola_soni = models.IntegerField()
    bet_soni = models.IntegerField()
    yaratilgan_sana = models.DateField(auto_now_add=True)
    word_fayl = models.FileField(upload_to='word_files/')
    content = models.TextField(blank=True, null=True)  # blank=True qilishingiz tavsiya etiladi

    def __str__(self):
        return f"{self.conference.title} - Word"

    def save(self, *args, **kwargs):
        # Obyektni avval saqlaymiz (fayl diskka yozilishi uchun)
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # Fayl bor bo'lsa va content bo'sh bo'lsa matnni ajratib olamiz
        if self.word_fayl and not self.content:
            file_path = self.word_fayl.path
            if os.path.exists(file_path):
                try:
                    extractor = ImageToText()
                    text = extractor.extract_txt_from_file(file_path)
                    if text.strip():
                        self.content = text
                        # Faqat content maydonini qayta saqlaymiz
                        super().save(update_fields=['content'])
                except Exception as e:
                    print(f"Fayl matnini o'qishda xatolik: {e}")