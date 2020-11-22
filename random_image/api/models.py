from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Images(models.Model):
    image_id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=200) 
    img = models.ImageField(upload_to='images/')
    flag = models.IntegerField() 

    def save(self, *args, **kwargs):
        if self.url and not self.img:
            img_temp = NamedTemporaryFile(delete=True)
            # img_temp.write(urlopen(self.url).read())
            img_temp.flush()
            self.img.save(f"image_{self.image_id}", File(img_temp))
        super(Images, self).save(*args, **kwargs)

