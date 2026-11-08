"""Load the shared terminology base and the per-product terminology files.

`foundations/content/terminology/shared.yml` holds the schema, authority model
and shared policy, and lists one file per product under `products`. A product
without a file has no Design Language terminology layer: its labels come only
from its own Product Knowledge, never from another product's file.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
TERMINOLOGY_DIR = ROOT / "foundations" / "content" / "terminology"
SHARED_PATH = TERMINOLOGY_DIR / "shared.yml"
SHARED_ID = "content.foundation.terminology"
# Keys owned by the shared base; product files must not redefine them.
SHARED_KEYS = ("schema_version", "language", "authority_model", "policy", "precedence_source")


def read_yaml(path: Path, loader: type[yaml.SafeLoader] = yaml.SafeLoader) -> Any:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=loader)


def product_files(shared: dict[str, Any]) -> dict[str, Path]:
    products = shared.get("products")
    if not isinstance(products, dict):
        return {}
    return {name: TERMINOLOGY_DIR / str(file) for name, file in products.items()}


def merge(shared: dict[str, Any], product: str, data: dict[str, Any]) -> dict[str, Any]:
    """Return one product's terminology as a single mapping, shared keys from the base."""
    merged = dict(data)
    merged["id"] = shared.get("id")
    merged["product"] = product
    for key in SHARED_KEYS:
        if key in shared:
            merged[key] = shared[key]
    return merged


def load_products(loader: type[yaml.SafeLoader] = yaml.SafeLoader) -> dict[str, dict[str, Any]]:
    """Return {product: merged terminology} for every product with a file."""
    shared = read_yaml(SHARED_PATH, loader) or {}
    return {
        name: merge(shared, name, read_yaml(path, loader) or {})
        for name, path in product_files(shared).items()
        if path.is_file()
    }
