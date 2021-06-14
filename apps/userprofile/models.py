from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ACCOUNT_TYPE = (('Hedged/Hedging', 'Hedged/Hedging'),
                ('Standart/Netted', 'Standart/Netted'))

SELECT_PAIRS = (('AUD/USD', 'AUD/USD'),
                ('EUR/USD', 'EUR/USD'))


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(default='default-avatar.png', upload_to='users/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    strategy_name = models.CharField(max_length=30, blank=True, null=True)
    equity = models.IntegerField(null=True, blank=True)
    leverage = models.IntegerField(null=True, blank=True)
    account_type = models.CharField(max_length=30, choices=ACCOUNT_TYPE, blank=True, null=True)
    select_pairs = models.CharField(max_length=30, choices=SELECT_PAIRS, blank=True, null=True)
    simulation_start_date = models.DateField(max_length=10, blank=True, null=True)
    most_recent_data = models.BooleanField(blank=True, null=True)
    tick_volume = models.BooleanField(blank=True, null=True)
    min_timeframe = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return '%s' % (self.strategy_name)