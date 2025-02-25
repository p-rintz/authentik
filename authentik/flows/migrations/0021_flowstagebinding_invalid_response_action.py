# Generated by Django 3.2.4 on 2021-06-27 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_flows", "0020_flow_compatibility_mode"),
    ]

    operations = [
        migrations.AddField(
            model_name="flowstagebinding",
            name="invalid_response_action",
            field=models.TextField(
                choices=[("retry", "Retry"), ("continue", "Continue")],
                default="retry",
                help_text="Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor while CONTINUE continues with the next stage.",
            ),
        ),
    ]
