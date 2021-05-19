from . import text_prediction
from .text_prediction import TextPredictor
from .text_prediction.presets import ag_text_presets, list_presets

try:
    from .version import __version__
except ImportError:
    pass
