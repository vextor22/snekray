from dotenv import load_dotenv

load_dotenv(override=True)

import os

print(os.environ.get("PYTHONPATH", "none"))
from praytracer import PRay


tracer = PRay()

print(f"Render at: {tracer.get_dimensions()}")
