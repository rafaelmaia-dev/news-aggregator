from src.config import Settings, settings


# Test parse_schedule()
def test_parse_schedule_with_string() -> str:
    result = Settings.parse_schedule("00:00", "18:00")


# Second method 
# Simula o .env na memória, sem arquivo real
def test_settings_env_mock():
    settings = Settings(
        DIGEST_SCHEDULE="08:00, 18:00",
        TELEGRAM_BOT_TOKEN="fake",
        TELEGRAM_CHAT_ID=,
        GROQ_API_KEY="",
        DATABASE_URL="",
        DIGEST_MAX_ARTICLES=
    )


t1 = test_parse_schedule_with_string()
print(t1)