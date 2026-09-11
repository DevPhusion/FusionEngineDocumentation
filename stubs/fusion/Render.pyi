"""
Immediate-mode debug drawing
"""
from __future__ import annotations
import collections.abc
import fusion
import typing
__all__: list[str] = ['draw_arrow', 'draw_circle', 'draw_filled_polygon', 'draw_line']
def draw_arrow(origin: fusion.Vector3, direction: fusion.Vector3, length: typing.SupportsFloat | typing.SupportsIndex, color: fusion.Vector4, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0, head_length: typing.SupportsFloat | typing.SupportsIndex = 0.15000000596046448, head_angle_deg: typing.SupportsFloat | typing.SupportsIndex = 25.0, screen_space: bool = False) -> None:
    """
    Draw an arrow from origin along direction (auto-normalized) for one frame.
    
    Example:
        ```python
        Render.draw_arrow(pos, Vector3(0,1,0), 1.5, Vector4(0,1,0,1))
        ```
    """
def draw_circle(center: fusion.Vector3, radius: typing.SupportsFloat | typing.SupportsIndex, color: fusion.Vector4, segments: typing.SupportsInt | typing.SupportsIndex = 32, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0, screen_space: bool = False) -> None:
    """
    Draw a circle outline for one frame.
    
    Example:
        ```python
        Render.draw_circle(pos, 1.0, Vector4(1,1,0,1))
        ```
    """
def draw_filled_polygon(world_points: collections.abc.Sequence[fusion.Vector3], fill_color: fusion.Vector4, outline_color: fusion.Vector4, outline_thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0) -> None:
    """
    Draw a filled, outlined polygon from world-space points (min 3) for one frame.
    
    Example:
        ```python
        Render.draw_filled_polygon(
            [Vector3(0,0,0), Vector3(1,0,0), Vector3(0,1,0)],
            Vector4(1,0,0,0.5), Vector4(1,0,0,1))
        ```
    """
def draw_line(p1: fusion.Vector3, p2: fusion.Vector3, color: fusion.Vector4, thickness: typing.SupportsFloat | typing.SupportsIndex = 1.0, screen_space: bool = False) -> None:
    """
    Draw a line between two world-space points for one frame.
    
    Example:
        ```python
        Render.draw_line(Vector3(0,0,0), Vector3(1,1,0), Vector4(1,0,0,1))
        ```
    """
