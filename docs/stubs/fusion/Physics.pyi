"""
Physics engine queries
"""
from __future__ import annotations
import collections.abc
import fusion
import typing
__all__: list[str] = ['raycast', 'raycast_all']
def raycast(origin: fusion.Vector3, direction: fusion.Vector3, length: typing.SupportsFloat | typing.SupportsIndex, collision_layer: typing.SupportsInt | typing.SupportsIndex | None = None, ignore_objects: collections.abc.Sequence[Object] = []) -> fusion.RayCastHit:
    """
    Cast a ray and return the closest hit. collision_layer=None hits every layer.
    
    Example:
        ```python
        hit = Physics.raycast(pos, Vector3(0,-1,0), 5.0, CollisionMask.LAYER_1, [self.owner])
        ```
    """
def raycast_all(origin: fusion.Vector3, direction: fusion.Vector3, length: typing.SupportsFloat | typing.SupportsIndex, collision_layer: typing.SupportsInt | typing.SupportsIndex | None = None, ignore_objects: collections.abc.Sequence[Object] = []) -> list[fusion.RayCastHit]:
    """
    Cast a ray and return every hit, sorted nearest-first.
    """
