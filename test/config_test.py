import sys
from pathlib import Path

# Make the project root importable when run as `python test/config_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.config import settings

s = settings()
key = s.aws_access_key_id
print(f"AWS Access Key ID: {key[:4]}...{key[-4:]}" if key else "AWS Access Key ID: <not set>")
print(f"AWS Region: {s.aws_region}")
