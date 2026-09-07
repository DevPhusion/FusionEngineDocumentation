"""
File management
"""
from __future__ import annotations
__all__: list[str] = ['absolute_to_virtual', 'virtual_to_absolute']
def absolute_to_virtual(absolute_path: str) -> str:
    """
    Convert a real filesystem path back into a res:// virtual path, e.g.
      virtual_path = File.absolute_to_virtual(abs_path)
    """
def virtual_to_absolute(virtual_path: str) -> str:
    """
    Resolve a res:// virtual path (as stored by export_file/export_scene) to a real filesystem path, e.g.
      abs_path = File.virtual_to_absolute(self.model_path)
    """
