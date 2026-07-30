BOT_TOKEN = os.getenv("BOT_TOKEN", "")
if not BOT_TOKEN:
    if os.path.exists("/root/.hermes/config.yaml"):
        cfg = open("/root/.hermes/config.yaml").read()
        for line in cfg.splitlines():
            if "bot_token:" in line:
                token = line.split("bot_token:", 1)[1].strip()
                if token:
                    os.environ["BOT_TOKEN"] = token
                    break
