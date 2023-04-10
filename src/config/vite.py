import json
from pathlib import Path

from .settings import STATIC_FILES_DIR


class ViteAssetsLoader:
    """Vite assets loader"""

    entry_point_js_file: str = "src/main.ts"
    css_file: str = "src/main.css"

    def load_manifest(self) -> None:
        manifest_file_path = Path(STATIC_FILES_DIR).joinpath("manifest.json")
        with open(file=manifest_file_path, mode="r") as f:
            content = f.read()
        try:
            self.manifest = json.loads(content)
        except Exception:
            raise RuntimeError(
                f"Cannot read Vite manifest file at {manifest_file_path}"
            )

    def generate_css_file_name(self) -> str:
        return self.manifest[self.css_file]["file"]

    def generate_js_file_name(self) -> str:
        return self.manifest[self.entry_point_js_file]["file"]
