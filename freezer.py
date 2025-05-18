from flask_frozen import Freezer
from pathlib import Path
import shutil
import traceback
from app import app

try:
    build_path = Path("build")
    if build_path.exists():
        shutil.rmtree(build_path)
    freezer = Freezer(app)

    if __name__ == "__main__":
        freezer.freeze()
except:
    print(traceback.format_exc())
