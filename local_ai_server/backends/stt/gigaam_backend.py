from __future__ import annotations

from typing import Any, Dict, Optional

from backends.interface import STTBackendInterface


class GigaamBackend(STTBackendInterface):
    def __init__(self):
        self._model = None

    @classmethod
    def name(cls) -> str:
        return "gigaam"

    @classmethod
    def config_schema(cls) -> Dict[str, Any]:
        return {
            "model_name": {"type": "string", "required": False, "default": "v3_e2e_rnnt", "description": "GigaAM model variant"},
            "device": {"type": "string", "required": False, "default": "cpu", "enum": ["cpu", "cuda"]},
        }

    @classmethod
    def is_available(cls) -> bool:
        try:
            import gigaam
            return True
        except ImportError:
            return False

    def initialize(self, config: Dict[str, Any]) -> None:
        pass

    def shutdown(self) -> None:
        self._model = None

    def process_audio(self, audio_bytes: bytes) -> Optional[str]:
        return None

    def status(self) -> Dict[str, Any]:
        return {"backend": "gigaam", "loaded": self._model is not None}
