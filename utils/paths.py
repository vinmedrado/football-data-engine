from pathlib import Path

# ROOT aponta independente de onde o script é chamado
ROOT = Path(__file__).resolve().parents[1]

CONFIG_DIR = ROOT / "config"
OUTPUT_DIR = ROOT / "output"
STATE_DIR  = ROOT / "state"

LEAGUES_FILE = CONFIG_DIR / "leagues.json"
RUN_CONFIG   = CONFIG_DIR / "run_config.json"
BOOKMAKERS   = CONFIG_DIR / "bookmakers.json"

LEAGUES_OUT = OUTPUT_DIR / "leagues"
MATCHES_OUT = OUTPUT_DIR / "matches"
ODDS_OUT    = OUTPUT_DIR / "odds"
PARSED_OUT  = OUTPUT_DIR / "parsed"
FINAL_OUT   = OUTPUT_DIR / "final"

for d in [
    OUTPUT_DIR,
    STATE_DIR,
    LEAGUES_OUT,
    MATCHES_OUT,
    ODDS_OUT,
    PARSED_OUT,
    FINAL_OUT,
]:
    d.mkdir(parents=True, exist_ok=True)