from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_LINK: str = "t.me/seed_coin_bot/app?startapp=558455838"

    AUTO_UPGRADE_STORAGE: bool = True
    AUTO_UPGRADE_MINING: bool = True
    AUTO_UPGRADE_HOLY: bool = True
    AUTO_CLEAR_TASKS: bool = True
    AUTO_START_HUNT: bool = True

    AUTO_SELL_WORMS: bool = False
    QUANTITY_TO_KEEP: dict = {
        "common": {
            "quantity_to_keep": 3,
            "sale_price": 0.44
        },
        "uncommon": {
            "quantity_to_keep": 3,
            "sale_price": 0.59
        },
        "rare": {
            "quantity_to_keep": 2,
            "sale_price": 2.76
        },
        "epic": {
            "quantity_to_keep": 5,
            "sale_price": 10.5
        },
        "legendary": {
            "quantity_to_keep": 10,
            "sale_price": 100
        }
    }

    USE_PROXY_FROM_FILE: bool = False

settings = Settings()


