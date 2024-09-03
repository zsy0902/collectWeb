# Generated by Django 4.2.14 on 2024-07-22 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Admin",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=25, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("password", models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name="PicTest",
            fields=[
                ("record_id", models.AutoField(primary_key=True, serialize=False)),
                ("testId", models.CharField(max_length=55)),
                (
                    "testDate",
                    models.CharField(
                        blank=True, default="0000-00-00", max_length=20, null=True
                    ),
                ),
                ("audio", models.BinaryField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="QuestionTest",
            fields=[
                ("record_id", models.AutoField(primary_key=True, serialize=False)),
                ("testId", models.CharField(max_length=55)),
                (
                    "testDate",
                    models.CharField(
                        blank=True, default="0000-00-00", max_length=20, null=True
                    ),
                ),
                ("todayDate", models.IntegerField(blank=True, null=True)),
                ("position", models.IntegerField(blank=True, null=True)),
                ("remember", models.IntegerField(blank=True, null=True)),
                ("calculate", models.IntegerField(blank=True, null=True)),
                ("memorize", models.IntegerField(blank=True, null=True)),
                ("named", models.IntegerField(blank=True, null=True)),
                ("repeating", models.IntegerField(blank=True, null=True)),
                ("commandOperate", models.IntegerField(blank=True, null=True)),
                ("wordOperate", models.IntegerField(blank=True, null=True)),
                ("writing", models.IntegerField(blank=True, null=True)),
                ("draw", models.IntegerField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, max_length=800, null=True)),
                ("audio", models.BinaryField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.CharField(
                        max_length=55, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("password", models.CharField(max_length=25)),
                (
                    "name",
                    models.CharField(
                        default=models.CharField(
                            max_length=55,
                            primary_key=True,
                            serialize=False,
                            unique=True,
                        ),
                        max_length=80,
                    ),
                ),
                ("gender", models.CharField(blank=True, max_length=15, null=True)),
                ("age", models.CharField(blank=True, max_length=20, null=True)),
                ("phonenumber", models.CharField(blank=True, max_length=20, null=True)),
                ("education", models.CharField(blank=True, max_length=80, null=True)),
                ("workout", models.CharField(blank=True, max_length=20, null=True)),
                ("readnwrite", models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
