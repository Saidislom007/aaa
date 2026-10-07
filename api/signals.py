import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import WordPart
from .text_from_img import ImageToText  # ImageToText classi joylashgan faylingizdan import qiling


@receiver(post_save, sender=WordPart)
def extract_content_from_word_file(sender, instance, created, **kwargs):
    """WordPart saqlanganda word_fayl dan matnni ajratib olib, content field'iga yozadi."""
    
    # Agar fayl mavjud bo'lsa va content hali to'ldirilmagan bo'lsa (yoki yangilanishi kerak bo'lsa)
    if instance.word_fayl and not instance.content:
        file_path = instance.word_fayl.path
        
        # Fayl diskda mavjudligini e'lon qilamiz
        if os.path.exists(file_path):
            try:
                # TextExtractor classidan foydalanamiz
                extractor = ImageToText()
                extracted_text = extractor.extract_txt_from_file(file_path)
                
                # Agar matn topilgan bo'lsa, kontentni yangilaymiz
                if extracted_text.strip():
                    instance.content = extracted_text
                    
                    # Cheksiz rekurtsiyaga tushmaslik uchun faqat 'content' maydonini update qilamiz
                    instance.save(update_fields=['content'])
            except Exception as e:
                print(f"Matnni ajratib olishda xatolik yuz berdi: {e}")