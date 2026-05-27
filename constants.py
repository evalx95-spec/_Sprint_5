BASE_URLS = {
    "prod": "https://qa-desk.education-services.ru/",
    "staging": "https://staging.qa-desk.education-services.ru/",
    "dev": "http://localhost:3000/",
    "qa": "https://qa.qa-desk.education-services.ru/"
}


CURRENT_ENV = "prod"  
BASE_URL = BASE_URLS[CURRENT_ENV]


ENDPOINTS = {
    "login": "/login",
    "dashboard": "/dashboard",
    "ads": "/ads",
    "profile": "/profile",
    "api_users": "/api/v1/users",
    "api_ads": "/api/v1/ads"
}

FULL_URLS = {
    "login": BASE_URL + ENDPOINTS["login"],
    "dashboard": BASE_URL + ENDPOINTS["dashboard"],
    "ads": BASE_URL + ENDPOINTS["ads"],
    "profile": BASE_URL + ENDPOINTS["profile"]
    }
