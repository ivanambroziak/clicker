from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name="Ім'я користувача")),
                ('message', models.TextField(verbose_name='Повідомлення')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Повідомлення чату',
                'verbose_name_plural': 'Повідомлення чату',
                'ordering': ['timestamp'],
            },
        ),
    ]