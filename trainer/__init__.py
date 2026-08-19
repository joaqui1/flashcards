"""Trainer package initialization."""

# Apply the practical curriculum extensions before other trainer modules import
# the shared catalog. The extension is idempotent and keeps cards.py as the base deck.
from . import curriculum as _curriculum  # noqa: F401
