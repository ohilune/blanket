import json
from pathlib import Path
from logging import getLogger

logger = getLogger(__name__)

DEFAULT_CONFIG = {
    'project_name': 'Untitled Project',
    'fps': 24,
    'resolution': '1920x1080'
}


def load_config():
    return ''
