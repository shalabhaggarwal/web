# Generated by Django 2.1.1 on 2018-10-09 18:52

from django.db import migrations, models
import django.db.models.deletion
import economy.models
import grants.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dashboard', '0108_auto_20180917_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('tx_id', models.CharField(default='0x0', max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Grant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('status', models.BooleanField(default=True)),
                ('title', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True, default='')),
                ('reference_url', models.URLField(db_index=True)),
                ('image_url', models.URLField(default='')),
                ('logo', models.ImageField(blank=True, help_text='The Grant logo image.', null=True, upload_to=grants.utils.get_upload_filename)),
                ('logo_svg', models.FileField(blank=True, help_text='The Grant logo SVG.', null=True, upload_to=grants.utils.get_upload_filename)),
                ('admin_address', models.CharField(default='0x0', max_length=255)),
                ('frequency', models.DecimalField(decimal_places=0, default=30, max_digits=50)),
                ('amount_goal', models.DecimalField(decimal_places=4, default=1, max_digits=50)),
                ('amount_received', models.DecimalField(decimal_places=4, default=0, max_digits=50)),
                ('token_address', models.CharField(default='0x0', max_length=255)),
                ('contract_address', models.CharField(default='0x0', max_length=255)),
                ('transaction_hash', models.CharField(default='0x0', max_length=255)),
                ('network', models.CharField(default='mainnet', max_length=8)),
                ('required_gas_price', models.DecimalField(decimal_places=0, default='0', max_digits=50)),
                ('admin_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grant_admin', to='dashboard.Profile')),
                ('team_member_profiles', models.ManyToManyField(related_name='grant_team_members', to='dashboard.Profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('status', models.BooleanField(default=True)),
                ('subscription_hash', models.CharField(default='', max_length=255)),
                ('contributor_signature', models.CharField(default='', max_length=255)),
                ('contributor_address', models.CharField(default='', max_length=255)),
                ('amount_per_period', models.DecimalField(decimal_places=4, default=1, max_digits=50)),
                ('token_address', models.CharField(default='0x0', max_length=255)),
                ('gas_price', models.DecimalField(decimal_places=4, default=1, max_digits=50)),
                ('network', models.CharField(default='mainnet', max_length=8)),
                ('contributor_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grant_contributor', to='dashboard.Profile')),
                ('grant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to='grants.Grant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contribution',
            name='subscription',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscription_contribution', to='grants.Subscription'),
        ),
    ]
