"""
Fusion engine scripting API
"""
from __future__ import annotations
import collections.abc
import typing
from . import File
from . import Key
from . import Mouse
from . import Physics
from . import RL
from . import Render
__all__: list[str] = ['AgentComponent', 'CameraComponent', 'CircleShape', 'CollisionComponent', 'CollisionEventData', 'CollisionLayer', 'CollisionMask', 'CollisionType', 'Console', 'Constraint', 'ConstraintComponent', 'DistanceConstraint', 'File', 'FluidComponent', 'FluidParticle', 'FluidVsRigid', 'FluidVsSoft', 'FractureComponent', 'Input', 'Key', 'Mouse', 'Object', 'Physics', 'PointMass', 'PolygonShape', 'PrismaticConstraint', 'RL', 'RayCastHit', 'RectangleShape', 'Render', 'RenderComponent', 'RevoluteConstraint', 'RigidBodyComponent', 'RigidVsRigid', 'RigidVsSoft', 'RigidVsStatic', 'Script', 'SoftBodyComponent', 'SoftVsSoft', 'SpringConstraint', 'StaticVsStatic', 'TransformComponent', 'Vector2', 'Vector3', 'Vector4', 'WeldConstraint', 'add_scene', 'export', 'export_angle_slider', 'export_color_edit', 'export_color_picker', 'export_drag', 'export_file', 'export_range', 'export_scene', 'export_section', 'export_sub_section', 'find_objects_with_component', 'get_all_objects', 'get_script', 'layer_overlap', 'lerp', 'load_scene']
class AgentComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    @typing.overload
    def add_observation(self, value: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Append a single float to this frame's observation vector
        """
    @typing.overload
    def add_observation(self, values: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        """
        Append multiple floats to this frame's observation vector
        """
    def add_reward(self, delta: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Add delta to this episode's accumulated reward
        """
    def clear_observation(self) -> None:
        """
        Clear the observation vector accumulated so far this frame
        """
    def end_episode(self) -> None:
        """
        Mark the current episode as done, ending the RL rollout on the next step
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_action_space(self, space: typing.Any) -> None:
        """
        Set this agent's action space to any gymnasium.spaces.Space instance (Discrete, Box, MultiDiscrete, MultiBinary).
        
        Example:
            ```python
            from gymnasium import spaces
            self.agent.set_action_space(spaces.MultiDiscrete([3, 2, 2]))
            ```
        Must be called (e.g. from OnStart) before training or inference.
        """
    def set_observation(self, values: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        """
        Replace this frame's entire observation vector
        """
    def set_observation_space(self, space: typing.Any) -> None:
        """
        Optional. Override the observation space with any gymnasium.spaces.Space. If not set, a Box inferred from the length of accumulated add_observation() values is used automatically (previous default behavior).
        """
    def set_reward(self, value: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Overwrite this step's reward with value
        """
    @property
    def action(self) -> typing.Any:
        """
        The most recent action, in whatever type matches the configured action_space (int for Discrete, list for Box/MultiDiscrete/MultiBinary).
        
        Example:
            ```python
            move_idx, jump, shoot = self.agent.action  # MultiDiscrete([3, 2, 2])
            ```
        """
    @property
    def action_space(self) -> typing.Any:
        """
        The gymnasium.spaces.Space configured via set_action_space()
        """
    @property
    def agent_id(self) -> int:
        """
        Unique id of this agent, used to key per-agent training state
        """
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def observation_space(self) -> typing.Any:
        """
        The gymnasium.spaces.Space configured via set_observation_space(), or None if unset
        """
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
class CameraComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def get_range(self) -> float:
        """
        Get range. See the range property.
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_enable(self, enable: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_is_main(self, is_main: bool) -> None:
        """
        Set is_main. See the is_main property.
        """
    def set_range(self, range: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set range. See the range property.
        """
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def is_main(self) -> bool:
        """
        Whether this is the active/main camera. Setting this to True on one camera does not automatically unset another camera's is_main.
        """
    @is_main.setter
    def is_main(self, arg1: bool) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def range(self) -> float:
        """
        Visible extent (view size/zoom) of the camera
        """
    @range.setter
    def range(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class CircleShape:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, center: Vector3, radius: typing.SupportsFloat | typing.SupportsIndex, segments: typing.SupportsInt | typing.SupportsIndex = 30, physics_segments: typing.SupportsInt | typing.SupportsIndex = 30) -> None:
        ...
    @property
    def center(self) -> Vector3:
        """
        Local-space center of the circle
        """
    @center.setter
    def center(self, arg0: Vector3) -> None:
        ...
    @property
    def radius(self) -> float:
        """
        Radius of the circle in local units
        """
    @radius.setter
    def radius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def segments(self) -> int:
        """
        Number of segments used to render the circle's outline
        """
    @segments.setter
    def segments(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CollisionComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_collision_callback(self, callback: collections.abc.Callable) -> int:
        """
        Fires every physics substep while two shapes are overlapping. Returns an id usable with remove_collision_callback().
        """
    def add_collision_enter_callback(self, callback: collections.abc.Callable) -> int:
        """
        Fires once on the frame a collision first begins.
        """
    def add_collision_exit_callback(self, callback: collections.abc.Callable) -> int:
        """
        Fires once on the frame a collision stops.
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def add_shape(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape, name: str = '') -> int:
        """
        Add a new collision shape to this component. Returns its shape_id.
        
        Example:
            ```python
            sid = col.add_shape(CircleShape(Vector3(0,0,0), 1.0), 'Detector')
            ```
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def get_resolution_shape_id(self) -> int:
        """
        Get resolution_shape_id. See the resolution_shape_id property.
        """
    def get_shape(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape:
        """
        Get the Shape object for the shape with the given id
        """
    def get_shape_area(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> float:
        """
        Area of the shape with the given id, in world units squared
        """
    def get_shape_center(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> Vector3:
        """
        World-space center of the shape with the given id
        """
    def get_shape_id(self, name: str) -> int:
        """
        Look up a shape's id by its name (as set in the inspector or via set_shape_name). Returns -1 if no shape has that name.
        
        Example:
            ```python
            detector_id = self.cc.get_shape_id('Aggro Radius')
            ```
        """
    def get_shape_ids(self) -> list[int]:
        """
        Returns the ids of every collision shape on this component
        """
    def get_shape_name(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> str:
        """
        Get the display name of the shape with the given id
        """
    def get_sync_with_render_component(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        Whether the shape with the given id mirrors the RenderComponent shape
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def is_grounded(self, probe_length: typing.SupportsFloat | typing.SupportsIndex = 0.15000000596046448) -> bool:
        """
        Cast a short ray straight down from the lowest point of this shape to check for ground
        """
    def remove_collision_callback(self, id: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Unregister a callback previously registered with add_collision_callback()
        """
    def remove_collision_enter_callback(self, id: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Unregister a callback previously registered with add_collision_enter_callback()
        """
    def remove_collision_exit_callback(self, id: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Unregister a callback previously registered with add_collision_exit_callback()
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def remove_shape(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Remove a collision shape by id, as returned by add_shape()
        """
    def set_collision_layer(self, layer: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set collision_layer. See the collision_layer property.
        """
    def set_collision_mask(self, mask: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set collision_mask. See the collision_mask property.
        """
    def set_enable(self, arg0: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_resolution_shape_id(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Pass -1 for None: shapes stay collidable for detection, but nothing is physically resolved.
        """
    @typing.overload
    def set_shape(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape) -> None:
        """
        Accepts a RectangleShape, CircleShape, or PolygonShape. Applies to the resolution shape (or the first shape if none is set as resolution).
        """
    @typing.overload
    def set_shape(self, shape_id: typing.SupportsInt | typing.SupportsIndex, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape) -> None:
        """
        Replace the shape stored under the given shape_id
        """
    def set_shape_name(self, shape_id: typing.SupportsInt | typing.SupportsIndex, name: str) -> None:
        """
        Rename the shape with the given id
        """
    def set_static(self, is_static: bool) -> None:
        """
        Set is_static. See the is_static property.
        """
    @typing.overload
    def set_sync_with_render_component(self, sync: bool) -> None:
        """
        Set sync_with_render_component. See the sync_with_render_component property.
        """
    @typing.overload
    def set_sync_with_render_component(self, shape_id: typing.SupportsInt | typing.SupportsIndex, sync: bool) -> None:
        """
        Set whether the shape with the given id mirrors the RenderComponent shape
        """
    @property
    def collision_layer(self) -> int:
        """
        CollisionLayer bit flags describing what this object is. Combined with other objects' collision_mask to decide whether they collide.
        """
    @collision_layer.setter
    def collision_layer(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def collision_mask(self) -> int:
        """
        CollisionMask bit flags describing which layers this object collides with
        """
    @collision_mask.setter
    def collision_mask(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def is_static(self) -> bool:
        """
        Whether this object is treated as immovable for collision resolution (other bodies collide against it, but it is never pushed)
        """
    @is_static.setter
    def is_static(self, arg1: bool) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def resolution_shape_id(self) -> int:
        """
        Id of the shape used for physical collision resolution. -1 means None: shapes stay collidable for detection, but nothing is physically resolved.
        """
    @resolution_shape_id.setter
    def resolution_shape_id(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def shape(self) -> fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape:
        """
        The resolution shape used for physical collision response. Equivalent to calling set_shape() with no shape_id.
        """
    @shape.setter
    def shape(self, arg1: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape) -> None:
        ...
    @property
    def sync_with_render_component(self) -> bool:
        """
        Whether the resolution shape (or the first shape if none is set as resolution) automatically mirrors this object's RenderComponent shape. When True, calling set_shape() on that shape will be overridden on the next sync.
        """
    @sync_with_render_component.setter
    def sync_with_render_component(self, arg1: bool) -> None:
        ...
class CollisionEventData:
    """
    Snapshot of a single collision, passed to callbacks registered via CollisionComponent.add_collision_callback() and friends.
    """
    def __repr__(self) -> str:
        ...
    @property
    def normal(self) -> Vector3:
        """
        World-space contact normal, pointing away from self
        """
    @property
    def other(self) -> Object:
        """
        The other Object involved in the collision
        """
    @property
    def other_shape_id(self) -> int:
        """
        Id of the colliding shape on other
        """
    @property
    def penetration(self) -> float:
        """
        Overlap depth along the contact normal, in world units
        """
    @property
    def point(self) -> Vector3:
        """
        World-space contact point
        """
    @property
    def self(self) -> Object:
        """
        The Object whose CollisionComponent this callback is registered on
        """
    @property
    def shape_id(self) -> int:
        """
        Id of the colliding shape on self, as returned by CollisionComponent.add_shape()
        """
    @property
    def type(self) -> CollisionType:
        """
        The CollisionType (RigidVsRigid, RigidVsSoft, etc.) of this collision
        """
class CollisionLayer:
    """
    Collision layer bit flags. Combine multiple with |, e.g. CollisionLayer.LAYER_1 | CollisionLayer.LAYER_3
    
    Members:
    
      LAYER_1
    
      LAYER_2
    
      LAYER_3
    
      LAYER_4
    
      LAYER_5
    
      LAYER_6
    
      LAYER_7
    
      LAYER_8
    
      LAYER_9
    
      LAYER_10
    
      LAYER_11
    
      LAYER_12
    
      LAYER_13
    
      LAYER_14
    
      LAYER_15
    
      LAYER_16
    """
    LAYER_1: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_1: 1>
    LAYER_10: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_10: 512>
    LAYER_11: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_11: 1024>
    LAYER_12: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_12: 2048>
    LAYER_13: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_13: 4096>
    LAYER_14: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_14: 8192>
    LAYER_15: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_15: 16384>
    LAYER_16: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_16: 32768>
    LAYER_2: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_2: 2>
    LAYER_3: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_3: 4>
    LAYER_4: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_4: 8>
    LAYER_5: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_5: 16>
    LAYER_6: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_6: 32>
    LAYER_7: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_7: 64>
    LAYER_8: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_8: 128>
    LAYER_9: typing.ClassVar[CollisionLayer]  # value = <CollisionLayer.LAYER_9: 256>
    __members__: typing.ClassVar[dict[str, CollisionLayer]]  # value = {'LAYER_1': <CollisionLayer.LAYER_1: 1>, 'LAYER_2': <CollisionLayer.LAYER_2: 2>, 'LAYER_3': <CollisionLayer.LAYER_3: 4>, 'LAYER_4': <CollisionLayer.LAYER_4: 8>, 'LAYER_5': <CollisionLayer.LAYER_5: 16>, 'LAYER_6': <CollisionLayer.LAYER_6: 32>, 'LAYER_7': <CollisionLayer.LAYER_7: 64>, 'LAYER_8': <CollisionLayer.LAYER_8: 128>, 'LAYER_9': <CollisionLayer.LAYER_9: 256>, 'LAYER_10': <CollisionLayer.LAYER_10: 512>, 'LAYER_11': <CollisionLayer.LAYER_11: 1024>, 'LAYER_12': <CollisionLayer.LAYER_12: 2048>, 'LAYER_13': <CollisionLayer.LAYER_13: 4096>, 'LAYER_14': <CollisionLayer.LAYER_14: 8192>, 'LAYER_15': <CollisionLayer.LAYER_15: 16384>, 'LAYER_16': <CollisionLayer.LAYER_16: 32768>}
    def __and__(self, arg0: CollisionLayer) -> CollisionLayer:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> CollisionLayer:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, arg0: CollisionLayer) -> CollisionLayer:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, arg0: CollisionLayer) -> CollisionLayer:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CollisionMask:
    """
    Collision mask bit flags. Combine multiple with |, e.g. CollisionMask.LAYER_1 | CollisionMask.LAYER_3
    
    Members:
    
      LAYER_1
    
      LAYER_2
    
      LAYER_3
    
      LAYER_4
    
      LAYER_5
    
      LAYER_6
    
      LAYER_7
    
      LAYER_8
    
      LAYER_9
    
      LAYER_10
    
      LAYER_11
    
      LAYER_12
    
      LAYER_13
    
      LAYER_14
    
      LAYER_15
    
      LAYER_16
    """
    LAYER_1: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_1: 1>
    LAYER_10: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_10: 512>
    LAYER_11: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_11: 1024>
    LAYER_12: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_12: 2048>
    LAYER_13: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_13: 4096>
    LAYER_14: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_14: 8192>
    LAYER_15: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_15: 16384>
    LAYER_16: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_16: 32768>
    LAYER_2: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_2: 2>
    LAYER_3: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_3: 4>
    LAYER_4: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_4: 8>
    LAYER_5: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_5: 16>
    LAYER_6: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_6: 32>
    LAYER_7: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_7: 64>
    LAYER_8: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_8: 128>
    LAYER_9: typing.ClassVar[CollisionMask]  # value = <CollisionMask.LAYER_9: 256>
    __members__: typing.ClassVar[dict[str, CollisionMask]]  # value = {'LAYER_1': <CollisionMask.LAYER_1: 1>, 'LAYER_2': <CollisionMask.LAYER_2: 2>, 'LAYER_3': <CollisionMask.LAYER_3: 4>, 'LAYER_4': <CollisionMask.LAYER_4: 8>, 'LAYER_5': <CollisionMask.LAYER_5: 16>, 'LAYER_6': <CollisionMask.LAYER_6: 32>, 'LAYER_7': <CollisionMask.LAYER_7: 64>, 'LAYER_8': <CollisionMask.LAYER_8: 128>, 'LAYER_9': <CollisionMask.LAYER_9: 256>, 'LAYER_10': <CollisionMask.LAYER_10: 512>, 'LAYER_11': <CollisionMask.LAYER_11: 1024>, 'LAYER_12': <CollisionMask.LAYER_12: 2048>, 'LAYER_13': <CollisionMask.LAYER_13: 4096>, 'LAYER_14': <CollisionMask.LAYER_14: 8192>, 'LAYER_15': <CollisionMask.LAYER_15: 16384>, 'LAYER_16': <CollisionMask.LAYER_16: 32768>}
    def __and__(self, arg0: CollisionMask) -> CollisionMask:
        ...
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> CollisionMask:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __or__(self, arg0: CollisionMask) -> CollisionMask:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    def __xor__(self, arg0: CollisionMask) -> CollisionMask:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CollisionType:
    """
    The kind of bodies involved in a collision, as reported on CollisionEventData.type
    
    Members:
    
      RigidVsRigid
    
      RigidVsStatic
    
      StaticVsStatic
    
      RigidVsSoft
    
      SoftVsSoft
    
      FluidVsRigid
    
      FluidVsSoft
    """
    FluidVsRigid: typing.ClassVar[CollisionType]  # value = <CollisionType.FluidVsRigid: 5>
    FluidVsSoft: typing.ClassVar[CollisionType]  # value = <CollisionType.FluidVsSoft: 6>
    RigidVsRigid: typing.ClassVar[CollisionType]  # value = <CollisionType.RigidVsRigid: 0>
    RigidVsSoft: typing.ClassVar[CollisionType]  # value = <CollisionType.RigidVsSoft: 3>
    RigidVsStatic: typing.ClassVar[CollisionType]  # value = <CollisionType.RigidVsStatic: 1>
    SoftVsSoft: typing.ClassVar[CollisionType]  # value = <CollisionType.SoftVsSoft: 4>
    StaticVsStatic: typing.ClassVar[CollisionType]  # value = <CollisionType.StaticVsStatic: 2>
    __members__: typing.ClassVar[dict[str, CollisionType]]  # value = {'RigidVsRigid': <CollisionType.RigidVsRigid: 0>, 'RigidVsStatic': <CollisionType.RigidVsStatic: 1>, 'StaticVsStatic': <CollisionType.StaticVsStatic: 2>, 'RigidVsSoft': <CollisionType.RigidVsSoft: 3>, 'SoftVsSoft': <CollisionType.SoftVsSoft: 4>, 'FluidVsRigid': <CollisionType.FluidVsRigid: 5>, 'FluidVsSoft': <CollisionType.FluidVsSoft: 6>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Console:
    """
    Prints messages to the in-editor console. All methods are static — call them directly on the class, e.g. Console.Print("hello").
    """
    @staticmethod
    def Print(value: typing.Any) -> None:
        """
        Log an informational message to the console. value is converted with str().
        """
    @staticmethod
    def PrintError(value: typing.Any) -> None:
        """
        Log an error message to the console. value is converted with str().
        """
    @staticmethod
    def PrintWarning(value: typing.Any) -> None:
        """
        Log a warning message to the console. value is converted with str().
        """
class Constraint:
    """
    Base class for physics constraints (DistanceConstraint, SpringConstraint, RevoluteConstraint, WeldConstraint, PrismaticConstraint). Not constructed directly.
    """
    def __repr__(self) -> str:
        ...
    def get_attach_world_a(self) -> Vector3:
        """
        World-space position of attach_point_a, given Object A's current transform
        """
    def get_attach_world_b(self) -> Vector3:
        """
        World-space position of attach_point_b, given Object B's current transform
        """
    def set_beta(self, beta: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set beta. See the beta property.
        """
    def set_draw_constraint(self, draw_constraint: bool) -> None:
        """
        Set draw_constraint. See the draw_constraint property.
        """
    def set_object_a(self, object: Object) -> None:
        """
        Change the owning object (Object A). Attach point resets to that object's center.
        """
    def set_object_b(self, object: Object) -> None:
        """
        Change the other object (Object B), or None to detach it. Attach point resets to that object's center.
        """
    @property
    def attach_point_a(self) -> Vector3:
        """
        Local-space attach point on Object A. Setting this disables use_center_a.
        """
    @attach_point_a.setter
    def attach_point_a(self, arg1: Vector3) -> None:
        ...
    @property
    def attach_point_b(self) -> Vector3:
        """
        Local-space attach point on Object B. Setting this disables use_center_b.
        """
    @attach_point_b.setter
    def attach_point_b(self, arg1: Vector3) -> None:
        ...
    @property
    def beta(self) -> float:
        """
        Baumgarte position-correction factor (0-1). Higher values correct constraint drift faster but can introduce jitter.
        """
    @beta.setter
    def beta(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def draw_constraint(self) -> bool:
        """
        Whether to draw this constraint's debug visualization in the editor/game view
        """
    @draw_constraint.setter
    def draw_constraint(self, arg1: bool) -> None:
        ...
    @property
    def name(self) -> str:
        """
        The constraint's type name, e.g. 'DistanceConstraint'
        """
    @property
    def object_a(self) -> Object:
        """
        The first Object this constraint is attached to
        """
    @property
    def object_b(self) -> Object:
        """
        The second Object this constraint is attached to, or None
        """
    @property
    def use_center_a(self) -> bool:
        """
        Whether Object A's attach point tracks its RenderComponent center automatically. Setting this to True immediately snaps attach_point_a to that center; setting attach_point_a directly turns this back off.
        """
    @use_center_a.setter
    def use_center_a(self, arg1: bool) -> None:
        ...
    @property
    def use_center_b(self) -> bool:
        """
        Whether Object B's attach point tracks its RenderComponent center automatically. Setting this to True immediately snaps attach_point_b to that center; setting attach_point_b directly turns this back off.
        """
    @use_center_b.setter
    def use_center_b(self, arg1: bool) -> None:
        ...
class ConstraintComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_constraint(self, constraint: Constraint) -> None:
        """
        Register a constraint (e.g. a DistanceConstraint) with this object and the physics engine.
        
        Example:
            ```python
            cc.add_constraint(DistanceConstraint(self.owner, target, 5.0))
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_constraint_count(self) -> int:
        """
        Number of constraints this object owns
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    @typing.overload
    def remove_constraint(self, constraint: Constraint) -> None:
        """
        Remove a constraint by reference
        """
    @typing.overload
    def remove_constraint(self, index: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Remove a constraint by its index in constraints
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    @property
    def constraints(self) -> list[Constraint]:
        """
        Constraints this object owns (as Object A)
        """
    @property
    def mirrored_constraints(self) -> list[Constraint]:
        """
        Constraints another object owns where this object is Object B. Read-only from here — modify them via their owner's ConstraintComponent instead.
        """
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
class DistanceConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, distance: typing.SupportsFloat | typing.SupportsIndex, object_b: Object = None, extendable: bool = False, retractable: bool = False) -> None:
        """
        Create a distance constraint attached at object_a's and object_b's centers by default. Not part of the scene until passed to ConstraintComponent.add_constraint().
        
        Example:
            ```python
            dc = DistanceConstraint(self.owner, target, 5.0)
            cc = self.add_component(ConstraintComponent)
            cc.add_constraint(dc)
            ```
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, distance: typing.SupportsFloat | typing.SupportsIndex, extendable: bool = False, retractable: bool = False) -> None:
        """
        Create a distance constraint at explicit local-space attach points on each object (pass Vector3(0,0,0) for object_b's attach point if object_b is None).
        
        Example:
            ```python
            dc = DistanceConstraint(self.owner, target, Vector3(0.5, 0, 0), Vector3(0, 0, 0), 5.0)
            cc = self.add_component(ConstraintComponent)
            cc.add_constraint(dc)
            ```
        """
    def set_distance(self, distance: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set distance. See the distance property.
        """
    def set_extendable(self, extendable: bool) -> None:
        """
        Set extendable. See the extendable property.
        """
    def set_retractable(self, retractable: bool) -> None:
        """
        Set retractable. See the retractable property.
        """
    @property
    def distance(self) -> float:
        """
        Target distance the constraint tries to maintain between its two attach points
        """
    @distance.setter
    def distance(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def extendable(self) -> bool:
        """
        If True, the two bodies may move further apart than distance (rope-like); the constraint only resists moving closer
        """
    @extendable.setter
    def extendable(self, arg1: bool) -> None:
        ...
    @property
    def retractable(self) -> bool:
        """
        If True, the two bodies may move closer than distance (rod pushing only); the constraint only resists moving further apart
        """
    @retractable.setter
    def retractable(self, arg1: bool) -> None:
        ...
class FluidComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    @typing.overload
    def add_particle(self, world_position: Vector3) -> FluidParticle:
        """
        Add a single fluid particle at the given world position.
        
        Example:
            ```python
            p = fluid.add_particle(Vector3(0, 2, 0))
            ```
        """
    @typing.overload
    def add_particle(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape, particle_count: typing.SupportsInt | typing.SupportsIndex) -> list[FluidParticle]:
        """
        Seed roughly particle_count particles filling the given shape and add them to the fluid.
        
        Example:
            ```python
            fluid.add_particle(CircleShape(Vector3(0, 3, 0), 1.5), 200)
            ```
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def get_particle(self, index: typing.SupportsInt | typing.SupportsIndex) -> FluidParticle:
        """
        Get a particle by index
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def remove_particle(self, particle: FluidParticle) -> None:
        """
        Remove and delete a specific FluidParticle previously returned by add_particle(), particles, or get_particle()
        """
    def reseed(self) -> None:
        """
        Discard all particles (including manually added ones) and re-fill the shape according to desired_particle_count
        """
    def set_collision_radius(self, collision_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set collision_radius. See the collision_radius property.
        """
    def set_color(self, color: Vector4) -> None:
        """
        Set color. See the color property.
        """
    def set_desired_particle_count(self, desired_particle_count: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Changing this re-seeds the whole fluid on its source shape, discarding any particles added individually via add_particle()
        """
    def set_enable(self, arg0: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_epsilon(self, epsilon: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set epsilon. See the epsilon property.
        """
    def set_metaball_edge_soft(self, metaball_edge_soft: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set metaball_edge_soft. See the metaball_edge_soft property.
        """
    def set_metaball_threshold(self, metaball_threshold: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set metaball_threshold. See the metaball_threshold property.
        """
    def set_outline_color(self, outline_color: Vector4) -> None:
        """
        Set outline_color. See the outline_color property.
        """
    def set_outline_width_texels(self, outline_width_texels: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set outline_width_texels. See the outline_width_texels property.
        """
    def set_particle_mass(self, particle_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set particle_mass. See the particle_mass property.
        """
    def set_particle_radius(self, particle_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set particle_radius. See the particle_radius property.
        """
    def set_rest_density(self, rest_density: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set rest_density. See the rest_density property.
        """
    def set_smoothing_radius(self, smoothing_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set smoothing_radius. See the smoothing_radius property.
        """
    def set_viscosity(self, viscosity: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set viscosity. See the viscosity property.
        """
    def set_vorticity_strength(self, vorticity_strength: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set vorticity_strength. See the vorticity_strength property.
        """
    def update_collision_layer_mask(self) -> None:
        """
        Sync every particle's collision_layer/collision_mask with this Object's CollisionComponent
        """
    @property
    def collision_radius(self) -> float:
        """
        Physical collision radius applied to every particle. Clamped to a small positive minimum. Distinct from particle_radius, which is purely visual.
        """
    @collision_radius.setter
    def collision_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def color(self) -> Vector4:
        """
        Fill color (RGBA, 0-1) of the rendered fluid surface
        """
    @color.setter
    def color(self, arg1: Vector4) -> None:
        ...
    @property
    def desired_particle_count(self) -> int:
        """
        Number of particles to seed when filling the source shape. Changing this re-seeds the whole fluid, discarding any particles added individually via add_particle().
        """
    @desired_particle_count.setter
    def desired_particle_count(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def epsilon(self) -> float:
        """
        Relaxation parameter (CFM) for the position-based fluid solver, used to prevent numerical instability in the density constraint
        """
    @epsilon.setter
    def epsilon(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def metaball_edge_soft(self) -> float:
        """
        Softness of the metaball surface edge falloff. Higher values give a more gradual, blurred edge.
        """
    @metaball_edge_soft.setter
    def metaball_edge_soft(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def metaball_threshold(self) -> float:
        """
        Density threshold at which the metaball surface renderer considers the fluid 'present'. Lower values merge particles into a smoother blob.
        """
    @metaball_threshold.setter
    def metaball_threshold(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def outline_color(self) -> Vector4:
        """
        Color (RGBA, 0-1) of the fluid's rendered outline
        """
    @outline_color.setter
    def outline_color(self, arg1: Vector4) -> None:
        ...
    @property
    def outline_width_texels(self) -> float:
        """
        Width of the rendered outline, in texels
        """
    @outline_width_texels.setter
    def outline_width_texels(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def particle_count(self) -> int:
        """
        Number of particles currently in this fluid
        """
    @property
    def particle_mass(self) -> float:
        """
        Mass of each individual particle. Values <= 0 are clamped to 0.01. Applies to all current particles.
        """
    @particle_mass.setter
    def particle_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def particle_radius(self) -> float:
        """
        Visual radius of each rendered fluid particle. Clamped to a small positive minimum.
        """
    @particle_radius.setter
    def particle_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def particles(self) -> list[FluidParticle]:
        """
        All FluidParticle instances currently owned by this component
        """
    @property
    def rest_density(self) -> float:
        """
        Target density the fluid solver tries to maintain per particle. Values <= 0 are clamped to 0.01. Higher values make the fluid behave more incompressibly dense.
        """
    @rest_density.setter
    def rest_density(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def smoothing_radius(self) -> float:
        """
        SPH smoothing (kernel) radius used for density/pressure calculations. Larger values sample a wider neighborhood per particle.
        """
    @smoothing_radius.setter
    def smoothing_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def viscosity(self) -> float:
        """
        How resistant the fluid is to flowing/shearing. Values <= 0 are clamped to 0.01. Higher values make the fluid feel thicker, like honey.
        """
    @viscosity.setter
    def viscosity(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def vorticity_strength(self) -> float:
        """
        Strength of vorticity confinement, which restores small-scale swirling motion that PBF-style solvers tend to damp out. Clamped to >= 0.
        """
    @vorticity_strength.setter
    def vorticity_strength(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class FluidParticle:
    """
    A single SPH particle owned by a FluidComponent.
    """
    def __repr__(self) -> str:
        ...
    def set_collision_radius(self, collision_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set collision_radius. See the collision_radius property.
        """
    def set_epsilon(self, epsilon: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set epsilon. See the epsilon property.
        """
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set inverse_mass. See the inverse_mass property.
        """
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set mass. See the mass property.
        """
    def set_position(self, position: Vector3) -> None:
        """
        Set position. See the position property.
        """
    def set_rest_density(self, rest_density: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set rest_density. See the rest_density property.
        """
    def set_smoothing_radius(self, smoothing_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set smoothing_radius. See the smoothing_radius property.
        """
    def set_velocity(self, velocity: Vector3) -> None:
        """
        Set velocity. See the velocity property.
        """
    def set_viscosity(self, viscosity: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set viscosity. See the viscosity property.
        """
    def set_vorticity_strength(self, vorticity_strength: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set vorticity_strength. See the vorticity_strength property.
        """
    @property
    def collision_radius(self) -> float:
        """
        Physical collision radius of this individual particle
        """
    @collision_radius.setter
    def collision_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def density(self) -> float:
        """
        Density computed by the solver this substep (read-only)
        """
    @property
    def epsilon(self) -> float:
        """
        Relaxation parameter (CFM) for this individual particle, overriding FluidComponent.epsilon
        """
    @epsilon.setter
    def epsilon(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_mass(self) -> float:
        """
        1/mass of this individual particle
        """
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def lambda_(self) -> float:
        """
        Constraint multiplier from the solver's last substep (read-only)
        """
        ...
    exec('lambda = lambda_')
    @property
    def mass(self) -> float:
        """
        Mass of this individual particle. Values <= 0 are clamped to 0.001.
        """
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object whose FluidComponent owns this particle
        """
    @property
    def position(self) -> Vector3:
        """
        World-space position of this particle. Setting this also resets predicted_position, teleporting the particle immediately.
        """
    @position.setter
    def position(self, arg1: Vector3) -> None:
        ...
    @property
    def predicted_position(self) -> Vector3:
        """
        Position predicted by the solver this substep (read-only)
        """
    @property
    def rest_density(self) -> float:
        """
        Target density for this individual particle, overriding FluidComponent.rest_density
        """
    @rest_density.setter
    def rest_density(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def smoothing_radius(self) -> float:
        """
        SPH smoothing radius for this individual particle, overriding FluidComponent.smoothing_radius
        """
    @smoothing_radius.setter
    def smoothing_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def velocity(self) -> Vector3:
        """
        Linear velocity of this particle
        """
    @velocity.setter
    def velocity(self, arg1: Vector3) -> None:
        ...
    @property
    def viscosity(self) -> float:
        """
        Viscosity for this individual particle, overriding FluidComponent.viscosity
        """
    @viscosity.setter
    def viscosity(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def vorticity_strength(self) -> float:
        """
        Vorticity confinement strength for this individual particle, overriding FluidComponent.vorticity_strength
        """
    @vorticity_strength.setter
    def vorticity_strength(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class FractureComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def fracture(self) -> None:
        """
        Immediately fracture this object into shards at its own center.
        
        Example:
            ```python
            self.get_component(FractureComponent).fracture()
            ```
        """
    def fracture_at_local_point(self, local_point: Vector3) -> None:
        """
        Immediately fracture this object into shards, using localPoint (in this object's local/model space) as the impact point that seeds the fracture pattern.
        
        Example:
            ```python
            fc.fracture_at_local_point(Vector3(0.5, 0, 0))
            ```
        """
    def fracture_at_world_point(self, world_point: Vector3) -> None:
        """
        Immediately fracture this object into shards, using worldPoint (world-space) as the impact point that seeds the fracture pattern.
        
        Example:
            ```python
            fc.fracture_at_world_point(hit.point)
            ```
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_fracturable(self, fracturable: bool) -> None:
        """
        Set fracturable. See the fracturable property.
        """
    def set_impulse_threshold(self, impulse_threshold: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set impulse_threshold. See the impulse_threshold property.
        """
    def set_max_fracture_generations(self, max_fracture_generations: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set max_fracture_generations. See the max_fracture_generations property.
        """
    def set_min_fragment_area(self, min_fragment_area: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set min_fragment_area. See the min_fragment_area property.
        """
    def set_rest_density(self, rest_density: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set rest_density. See the rest_density property.
        """
    def set_shard_count(self, shard_count: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Set shard_count. See the shard_count property.
        """
    @property
    def fracturable(self) -> bool:
        """
        Whether this object can fracture at all, either from impacts or via fracture()/fracture_at_world_point()
        """
    @fracturable.setter
    def fracturable(self, arg1: bool) -> None:
        ...
    @property
    def generation(self) -> int:
        """
        How many times this object (or its source ancestor) has already fractured
        """
    @property
    def impulse_threshold(self) -> float:
        """
        Minimum collision impulse required to trigger an automatic fracture
        """
    @impulse_threshold.setter
    def impulse_threshold(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def max_fracture_generations(self) -> int:
        """
        Maximum number of times a shard produced by this object (or its descendants) may itself fracture again. See the generation property.
        """
    @max_fracture_generations.setter
    def max_fracture_generations(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def min_fragment_area(self) -> float:
        """
        Fragments smaller than this area (in world units squared) are discarded rather than spawned as shards
        """
    @min_fragment_area.setter
    def min_fragment_area(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def rest_density(self) -> float:
        """
        Density used to compute mass for newly-created shards, based on their fragment area
        """
    @rest_density.setter
    def rest_density(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def shard_count(self) -> int:
        """
        Target number of shards produced by a fracture
        """
    @shard_count.setter
    def shard_count(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class Input:
    @staticmethod
    def is_key_just_pressed(key: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        True only on the frame the key was pressed
        """
    @staticmethod
    def is_key_pressed(key: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        True every frame the key is held down
        """
    @staticmethod
    def is_key_released(key: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        True only on the frame the key was released
        """
    @staticmethod
    def is_mouse_button_just_pressed(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        True only on the frame the mouse button was pressed
        """
    @staticmethod
    def is_mouse_button_pressed(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        True every frame the mouse button is held down
        """
    @staticmethod
    def is_mouse_button_released(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
        """
        True only on the frame the mouse button was released
        """
    @staticmethod
    def on_key_just_pressed(key: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires once on the frame the key is pressed. Returns an id usable with remove_key_just_pressed_callback().
        """
    @staticmethod
    def on_key_pressed(key: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires every frame while the key is held. Returns an id usable with remove_key_pressed_callback().
        """
    @staticmethod
    def on_key_released(key: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires once on the frame the key is released. Returns an id usable with remove_key_released_callback().
        """
    @staticmethod
    def on_mouse_button_just_pressed(button: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires once on the frame the mouse button is pressed. Returns an id usable with remove_mouse_button_just_pressed_callback().
        """
    @staticmethod
    def on_mouse_button_pressed(button: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires every frame while the mouse button is held. Returns an id usable with remove_mouse_button_pressed_callback().
        """
    @staticmethod
    def on_mouse_button_released(button: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires once on the frame the mouse button is released. Returns an id usable with remove_mouse_button_released_callback().
        """
    @staticmethod
    def remove_key_just_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        """
        Unregister a callback previously registered with on_key_just_pressed()
        """
    @staticmethod
    def remove_key_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        """
        Unregister a callback previously registered with on_key_pressed()
        """
    @staticmethod
    def remove_key_released_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        """
        Unregister a callback previously registered with on_key_released()
        """
    @staticmethod
    def remove_mouse_button_just_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        """
        Unregister a callback previously registered with on_mouse_button_just_pressed()
        """
    @staticmethod
    def remove_mouse_button_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        """
        Unregister a callback previously registered with on_mouse_button_pressed()
        """
    @staticmethod
    def remove_mouse_button_released_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        """
        Unregister a callback previously registered with on_mouse_button_released()
        """
class Object:
    def __init__(self) -> None:
        """
        Creates a new Object, not yet part of the scene — call add_object() to insert it.
        """
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this Object
        """
    def add_component(self, component: typing.Any) -> typing.Any:
        """
        Attach a component instance to this Object.
        
        Example:
            ```python
            obj.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_children(self) -> list[Object]:
        """
        Get children. See the children property.
        """
    def get_children_count(self) -> int:
        """
        Number of direct children this Object has
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_parent(self) -> Object:
        """
        Get parent. See the parent property.
        """
    def get_parent_id(self) -> int:
        """
        Get parent_id. See the parent_id property.
        """
    def has_component(self, component: typing.Any) -> bool:
        """
        Check if this Object has a component of the given type.
        
        Example:
            ```python
            obj.has_component(RenderComponent)
            ```
        """
    def hide(self) -> None:
        """
        Hide this Object
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this Object.
        
        Example:
            ```python
            obj.remove_component(RenderComponent)
            ```
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_name(self, name: str) -> None:
        """
        Set name. See the name property.
        """
    def show(self) -> None:
        """
        Unhide this Object
        """
    @property
    def children(self) -> list[Object]:
        """
        This Object's direct children
        """
    @property
    def hidden(self) -> bool:
        """
        Whether this Object is hidden. Prefer show()/hide() over setting this directly.
        """
    @hidden.setter
    def hidden(self, arg0: bool) -> None:
        ...
    @property
    def id(self) -> int:
        """
        Unique id of this Object
        """
    @property
    def name(self) -> str:
        """
        Display name of this Object
        """
    @name.setter
    def name(self, arg0: str) -> None:
        ...
    @property
    def parent(self) -> Object:
        """
        This Object's parent, or None if it has none
        """
    @property
    def parent_id(self) -> int:
        """
        Id of this Object's parent, or an invalid id if it has none
        """
class PointMass:
    """
    A single mass point within a SoftBodyComponent's mass-spring aggregate.
    """
    def __repr__(self) -> str:
        ...
    def get_world_position(self) -> Vector3:
        """
        Get world_pos. See the world_pos property.
        """
    def set_base_acceleration(self, base_acceleration: Vector3) -> None:
        """
        Set base_acceleration. See the base_acceleration property.
        """
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set inverse_mass. See the inverse_mass property.
        """
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set mass. See the mass property.
        """
    def set_point_radius(self, point_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set point_radius. See the point_radius property.
        """
    def set_velocity(self, velocity: Vector3) -> None:
        """
        Set velocity. See the velocity property.
        """
    def update_world_position(self, position: Vector3) -> None:
        """
        Move this point mass to a new world position immediately (bypasses springs)
        """
    @property
    def acceleration(self) -> Vector3:
        """
        Total acceleration this frame (gravity/base + accumulated forces)
        """
    @property
    def base_acceleration(self) -> Vector3:
        """
        Persistent acceleration such as gravity.
        
        Example:
            ```python
            Vector3(0, -9.8, 0)
            ```
        """
    @base_acceleration.setter
    def base_acceleration(self, arg1: Vector3) -> None:
        ...
    @property
    def index(self) -> int:
        """
        Index of this point mass within its SoftBodyComponent.mass_aggregate
        """
    @property
    def inverse_mass(self) -> float:
        """
        1/mass of this individual point mass. Set to 0 to pin it in place.
        """
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def is_center(self) -> bool:
        """
        Whether this is the soft body's center point mass
        """
    @property
    def local_pos(self) -> Vector3:
        """
        Rest position in the parent object's local/model space
        """
    @property
    def mass(self) -> float:
        """
        Mass of this individual point mass. Values <= 0 are ignored.
        """
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def point_radius(self) -> float:
        """
        Collision radius of this individual point mass
        """
    @point_radius.setter
    def point_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def soft_body(self) -> SoftBodyComponent:
        """
        The SoftBodyComponent this point mass belongs to
        """
    @property
    def velocity(self) -> Vector3:
        """
        Linear velocity of this individual point mass
        """
    @velocity.setter
    def velocity(self, arg1: Vector3) -> None:
        ...
    @property
    def world_pos(self) -> Vector3:
        """
        Current world-space position of this point mass. Setting this teleports it immediately, bypassing springs — same as update_world_position().
        """
    @world_pos.setter
    def world_pos(self, arg1: Vector3) -> None:
        ...
class PolygonShape:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, points: collections.abc.Sequence[Vector3]) -> None:
        """
        Build a polygon from a list of Vector3 points in local coordinates.
        
        Example:
            ```python
            PolygonShape([Vector3(0,0,0), Vector3(1,0,0), Vector3(0,1,0)])
            ```
        """
    @property
    def vertices(self) -> list[float]:
        """
        Flattened vertex buffer: 5 floats per vertex (x, y, z, u, v), in the order the points were given to the constructor. Read/write, but prefer constructing a new PolygonShape over editing this in place.
        """
    @vertices.setter
    def vertices(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
class PrismaticConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object = None, dir: Vector3 = ...) -> None:
        """
        Create a prismatic (slider) constraint at object_a's and object_b's centers by default, constraining relative motion to the line between them.
        
        Example:
            ```python
            pc = PrismaticConstraint(self.owner, target)
            cc.add_constraint(pc)
            ```
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, dir: Vector3 = ...) -> None:
        """
        Create a prismatic constraint at explicit local-space attach points on each object.
        """
    def relock_direction(self) -> None:
        """
        Recompute the locked slide direction from the objects' current world positions (mirrors the inspector's 'Re-lock direction' button)
        """
    @property
    def dir(self) -> Vector3:
        """
        The locked slide direction. Read-only from script — use relock_direction() to update it.
        """
class RayCastHit:
    """
    Result of a Physics.raycast() query. Falsy (bool(hit) is False) when nothing was hit.
    """
    def __bool__(self) -> bool:
        """
        Allows 'if hit:' instead of 'if hit.hit:'
        """
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def distance(self) -> float:
        """
        Distance from the ray's origin to the hit point
        """
    @property
    def edge_index(self) -> int:
        """
        Index of the shape edge that was hit
        """
    @property
    def hit(self) -> bool:
        """
        Whether the ray hit anything
        """
    @property
    def is_soft_body(self) -> bool:
        """
        Whether the hit object was a soft body
        """
    @property
    def normal(self) -> Vector3:
        """
        World-space surface normal at the hit point
        """
    @property
    def object(self) -> Object:
        """
        The Object that was hit, or None if hit is False
        """
    @property
    def point(self) -> Vector3:
        """
        World-space point where the ray hit
        """
class RectangleShape:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, center: Vector3, width: typing.SupportsFloat | typing.SupportsIndex, height: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def center(self) -> Vector3:
        """
        Local-space center of the rectangle
        """
    @center.setter
    def center(self, arg0: Vector3) -> None:
        ...
    @property
    def height(self) -> float:
        """
        Height of the rectangle in local units
        """
    @height.setter
    def height(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def width(self) -> float:
        """
        Width of the rectangle in local units
        """
    @width.setter
    def width(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class RenderComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_enable(self, arg0: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_shape(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape) -> None:
        """
        Accepts a RectangleShape, CircleShape, or PolygonShape
        """
    def set_texture(self, virtual_path: str) -> None:
        """
        Load a texture from a res:// path (e.g. 'res://textures/wood.png'), or pass '' to clear it
        """
    @property
    def color(self) -> Vector4:
        """
        Tint/fill color (RGBA, 0-1) applied to the shape and any texture
        """
    @color.setter
    def color(self, arg1: Vector4) -> None:
        ...
    @property
    def enable(self) -> bool:
        """
        Whether this component is active. Disabling hides the object's rendered shape.
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def shape(self) -> fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape:
        """
        The shape used to render this object. Accepts a RectangleShape, CircleShape, or PolygonShape. Equivalent to calling set_shape().
        """
    @shape.setter
    def shape(self, arg1: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape) -> None:
        ...
    @property
    def z_index(self) -> int:
        """
        Draw order relative to other render components. Higher values draw on top.
        """
    @z_index.setter
    def z_index(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class RevoluteConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object = None) -> None:
        """
        Create a revolute (hinge) constraint pinned at object_a's and object_b's centers by default.
        
        Example:
            ```python
            rc = RevoluteConstraint(self.owner, target)
            cc.add_constraint(rc)
            ```
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3) -> None:
        """
        Create a revolute constraint pinned at explicit local-space attach points on each object.
        """
class RigidBodyComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_force(self, force: Vector3) -> None:
        """
        Apply a force through the center of mass
        """
    def add_force_at_local_point(self, force: Vector3, point: Vector3) -> None:
        """
        Apply a force at a point given in this object's local/model coordinates
        """
    def add_force_at_world_point(self, force: Vector3, point: Vector3) -> None:
        """
        Apply a force at a point given in world coordinates
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def recalculate_inertia(self) -> None:
        """
        Recompute inertia from the current shape and mass, e.g. after resizing
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_acceleration(self, acceleration: Vector2) -> None:
        """
        Set acceleration. See the acceleration property.
        """
    def set_angular_acceleration(self, angular_acceleration: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set angular_acceleration. See the angular_acceleration property.
        """
    def set_angular_damping(self, angular_damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set angular_damping. See the angular_damping property.
        """
    def set_angular_velocity(self, angular_velocity: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set angular_velocity. See the angular_velocity property.
        """
    def set_enable(self, arg0: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_inertia(self, inertia: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set inertia. See the inertia property.
        """
    def set_inverse_inertia(self, inverse_inertia: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set inverse_inertia. See the inverse_inertia property.
        """
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set inverse_mass. See the inverse_mass property.
        """
    def set_linear_damping(self, linear_damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set linear_damping. See the linear_damping property.
        """
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set mass. See the mass property.
        """
    def set_net_force(self, net_force: Vector2) -> None:
        """
        Set net_force. See the net_force property.
        """
    def set_torque(self, torque: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set torque. See the torque property.
        """
    def set_velocity(self, velocity: Vector3) -> None:
        """
        Set velocity. See the velocity property.
        """
    @property
    def acceleration(self) -> Vector2:
        """
        Net acceleration applied every physics step, in addition to any per-frame add_force() calls
        """
    @acceleration.setter
    def acceleration(self, arg1: Vector2) -> None:
        ...
    @property
    def angular_acceleration(self) -> float:
        """
        Angular acceleration in radians per second squared, applied every physics step
        """
    @angular_acceleration.setter
    def angular_acceleration(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def angular_damping(self) -> float:
        """
        Fraction of angular velocity lost per second (0 = none, 1 = stops immediately)
        """
    @angular_damping.setter
    def angular_damping(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def angular_velocity(self) -> float:
        """
        Angular velocity in radians per second
        """
    @angular_velocity.setter
    def angular_velocity(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def inertia(self) -> float:
        """
        Rotational inertia. Setting this directly overrides whatever recalculate_inertia()/mass changes would otherwise compute.
        """
    @inertia.setter
    def inertia(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_inertia(self) -> float:
        """
        1/inertia. Set this to 0 to prevent rotation entirely.
        """
    @inverse_inertia.setter
    def inverse_inertia(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_mass(self) -> float:
        """
        1/mass. Set this to 0 to make the body immovable/infinite mass. Setting this also recalculates inertia from the current shape.
        """
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def linear_damping(self) -> float:
        """
        Fraction of linear velocity lost per second (0 = none, 1 = stops immediately)
        """
    @linear_damping.setter
    def linear_damping(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def mass(self) -> float:
        """
        Mass of the body. Values <= 0 are clamped to 0.001. Setting this also recalculates inertia from the current shape.
        """
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def net_force(self) -> Vector2:
        """
        Read-back of the total force accumulated this step, for inspection/debugging. Use add_force() to actually apply forces.
        """
    @net_force.setter
    def net_force(self, arg1: Vector2) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def torque(self) -> float:
        """
        Read-back of the total torque accumulated this step, for inspection/debugging
        """
    @torque.setter
    def torque(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def velocity(self) -> Vector3:
        """
        Linear velocity in world units per second
        """
    @velocity.setter
    def velocity(self, arg1: Vector3) -> None:
        ...
class Script:
    def __init__(self) -> None:
        ...
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
class SoftBodyComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_force(self, force: Vector3) -> None:
        """
        Apply a uniform force across every point mass in the soft body
        """
    def add_force_at_center(self, force: Vector3) -> None:
        """
        Apply a force to the center point mass only
        """
    def add_force_at_local_point(self, force: Vector3, point: Vector3) -> None:
        """
        Apply a force distributed across the point masses nearest the given local/model-space point
        """
    def add_force_at_world_point(self, force: Vector3, point: Vector3) -> None:
        """
        Apply a force distributed across the point masses nearest the given world-space point
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def add_point_mass(self, local_point: Vector3) -> None:
        """
        Add a new point mass at the given local/model position
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def get_point_mass(self, index: typing.SupportsInt | typing.SupportsIndex) -> PointMass:
        """
        Get a point mass by index. Index (size - 1) is always the center point mass.
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_damping(self, damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set damping. See the damping property.
        """
    def set_enable(self, arg0: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_gas_amount(self, gas_amount: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set gas_amount. See the gas_amount property.
        """
    def set_gas_pressure_enabled(self, enabled: bool) -> None:
        """
        Enable gas pressue mode
        """
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set inverse_mass. See the inverse_mass property.
        """
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set mass. See the mass property.
        """
    def set_stiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set stiffness. See the stiffness property.
        """
    def set_velocity(self, velocity: Vector3) -> None:
        """
        Set velocity. See the velocity property.
        """
    @property
    def acceleration(self) -> Vector3:
        """
        Current acceleration of the center point mass (gravity + accumulated forces)
        """
    @property
    def center_point_mass(self) -> PointMass:
        """
        The center point mass of this soft body
        """
    @property
    def damping(self) -> float:
        """
        Damping applied to internal springs, reducing jiggle/oscillation
        """
    @damping.setter
    def damping(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def gas_amount(self) -> float:
        """
        Amount of internal gas pressure applied when gas_pressure_enabled is True. Higher values push outward more strongly.
        """
    @gas_amount.setter
    def gas_amount(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def gas_pressure_enabled(self) -> bool:
        """
        Enable gas pressure mode, which pushes the body's outline outward to maintain internal volume (balloon-like)
        """
    @gas_pressure_enabled.setter
    def gas_pressure_enabled(self, arg1: bool) -> None:
        ...
    @property
    def inverse_mass(self) -> float:
        """
        1/mass for the whole soft body. Setting this redistributes evenly across every point mass, same as the mass property.
        """
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def mass(self) -> float:
        """
        Total mass of the soft body. Values <= 0 are ignored. Setting this redistributes mass evenly across every point mass.
        """
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def mass_aggregate(self) -> list[PointMass]:
        """
        All point masses in this soft body, in order (the last one is always the center)
        """
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def point_mass_count(self) -> int:
        """
        Number of point masses making up this soft body, including the center point mass
        """
    @property
    def stiffness(self) -> float:
        """
        How strongly internal springs resist deformation. Higher values make the body feel more rigid.
        """
    @stiffness.setter
    def stiffness(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def velocity(self) -> Vector3:
        """
        Bulk velocity applied to the soft body's center point mass
        """
    @velocity.setter
    def velocity(self, arg1: Vector3) -> None:
        ...
class SpringConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, length: typing.SupportsFloat | typing.SupportsIndex, object_b: Object = None, stiffness: typing.SupportsFloat | typing.SupportsIndex = 15.0, damping: typing.SupportsFloat | typing.SupportsIndex = 7.0) -> None:
        """
        Create a spring constraint attached at object_a's and object_b's centers by default.
        
        Example:
            ```python
            sc = SpringConstraint(self.owner, target, 5.0)
            cc.add_constraint(sc)
            ```
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, length: typing.SupportsFloat | typing.SupportsIndex, stiffness: typing.SupportsFloat | typing.SupportsIndex = 15.0, damping: typing.SupportsFloat | typing.SupportsIndex = 7.0) -> None:
        """
        Create a spring constraint at explicit local-space attach points on each object.
        """
    def set_damping(self, damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set damping. See the damping property.
        """
    def set_length(self, length: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set length. See the length property.
        """
    def set_stiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set stiffness. See the stiffness property.
        """
    @property
    def damping(self) -> float:
        """
        Damping coefficient. Higher values reduce oscillation around the rest length.
        """
    @damping.setter
    def damping(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def length(self) -> float:
        """
        Rest length of the spring
        """
    @length.setter
    def length(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def stiffness(self) -> float:
        """
        Spring constant. Higher values pull back to the rest length more strongly.
        """
    @stiffness.setter
    def stiffness(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class TransformComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object.
        
        Example:
            ```python
            render = self.add_component(RenderComponent)
            ```
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        """
        The Object that owns this component
        """
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_enable(self, arg0: bool) -> None:
        """
        Set enable. See the enable property.
        """
    def set_rotation(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set rotation (radians). See the rotation property.
        """
    def set_rotation_degrees(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set rotation_degrees. See the rotation_degrees property.
        """
    def set_size(self, arg0: Vector3) -> None:
        """
        Set size. See the size property.
        """
    def to_local_coordinates(self, arg0: Vector3) -> None:
        """
        Convert a world-space point into this object's local/model space
        """
    def to_world_coordinates(self, arg0: Vector3) -> None:
        """
        Convert a local/model-space point into world space
        """
    def update_world_position(self, arg0: Vector3) -> None:
        """
        Set world_position. See the world_position property.
        """
    @property
    def enable(self) -> bool:
        """
        Whether this component is active
        """
    @enable.setter
    def enable(self, arg1: bool) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def rotation(self) -> float:
        """
        Rotation in radians
        """
    @rotation.setter
    def rotation(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def rotation_degrees(self) -> float:
        """
        Rotation in degrees. Equivalent to the rotation property converted to/from radians.
        """
    @rotation_degrees.setter
    def rotation_degrees(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def size(self) -> Vector3:
        """
        Scale of the object along each axis
        """
    @size.setter
    def size(self, arg1: Vector3) -> None:
        ...
    @property
    def world_position(self) -> Vector3:
        """
        World-space position of the object
        """
    @world_position.setter
    def world_position(self, arg1: Vector3) -> None:
        ...
class Vector2:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def lerp(a: Vector2, b: Vector2, t: typing.SupportsFloat | typing.SupportsIndex) -> Vector2:
        """
        Linearly interpolate between a and b (t=0 -> a, t=1 -> b), e.g. Vector2.lerp(start, end, 0.5)
        """
    def __add__(self, arg0: Vector2) -> Vector2:
        ...
    def __eq__(self, arg0: Vector2) -> bool:
        ...
    def __getitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> float:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @typing.overload
    def __init__(self, scalar: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def __len__(self) -> int:
        ...
    @typing.overload
    def __mul__(self, arg0: Vector2) -> Vector2:
        ...
    @typing.overload
    def __mul__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector2:
        ...
    def __ne__(self, arg0: Vector2) -> bool:
        ...
    def __neg__(self) -> Vector2:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector2:
        ...
    def __setitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def __sub__(self, arg0: Vector2) -> Vector2:
        ...
    def __truediv__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector2:
        ...
    def dot(self, arg0: Vector2) -> float:
        ...
    def length(self) -> float:
        ...
    def normalize(self) -> Vector2:
        ...
    @property
    def x(self) -> float:
        ...
    @x.setter
    def x(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def y(self) -> float:
        ...
    @y.setter
    def y(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class Vector3:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def lerp(a: Vector3, b: Vector3, t: typing.SupportsFloat | typing.SupportsIndex) -> Vector3:
        """
        Linearly interpolate between a and b (t=0 -> a, t=1 -> b), e.g. Vector3.lerp(start, end, 0.5)
        """
    def __add__(self, arg0: Vector3) -> Vector3:
        ...
    def __eq__(self, arg0: Vector3) -> bool:
        ...
    def __getitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> float:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, z: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @typing.overload
    def __init__(self, scalar: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def __len__(self) -> int:
        ...
    @typing.overload
    def __mul__(self, arg0: Vector3) -> Vector3:
        ...
    @typing.overload
    def __mul__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector3:
        ...
    def __ne__(self, arg0: Vector3) -> bool:
        ...
    def __neg__(self) -> Vector3:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector3:
        ...
    def __setitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def __sub__(self, arg0: Vector3) -> Vector3:
        ...
    def __truediv__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector3:
        ...
    def cross(self, arg0: Vector3) -> Vector3:
        ...
    def dot(self, arg0: Vector3) -> float:
        ...
    def length(self) -> float:
        ...
    def normalized(self) -> Vector3:
        ...
    @property
    def x(self) -> float:
        ...
    @x.setter
    def x(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def y(self) -> float:
        ...
    @y.setter
    def y(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def z(self) -> float:
        ...
    @z.setter
    def z(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class Vector4:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def lerp(a: Vector4, b: Vector4, t: typing.SupportsFloat | typing.SupportsIndex) -> Vector4:
        """
        Linearly interpolate between a and b (t=0 -> a, t=1 -> b), e.g. Vector4.lerp(start, end, 0.5)
        """
    def __add__(self, arg0: Vector4) -> Vector4:
        ...
    def __eq__(self, arg0: Vector4) -> bool:
        ...
    def __getitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> float:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, x: typing.SupportsFloat | typing.SupportsIndex, y: typing.SupportsFloat | typing.SupportsIndex, z: typing.SupportsFloat | typing.SupportsIndex, w: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @typing.overload
    def __init__(self, scalar: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def __len__(self) -> int:
        ...
    @typing.overload
    def __mul__(self, arg0: Vector4) -> Vector4:
        ...
    @typing.overload
    def __mul__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector4:
        ...
    def __ne__(self, arg0: Vector4) -> bool:
        ...
    def __neg__(self) -> Vector4:
        ...
    def __repr__(self) -> str:
        ...
    def __rmul__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector4:
        ...
    def __setitem__(self, arg0: typing.SupportsInt | typing.SupportsIndex, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def __sub__(self, arg0: Vector4) -> Vector4:
        ...
    def __truediv__(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> Vector4:
        ...
    def dot(self, arg0: Vector4) -> float:
        ...
    def length(self) -> float:
        ...
    def normalized(self) -> Vector4:
        ...
    @property
    def a(self) -> float:
        ...
    @a.setter
    def a(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def b(self) -> float:
        ...
    @b.setter
    def b(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def g(self) -> float:
        ...
    @g.setter
    def g(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def r(self) -> float:
        ...
    @r.setter
    def r(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def w(self) -> float:
        ...
    @w.setter
    def w(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def x(self) -> float:
        ...
    @x.setter
    def x(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def y(self) -> float:
        ...
    @y.setter
    def y(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def z(self) -> float:
        ...
    @z.setter
    def z(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class WeldConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object = None, angular_offset: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
        """
        Create a weld constraint at object_a's and object_b's centers by default, locking their relative position and rotation.
        
        Example:
            ```python
            wc = WeldConstraint(self.owner, target)
            cc.add_constraint(wc)
            ```
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, angular_offset: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
        """
        Create a weld constraint at explicit local-space attach points on each object.
        """
    def set_angular_offset(self, angular_offset: typing.SupportsFloat | typing.SupportsIndex) -> None:
        """
        Set angular_offset. See the angular_offset property.
        """
    @property
    def angular_offset(self) -> float:
        """
        Fixed rotational offset (radians) maintained between Object A and Object B
        """
    @angular_offset.setter
    def angular_offset(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class _ExportMarker:
    pass
def _pack_get_source(arg0: str) -> typing.Any:
    ...
def _pack_has_module(arg0: str) -> bool:
    ...
def _pack_is_package(arg0: str) -> bool:
    ...
def add_scene(path: str, parent: Object = None) -> Object:
    """
    Load a scene from a res:// path and add it as a child of parent (or as a root-level object if parent is None). Returns the newly created root Object of the loaded scene.
    
    Example:
        ```python
        enemy = add_scene('res://enemy.fscene', self.owner)
        enemy.get_component(TransformComponent).world_position = spawn_point
        ```
    """
def export(value: typing.Any) -> _ExportMarker:
    """
    Mark a script attribute as editable in the inspector using the default widget for its type.
    
    Example:
        ```python
        name = export("Goblin")
        hp = export(100)
        ```
    For customizable export, use the appropriate export function: export_range, export_color_picker
    """
def export_angle_slider(value: typing.Any, min_degrees: typing.SupportsFloat | typing.SupportsIndex = -360.0, max_degrees: typing.SupportsFloat | typing.SupportsIndex = 360.0) -> _ExportMarker:
    """
    Mark a float script attribute (stored in radians) as editable with an angle slider displayed in degrees.
    
    Example:
        ```python
        facing = export_angle_slider(0.0)
        cone_angle = export_angle_slider(0.5, 0.0, 180.0)
        ```
    """
def export_color_edit(value: typing.Any) -> _ExportMarker:
    """
    Mark a Vector3 or Vector4 script attribute as editable with a color swatch that opens a picker popup.
    
    Example:
        ```python
        tint = export_color_edit(Vector4(1, 1, 1, 1))
        ```
    """
def export_color_picker(value: typing.Any) -> _ExportMarker:
    """
    Mark a Vector3 or Vector4 script attribute as editable with a full color picker always shown inline.
    
    Example:
        ```python
        glow_color = export_color_picker(Vector3(0.2, 0.8, 1.0))
        ```
    """
def export_drag(value: typing.Any, min: typing.SupportsFloat | typing.SupportsIndex = 0.0, max: typing.SupportsFloat | typing.SupportsIndex = 0.0, prefix: str = '', suffix: str = '') -> _ExportMarker:
    """
    Mark a script attribute as editable with a click-and-drag field. min=max=0 (the default) means unbounded.
    
    Example:
        ```python
        jump_force = export_drag(15.0)
        ammo = export_drag(30, 0, 999)
        ```
    """
def export_file(value: typing.Any, extension: str = '*.*') -> _ExportMarker:
    """
    Mark a str script attribute as editable with a file picker that stores a res:// virtual path. Clicking opens a file dialog; files can also be dragged in from the resource browser. extension filters which files are shown/accepted, using ';'-separated glob patterns.
    
    Example:
        ```python
        icon = export_file("", "*.png;*.jpg;*.jpeg")
        ```
    """
def export_range(value: typing.Any, min: typing.SupportsFloat | typing.SupportsIndex = ..., max: typing.SupportsFloat | typing.SupportsIndex = ..., slider: bool = False, prefix: str = '', suffix: str = '') -> _ExportMarker:
    """
    Mark a script attribute as editable within a min/max range. Shown as a bounded slider by default; pass slider=False for a plain input field that still applies min/max (and any prefix/suffix).
    
    Example:
        ```python
        speed = export_range(200.0, 0.0, 500.0)
        hp = export_range(100, 0, 999, slider=False, suffix=" hp")
        ```
    """
def export_scene(value: typing.Any) -> _ExportMarker:
    """
    Mark a str script attribute as editable with a file picker restricted to .fscene files, storing a res:// virtual path.
    
    Example:
        ```python
        next_level = export_scene("res://levels/level_2.fscene")
        ```
    """
def export_section(name: str) -> typing.Any:
    """
    Create a collapsible inspector section. All exported properties following this marker are displayed inside the section until another section marker is encountered. Can be used as a bare statement.
    
    Example:
        ```python
        export_section("Visuals")
        color = export_color_edit(Vector4(1, 1, 1, 1))
        ```
    """
def export_sub_section(name: str) -> typing.Any:
    """
    Create a collapsible inspector sub-section, nested inside whichever export_section is currently open (or at the top level if none is). Properties following this marker are displayed inside it until another section or sub-section marker is encountered. Can be used as a bare statement.
    
    Example:
        ```python
        export_section("Movement")
        speed = export(5.0)
        export_sub_section("Advanced")
        acceleration_curve = export(1.0)
        ```
    """
def find_objects_with_component(component_class: typing.Any) -> list[Object]:
    """
    Every Object in the scene that has the given component type.
    
    Example:
        ```python
        enemies = find_objects_with_component(Enemy)
        ```
    """
def get_all_objects() -> list[Object]:
    """
    Every Object currently in the scene. Useful for linear searches instead of maintaining your own registry.
    
    Example:
        ```python
        enemies = [o for o in get_all_objects() if o.has_component(Enemy)]
        ```
    """
def get_script(path: str) -> typing.Any:
    """
    Import and return the Script subclass at the given res:// path. Only needed for genuinely dynamic/data-driven loading — for normal use, just import the class directly, e.g. `from scripts.enemy import Enemy`.
    """
def layer_overlap(layer_a: typing.SupportsInt | typing.SupportsIndex, mask_a: typing.SupportsInt | typing.SupportsIndex, layer_b: typing.SupportsInt | typing.SupportsIndex, mask_b: typing.SupportsInt | typing.SupportsIndex) -> bool:
    """
    Check whether an (layer, mask) pair on object A would collide with (layer, mask) on object B
    """
def lerp(a: typing.SupportsFloat | typing.SupportsIndex, b: typing.SupportsFloat | typing.SupportsIndex, t: typing.SupportsFloat | typing.SupportsIndex) -> float:
    """
    Linearly interpolate between two floats (t=0 -> a, t=1 -> b)
    """
def load_scene(path: str) -> None:
    """
    Load a scene from a res:// path, replacing the current live scene.
    
    Example:
        ```python
        load_scene('res://levels/level_2.fscene')
        ```
    """
FluidVsRigid: CollisionType  # value = <CollisionType.FluidVsRigid: 5>
FluidVsSoft: CollisionType  # value = <CollisionType.FluidVsSoft: 6>
RigidVsRigid: CollisionType  # value = <CollisionType.RigidVsRigid: 0>
RigidVsSoft: CollisionType  # value = <CollisionType.RigidVsSoft: 3>
RigidVsStatic: CollisionType  # value = <CollisionType.RigidVsStatic: 1>
SoftVsSoft: CollisionType  # value = <CollisionType.SoftVsSoft: 4>
StaticVsStatic: CollisionType  # value = <CollisionType.StaticVsStatic: 2>
