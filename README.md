**Requeriments**

Python 3.8.3
Django 3.0.7
Django Rest Framework v2.0.0 - https://github.com/encode/django-rest-framework/
MySQL
---

**Endpoints - Allow (GET,POST,PUT,DELETE) **
/realty

	{
        "name": STRING - REQUIRED,
        "address": STRING - REQUIRED,
        "description": STRING - REQUIRED,
        "status": STRING - REQUIRED - VALID OPTIONS(ACTIVE = "1" , INACTIVE = "0"),
        "particulars": STRING - NOT REQUIRED,
        "type": STRING - REQUIRED - VALID OPTIONS(APARTMENT = "AP" , HOME = "HM"),
        "finality": STRING - NOT REQUIRED,
        "real_estate": INTEGER - REQUIRED - ID OF REAL STATE
    }


/real_estate

	{
        "name": STRING - REQUIRED,
        "address": STRING - REQUIRED,
    }

---