# Generated by Django 4.0.5 on 2022-07-04 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_remove_hocphi_hocvien_phuhuynh_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hocphi_hocvien',
            old_name='ngay',
            new_name='ngayDangKy',
        ),
        migrations.RemoveField(
            model_name='hocphi_hocvien',
            name='soChuaThanhToan',
        ),
        migrations.RemoveField(
            model_name='hocphi_hocvien',
            name='soTienDong',
        ),
        migrations.AddField(
            model_name='hocphi_hocvien',
            name='hocPhi',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='DongTien_HocVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngay', models.DateField()),
                ('soTienDong', models.IntegerField()),
                ('ghiChu', models.TextField(blank=True)),
                ('hocVien_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.hocvien')),
            ],
        ),
    ]