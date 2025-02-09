import os
__import__("pysqlite3")
import sys  # noqa: E402

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = "KEEP_ME_SECRET_PLEASE"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = False

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

INSTALLED_APPS = ("db",)
