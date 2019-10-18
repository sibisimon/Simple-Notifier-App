from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from notifier.models import UserComment


@receiver(post_save, sender=User)
def broadcast_user(sender, instance, created, **kwargs):
    # Informing consumers when user is created or updated

    channel_layer = get_channel_layer()

    # Defining notification payload
    payload = {"type": "user.echo",
               "user_id": instance.id,
               "username": instance.username,
               "first_name": instance.first_name,
               "last_name": instance.last_name
              }
    if created:
        # User added
        payload["event"] = "New User"
        async_to_sync(channel_layer.group_send)(
            "user", payload)
    else:
        # User updated
        payload["event"] = "User updated"
        async_to_sync(channel_layer.group_send)(
            "user", payload)


@receiver(post_delete, sender=User)
def broadcast_deleted_user(sender, instance, **kwargs):
    # Informing user deleted to the consumers
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "user", {"type": "user.echo",
               "user_id": instance.id,
               "event": "User deleted",
               "username": instance.username,
               "first_name": instance.first_name,
               "last_name": instance.last_name
              })

@receiver(post_save, sender=UserComment)
def broadcast_comment(sender, instance, created, **kwargs):
    # User comment added
    channel_layer = get_channel_layer()
    payload = {"type": "user.echo",
               "comment": instance.comment,
               "username": instance.user.username,
              }
    if created:
        payload["event"] = "New comment"
        async_to_sync(channel_layer.group_send)(
            "user", payload)


