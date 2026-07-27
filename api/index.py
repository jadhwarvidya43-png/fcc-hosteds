import os
import sys
from pathlib import Path

# Add src folder to sys.path so free_claude_code imports work seamlessly
src_path = str(Path(__file__).parent.parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from free_claude_code.config.settings import Settings
from free_claude_code.runtime.bootstrap import build_asgi_app

# Instantiate settings and ASGI application for Vercel Serverless Function
settings = Settings()
app = build_asgi_app(settings)
