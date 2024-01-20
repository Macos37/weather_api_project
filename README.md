## Quick start
Create a .env file for the virtual environment, which will contain the TG_APY_KEY and YANDEX_APY_KEY environment variables.

Docker compose

```sh
docker compose up --build
```
Router

```sh
http://127.0.0.1:8000/weather/?city=<city_name>
```

Telegram bot acts as an interface, enter the text name of the city and receive weather data.
