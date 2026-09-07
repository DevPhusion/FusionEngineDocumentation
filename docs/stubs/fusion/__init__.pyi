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
    enable: bool
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    @typing.overload
    def add_observation(self, value: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @typing.overload
    def add_observation(self, values: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    def add_reward(self, delta: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def clear_observation(self) -> None:
        ...
    def end_episode(self) -> None:
        ...
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        ...
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
        Set this agent's action space to any gymnasium.spaces.Space instance (Discrete, Box, MultiDiscrete, MultiBinary), e.g.
          from gymnasium import spaces
          self.agent.set_action_space(spaces.MultiDiscrete([3, 2, 2]))
        Must be called (e.g. from OnStart) before training or inference.
        """
    def set_observation(self, values: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
    def set_observation_space(self, space: typing.Any) -> None:
        """
        Optional. Override the observation space with any gymnasium.spaces.Space. If not set, a Box inferred from the length of accumulated add_observation() values is used automatically (previous default behavior).
        """
    def set_reward(self, value: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def action(self) -> typing.Any:
        """
        The most recent action, in whatever type matches the configured action_space (int for Discrete, list for Box/MultiDiscrete/MultiBinary), e.g.
          move_idx, jump, shoot = self.agent.action  # MultiDiscrete([3, 2, 2])
        """
    @property
    def action_space(self) -> typing.Any:
        ...
    @property
    def agent_id(self) -> int:
        ...
    @property
    def observation_space(self) -> typing.Any:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
class CameraComponent:
    enable: bool
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
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
        ...
    def get_range(self) -> float:
        ...
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
        ...
    def set_is_main(self, is_main: bool) -> None:
        ...
    def set_range(self, range: typing.SupportsFloat | typing.SupportsIndex) -> None:
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
        ...
    @range.setter
    def range(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class CircleShape:
    center: Vector3
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, center: Vector3, radius: typing.SupportsFloat | typing.SupportsIndex, segments: typing.SupportsInt | typing.SupportsIndex = 30, physics_segments: typing.SupportsInt | typing.SupportsIndex = 30) -> None:
        ...
    @property
    def radius(self) -> float:
        ...
    @radius.setter
    def radius(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def segments(self) -> int:
        ...
    @segments.setter
    def segments(self, arg0: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CollisionComponent:
    enable: bool
    is_static: bool
    shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape
    sync_with_render_component: bool
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
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def add_shape(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape, name: str = '') -> int:
        """
        Add a new collision shape to this component. Returns its shape_id, e.g.
          sid = col.add_shape(CircleShape(Vector3(0,0,0), 1.0), 'Detector')
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        ...
    def get_resolution_shape_id(self) -> int:
        ...
    def get_shape(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape:
        ...
    def get_shape_area(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> float:
        ...
    def get_shape_center(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> Vector3:
        ...
    def get_shape_id(self, name: str) -> int:
        """
        Look up a shape's id by its name (as set in the inspector or via set_shape_name). Returns -1 if no shape has that name, e.g.
          detector_id = self.cc.get_shape_id('Aggro Radius')
        """
    def get_shape_ids(self) -> list[int]:
        """
        Returns the ids of every collision shape on this component
        """
    def get_shape_name(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> str:
        ...
    def get_sync_with_render_component(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    def has_component(self, component_class: typing.Any) -> bool:
        """
        Check whether this component's owning Object has a component of the given type
        """
    def is_grounded(self, probe_length: typing.SupportsFloat | typing.SupportsIndex = 0.15000000596046448) -> bool:
        """
        Cast a short ray straight down from the lowest point of this shape to check for ground
        """
    def remove_collision_callback(self, id: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def remove_collision_enter_callback(self, id: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def remove_collision_exit_callback(self, id: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this component's owning Object
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def remove_shape(self, shape_id: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_collision_layer(self, layer: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_collision_mask(self, mask: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_enable(self, arg0: bool) -> None:
        ...
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
        ...
    def set_shape_name(self, shape_id: typing.SupportsInt | typing.SupportsIndex, name: str) -> None:
        ...
    def set_static(self, is_static: bool) -> None:
        ...
    @typing.overload
    def set_sync_with_render_component(self, sync: bool) -> None:
        ...
    @typing.overload
    def set_sync_with_render_component(self, shape_id: typing.SupportsInt | typing.SupportsIndex, sync: bool) -> None:
        ...
    @property
    def collision_layer(self) -> int:
        ...
    @collision_layer.setter
    def collision_layer(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def collision_mask(self) -> int:
        ...
    @collision_mask.setter
    def collision_mask(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def resolution_shape_id(self) -> int:
        ...
    @resolution_shape_id.setter
    def resolution_shape_id(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class CollisionEventData:
    def __repr__(self) -> str:
        ...
    @property
    def normal(self) -> Vector3:
        ...
    @property
    def other(self) -> Object:
        ...
    @property
    def other_shape_id(self) -> int:
        ...
    @property
    def penetration(self) -> float:
        ...
    @property
    def point(self) -> Vector3:
        ...
    @property
    def self(self) -> Object:
        ...
    @property
    def shape_id(self) -> int:
        ...
    @property
    def type(self) -> CollisionType:
        ...
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
    @staticmethod
    def Print(value: typing.Any) -> None:
        ...
    @staticmethod
    def PrintError(value: typing.Any) -> None:
        ...
    @staticmethod
    def PrintWarning(value: typing.Any) -> None:
        ...
class Constraint:
    draw_constraint: bool
    use_center_a: bool
    use_center_b: bool
    def __repr__(self) -> str:
        ...
    def get_attach_world_a(self) -> Vector3:
        ...
    def get_attach_world_b(self) -> Vector3:
        ...
    def set_beta(self, beta: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_draw_constraint(self, draw_constraint: bool) -> None:
        ...
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
        ...
    @beta.setter
    def beta(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def object_a(self) -> Object:
        ...
    @property
    def object_b(self) -> Object:
        ...
class ConstraintComponent:
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
        """
    def add_constraint(self, constraint: Constraint) -> None:
        """
        Register a constraint (e.g. a DistanceConstraint) with this object and the physics engine, e.g.
          cc.add_constraint(DistanceConstraint(self.owner, target, 5.0))
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
        ...
    def get_owner(self) -> Object:
        ...
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
        ...
    @typing.overload
    def remove_constraint(self, index: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
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
    extendable: bool
    retractable: bool
    @typing.overload
    def __init__(self, object_a: Object, distance: typing.SupportsFloat | typing.SupportsIndex, object_b: Object = None, extendable: bool = False, retractable: bool = False) -> None:
        """
        Create a distance constraint attached at object_a's and object_b's centers by default. Not part of the scene until passed to ConstraintComponent.add_constraint(), e.g.
          dc = DistanceConstraint(self.owner, target, 5.0)
          cc = self.add_component(ConstraintComponent)
          cc.add_constraint(dc)
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, distance: typing.SupportsFloat | typing.SupportsIndex, extendable: bool = False, retractable: bool = False) -> None:
        """
        Create a distance constraint at explicit local-space attach points on each object (pass Vector3(0,0,0) for object_b's attach point if object_b is None), e.g.
          dc = DistanceConstraint(self.owner, target, Vector3(0.5, 0, 0), Vector3(0, 0, 0), 5.0)
          cc = self.add_component(ConstraintComponent)
          cc.add_constraint(dc)
        """
    def set_distance(self, distance: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_extendable(self, extendable: bool) -> None:
        ...
    def set_retractable(self, retractable: bool) -> None:
        ...
    @property
    def distance(self) -> float:
        ...
    @distance.setter
    def distance(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class FluidComponent:
    color: Vector4
    enable: bool
    outline_color: Vector4
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    @typing.overload
    def add_particle(self, world_position: Vector3) -> FluidParticle:
        """
        Add a single fluid particle at the given world position, e.g.
          p = fluid.add_particle(Vector3(0, 2, 0))
        """
    @typing.overload
    def add_particle(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape, particle_count: typing.SupportsInt | typing.SupportsIndex) -> list[FluidParticle]:
        """
        Seed roughly particle_count particles filling the given shapeand add them to the fluid, e.g.
          fluid.add_particle(CircleShape(Vector3(0, 3, 0), 1.5), 200)
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        ...
    def get_particle(self, index: typing.SupportsInt | typing.SupportsIndex) -> FluidParticle:
        ...
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
        ...
    def set_color(self, color: Vector4) -> None:
        ...
    def set_desired_particle_count(self, desired_particle_count: typing.SupportsInt | typing.SupportsIndex) -> None:
        """
        Changing this re-seeds the whole fluid on its source shape, discarding any particles added individually via add_particle()
        """
    def set_enable(self, arg0: bool) -> None:
        ...
    def set_epsilon(self, epsilon: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_metaball_edge_soft(self, metaball_edge_soft: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_metaball_threshold(self, metaball_threshold: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_outline_color(self, outline_color: Vector4) -> None:
        ...
    def set_outline_width_texels(self, outline_width_texels: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_particle_mass(self, particle_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_particle_radius(self, particle_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_rest_density(self, rest_density: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_smoothing_radius(self, smoothing_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_viscosity(self, viscosity: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_vorticity_strength(self, vorticity_strength: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def update_collision_layer_mask(self) -> None:
        """
        Sync every particle's collision_layer/collision_mask with this Object's CollisionComponent
        """
    @property
    def collision_radius(self) -> float:
        ...
    @collision_radius.setter
    def collision_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def desired_particle_count(self) -> int:
        ...
    @desired_particle_count.setter
    def desired_particle_count(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def epsilon(self) -> float:
        ...
    @epsilon.setter
    def epsilon(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def metaball_edge_soft(self) -> float:
        ...
    @metaball_edge_soft.setter
    def metaball_edge_soft(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def metaball_threshold(self) -> float:
        ...
    @metaball_threshold.setter
    def metaball_threshold(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def outline_width_texels(self) -> float:
        ...
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
        ...
    @property
    def particle_mass(self) -> float:
        ...
    @particle_mass.setter
    def particle_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def particle_radius(self) -> float:
        ...
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
        ...
    @rest_density.setter
    def rest_density(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def smoothing_radius(self) -> float:
        ...
    @smoothing_radius.setter
    def smoothing_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def viscosity(self) -> float:
        ...
    @viscosity.setter
    def viscosity(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def vorticity_strength(self) -> float:
        ...
    @vorticity_strength.setter
    def vorticity_strength(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class FluidParticle:
    position: Vector3
    velocity: Vector3
    def __repr__(self) -> str:
        ...
    def set_collision_radius(self, collision_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_epsilon(self, epsilon: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_position(self, position: Vector3) -> None:
        ...
    def set_rest_density(self, rest_density: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_smoothing_radius(self, smoothing_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_velocity(self, velocity: Vector3) -> None:
        ...
    def set_viscosity(self, viscosity: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_vorticity_strength(self, vorticity_strength: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def collision_radius(self) -> float:
        ...
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
        ...
    @epsilon.setter
    def epsilon(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_mass(self) -> float:
        ...
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
        ...
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def owner(self) -> Object:
        ...
    @property
    def predicted_position(self) -> Vector3:
        """
        Position predicted by the solver this substep (read-only)
        """
    @property
    def rest_density(self) -> float:
        ...
    @rest_density.setter
    def rest_density(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def smoothing_radius(self) -> float:
        ...
    @smoothing_radius.setter
    def smoothing_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def viscosity(self) -> float:
        ...
    @viscosity.setter
    def viscosity(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def vorticity_strength(self) -> float:
        ...
    @vorticity_strength.setter
    def vorticity_strength(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class FractureComponent:
    fracturable: bool
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def fracture(self) -> None:
        """
        Immediately fracture this object into shards at its own center, e.g.
          self.get_component(FractureComponent).fracture()
        """
    def fracture_at_local_point(self, local_point: Vector3) -> None:
        """
        Immediately fracture this object into shards, using localPoint (in this object's local/model space) as the impact point that seeds the fracture pattern, e.g.
          fc.fracture_at_local_point(Vector3(0.5, 0, 0))
        """
    def fracture_at_world_point(self, world_point: Vector3) -> None:
        """
        Immediately fracture this object into shards, using worldPoint (world-space) as the impact point that seeds the fracture pattern, e.g.
          fc.fracture_at_world_point(hit.point)
        """
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_owner(self) -> Object:
        ...
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
        ...
    def set_impulse_threshold(self, impulse_threshold: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_max_fracture_generations(self, max_fracture_generations: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    def set_min_fragment_area(self, min_fragment_area: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_rest_density(self, rest_density: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_shard_count(self, shard_count: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def generation(self) -> int:
        """
        How many times this object (or its source ancestor) has already fractured
        """
    @property
    def impulse_threshold(self) -> float:
        ...
    @impulse_threshold.setter
    def impulse_threshold(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def max_fracture_generations(self) -> int:
        ...
    @max_fracture_generations.setter
    def max_fracture_generations(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
    @property
    def min_fragment_area(self) -> float:
        ...
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
        ...
    @rest_density.setter
    def rest_density(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def shard_count(self) -> int:
        ...
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
        ...
    @staticmethod
    def is_mouse_button_pressed(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @staticmethod
    def is_mouse_button_released(button: typing.SupportsInt | typing.SupportsIndex) -> bool:
        ...
    @staticmethod
    def on_key_just_pressed(key: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        ...
    @staticmethod
    def on_key_pressed(key: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        """
        Fires every frame while the key is held. Returns an id usable with remove_key_pressed_callback().
        """
    @staticmethod
    def on_key_released(key: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        ...
    @staticmethod
    def on_mouse_button_just_pressed(button: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        ...
    @staticmethod
    def on_mouse_button_pressed(button: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        ...
    @staticmethod
    def on_mouse_button_released(button: typing.SupportsInt | typing.SupportsIndex, callback: collections.abc.Callable) -> tuple[int, int]:
        ...
    @staticmethod
    def remove_key_just_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    @staticmethod
    def remove_key_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    @staticmethod
    def remove_key_released_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    @staticmethod
    def remove_mouse_button_just_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    @staticmethod
    def remove_mouse_button_pressed_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
    @staticmethod
    def remove_mouse_button_released_callback(id: tuple[typing.SupportsInt | typing.SupportsIndex, typing.SupportsInt | typing.SupportsIndex]) -> None:
        ...
class Object:
    hidden: bool
    name: str
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
        Attach a component instance to this Object, e.g. obj.add_component(RenderComponent)
        """
    def add_object(self, obj: Object, parent: Object = None) -> Object:
        """
        Add a newly created Object to the scene, optionally parented to another Object
        """
    def get_children(self) -> list[Object]:
        ...
    def get_children_count(self) -> int:
        ...
    def get_component(self, component_class: typing.Any) -> typing.Any:
        """
        Look up a component on this Object
        """
    def get_parent(self) -> Object:
        ...
    def get_parent_id(self) -> int:
        ...
    def has_component(self, component: typing.Any) -> bool:
        """
        Check if this Object has a component of the given type, e.g. obj.has_component(RenderComponent)
        """
    def hide(self) -> None:
        ...
    def remove_component(self, component_class: typing.Any) -> None:
        """
        Remove a component of the given type from this Object, e.g. obj.remove_component(RenderComponent)
        """
    def remove_object(self, obj: Object) -> None:
        """
        Remove an object from the scene
        """
    def set_name(self, name: str) -> None:
        ...
    def show(self) -> None:
        ...
    @property
    def children(self) -> list[Object]:
        ...
    @property
    def id(self) -> int:
        ...
    @property
    def parent(self) -> Object:
        ...
    @property
    def parent_id(self) -> int:
        ...
class PointMass:
    velocity: Vector3
    world_pos: Vector3
    def __repr__(self) -> str:
        ...
    def get_world_position(self) -> Vector3:
        ...
    def set_base_acceleration(self, base_acceleration: Vector3) -> None:
        ...
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_point_radius(self, point_radius: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_velocity(self, velocity: Vector3) -> None:
        ...
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
        Persistent acceleration such as gravity, e.g. Vector3(0, -9.8, 0)
        """
    @base_acceleration.setter
    def base_acceleration(self, arg1: Vector3) -> None:
        ...
    @property
    def index(self) -> int:
        ...
    @property
    def inverse_mass(self) -> float:
        ...
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def is_center(self) -> bool:
        ...
    @property
    def local_pos(self) -> Vector3:
        """
        Rest position in the parent object's local/model space
        """
    @property
    def mass(self) -> float:
        ...
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def point_radius(self) -> float:
        ...
    @point_radius.setter
    def point_radius(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def soft_body(self) -> SoftBodyComponent:
        """
        The SoftBodyComponent this point mass belongs to
        """
class PolygonShape:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, points: collections.abc.Sequence[Vector3]) -> None:
        """
        Build a polygon from a list of Vector3 points in local coordinates, e.g. [Vector3(0,0,0), Vector3(1,0,0), Vector3(0,1,0)]
        """
    @property
    def vertices(self) -> list[float]:
        ...
    @vertices.setter
    def vertices(self, arg0: collections.abc.Sequence[typing.SupportsFloat | typing.SupportsIndex]) -> None:
        ...
class PrismaticConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object = None, dir: Vector3 = ...) -> None:
        """
        Create a prismatic (slider) constraint at object_a's and object_b's centers by default, constraining relative motion to the line between them, e.g.
          pc = PrismaticConstraint(self.owner, target)
          cc.add_constraint(pc)
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
        ...
    @property
    def edge_index(self) -> int:
        ...
    @property
    def hit(self) -> bool:
        ...
    @property
    def is_soft_body(self) -> bool:
        ...
    @property
    def normal(self) -> Vector3:
        ...
    @property
    def object(self) -> Object:
        ...
    @property
    def point(self) -> Vector3:
        ...
class RectangleShape:
    center: Vector3
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, center: Vector3, width: typing.SupportsFloat | typing.SupportsIndex, height: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def height(self) -> float:
        ...
    @height.setter
    def height(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def width(self) -> float:
        ...
    @width.setter
    def width(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class RenderComponent:
    color: Vector4
    enable: bool
    shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
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
        ...
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
        ...
    def set_shape(self, shape: fusion.PolygonShape | fusion.RectangleShape | fusion.CircleShape) -> None:
        """
        Accepts a RectangleShape, CircleShape, or PolygonShape
        """
    def set_texture(self, virtual_path: str) -> None:
        """
        Load a texture from a res:// path (e.g. 'res://textures/wood.png'), or pass '' to clear it
        """
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def z_index(self) -> int:
        ...
    @z_index.setter
    def z_index(self, arg1: typing.SupportsInt | typing.SupportsIndex) -> None:
        ...
class RevoluteConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object = None) -> None:
        """
        Create a revolute (hinge) constraint pinned at object_a's and object_b's centers by default, e.g.
          rc = RevoluteConstraint(self.owner, target)
          cc.add_constraint(rc)
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3) -> None:
        """
        Create a revolute constraint pinned at explicit local-space attach points on each object.
        """
class RigidBodyComponent:
    acceleration: Vector2
    enable: bool
    net_force: Vector2
    velocity: Vector3
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
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
        ...
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
        ...
    def set_angular_acceleration(self, angular_acceleration: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_angular_damping(self, angular_damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_angular_velocity(self, angular_velocity: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_enable(self, arg0: bool) -> None:
        ...
    def set_inertia(self, inertia: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_inverse_inertia(self, inverse_inertia: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_linear_damping(self, linear_damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_net_force(self, net_force: Vector2) -> None:
        ...
    def set_torque(self, torque: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_velocity(self, velocity: Vector3) -> None:
        ...
    @property
    def angular_acceleration(self) -> float:
        ...
    @angular_acceleration.setter
    def angular_acceleration(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def angular_damping(self) -> float:
        ...
    @angular_damping.setter
    def angular_damping(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def angular_velocity(self) -> float:
        ...
    @angular_velocity.setter
    def angular_velocity(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inertia(self) -> float:
        ...
    @inertia.setter
    def inertia(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_inertia(self) -> float:
        ...
    @inverse_inertia.setter
    def inverse_inertia(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_mass(self) -> float:
        ...
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def linear_damping(self) -> float:
        ...
    @linear_damping.setter
    def linear_damping(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def mass(self) -> float:
        ...
    @mass.setter
    def mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def torque(self) -> float:
        ...
    @torque.setter
    def torque(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
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
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
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
        ...
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
    enable: bool
    gas_pressure_enabled: bool
    velocity: Vector3
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
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
        ...
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
        ...
    def set_enable(self, arg0: bool) -> None:
        ...
    def set_gas_amount(self, gas_amount: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_gas_pressure_enabled(self, enabled: bool) -> None:
        """
        Enable gas pressue mode
        """
    def set_inverse_mass(self, inverse_mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_mass(self, mass: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_stiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_velocity(self, velocity: Vector3) -> None:
        ...
    @property
    def acceleration(self) -> Vector3:
        """
        Current acceleration of the center point mass (gravity + accumulated forces)
        """
    @property
    def center_point_mass(self) -> PointMass:
        ...
    @property
    def damping(self) -> float:
        ...
    @damping.setter
    def damping(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def gas_amount(self) -> float:
        ...
    @gas_amount.setter
    def gas_amount(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def inverse_mass(self) -> float:
        ...
    @inverse_mass.setter
    def inverse_mass(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def mass(self) -> float:
        ...
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
        ...
    @property
    def stiffness(self) -> float:
        ...
    @stiffness.setter
    def stiffness(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class SpringConstraint(Constraint):
    @typing.overload
    def __init__(self, object_a: Object, length: typing.SupportsFloat | typing.SupportsIndex, object_b: Object = None, stiffness: typing.SupportsFloat | typing.SupportsIndex = 15.0, damping: typing.SupportsFloat | typing.SupportsIndex = 7.0) -> None:
        """
        Create a spring constraint attached at object_a's and object_b's centers by default, e.g.
          sc = SpringConstraint(self.owner, target, 5.0)
          cc.add_constraint(sc)
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, length: typing.SupportsFloat | typing.SupportsIndex, stiffness: typing.SupportsFloat | typing.SupportsIndex = 15.0, damping: typing.SupportsFloat | typing.SupportsIndex = 7.0) -> None:
        """
        Create a spring constraint at explicit local-space attach points on each object.
        """
    def set_damping(self, damping: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_length(self, length: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_stiffness(self, stiffness: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def damping(self) -> float:
        ...
    @damping.setter
    def damping(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def length(self) -> float:
        ...
    @length.setter
    def length(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def stiffness(self) -> float:
        ...
    @stiffness.setter
    def stiffness(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
class TransformComponent:
    enable: bool
    size: Vector3
    world_position: Vector3
    def add_child(self, obj: Object) -> Object:
        """
        Add obj as a child of this component's owning Object
        """
    def add_component(self, component_class: typing.Any) -> typing.Any:
        """
        Attach a new component of the given type to this component's owning Object, e.g. render = self.add_component(RenderComponent)
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
        ...
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
        ...
    def set_rotation(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_rotation_degrees(self, arg0: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    def set_size(self, arg0: Vector3) -> None:
        ...
    def to_local_coordinates(self, arg0: Vector3) -> None:
        ...
    def to_world_coordinates(self, arg0: Vector3) -> None:
        ...
    def update_world_position(self, arg0: Vector3) -> None:
        ...
    @property
    def owner(self) -> Object:
        """
        The Object that owns this component
        """
    @property
    def rotation(self) -> float:
        ...
    @rotation.setter
    def rotation(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def rotation_degrees(self) -> float:
        ...
    @rotation_degrees.setter
    def rotation_degrees(self, arg1: typing.SupportsFloat | typing.SupportsIndex) -> None:
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
        Create a weld constraint at object_a's and object_b's centers by default, locking their relative position and rotation, e.g.
          wc = WeldConstraint(self.owner, target)
          cc.add_constraint(wc)
        """
    @typing.overload
    def __init__(self, object_a: Object, object_b: Object, attach_point_a: Vector3, attach_point_b: Vector3, angular_offset: typing.SupportsFloat | typing.SupportsIndex = 0.0) -> None:
        """
        Create a weld constraint at explicit local-space attach points on each object.
        """
    def set_angular_offset(self, angular_offset: typing.SupportsFloat | typing.SupportsIndex) -> None:
        ...
    @property
    def angular_offset(self) -> float:
        ...
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
    Load a scene from a res:// path and add it as a child of parent (or as a root-level object if parent is None). Returns the newly created root Object of the loaded scene, e.g.   enemy = add_scene('res://enemy.fscene', self.owner)
      enemy.get_component(TransformComponent).world_position = spawn_point
    """
def export(value: typing.Any) -> _ExportMarker:
    """
    Mark a script attribute as editable in the inspector using the default widget for its type, e.g.
      name = export("Goblin")
      hp = export(100)
    For customizable export, use the appropriate export function: export_range, export_color_picker
    """
def export_angle_slider(value: typing.Any, min_degrees: typing.SupportsFloat | typing.SupportsIndex = -360.0, max_degrees: typing.SupportsFloat | typing.SupportsIndex = 360.0) -> _ExportMarker:
    """
    Mark a float script attribute (stored in radians) as editable with an angle slider displayed in degrees, e.g.
      facing = export_angle_slider(0.0)
      cone_angle = export_angle_slider(0.5, 0.0, 180.0)
    """
def export_color_edit(value: typing.Any) -> _ExportMarker:
    """
    Mark a Vector3 or Vector4 script attribute as editable with a color swatch that opens a picker popup, e.g.
      tint = export_color_edit(Vector4(1, 1, 1, 1))
    """
def export_color_picker(value: typing.Any) -> _ExportMarker:
    """
    Mark a Vector3 or Vector4 script attribute as editable with a full color picker always shown inline, e.g.
      glow_color = export_color_picker(Vector3(0.2, 0.8, 1.0))
    """
def export_drag(value: typing.Any, min: typing.SupportsFloat | typing.SupportsIndex = 0.0, max: typing.SupportsFloat | typing.SupportsIndex = 0.0, prefix: str = '', suffix: str = '') -> _ExportMarker:
    """
    Mark a script attribute as editable with a click-and-drag field. min=max=0 (the default) means unbounded, e.g.
      jump_force = export_drag(15.0)
      ammo = export_drag(30, 0, 999)
    """
def export_file(value: typing.Any, extension: str = '*.*') -> _ExportMarker:
    """
    Mark a str script attribute as editable with a file picker that stores a res:// virtual path. Clicking opens a file dialog; files can also be dragged in from the resource browser. extension filters which files are shown/accepted, using ';'-separated glob patterns, e.g.
      icon = export_file("", "*.png;*.jpg;*.jpeg")
    """
def export_range(value: typing.Any, min: typing.SupportsFloat | typing.SupportsIndex = ..., max: typing.SupportsFloat | typing.SupportsIndex = ..., slider: bool = False, prefix: str = '', suffix: str = '') -> _ExportMarker:
    """
    Mark a script attribute as editable within a min/max range. Shown as a bounded slider by default; pass slider=False for a plain input field that still applies min/max (and any prefix/suffix), e.g.
      speed = export_range(200.0, 0.0, 500.0)
      hp = export_range(100, 0, 999, slider=False, suffix=" hp")
    """
def export_scene(value: typing.Any) -> _ExportMarker:
    """
    Mark a str script attribute as editable with a file picker restricted to .fscene files, storing a res:// virtual path, e.g.
      next_level = export_scene("res://levels/level_2.fscene")
    """
def export_section(name: str) -> typing.Any:
    """
    Create a collapsible inspector section. All exported properties following this marker are displayed inside the section until another section marker is encountered. Can be used as a bare statement, e.g.
      export_section("Visuals")
      color = export_color_edit(Vector4(1, 1, 1, 1))
    """
def export_sub_section(name: str) -> typing.Any:
    """
    Create a collapsible inspector sub-section, nested inside whichever export_section is currently open (or at the top level if none is). Properties following this marker are displayed inside it until another section or sub-section marker is encountered. Can be used as a bare statement, e.g.
      export_section("Movement")
      speed = export(5.0)
      export_sub_section("Advanced")
      acceleration_curve = export(1.0)
    """
def find_objects_with_component(component_class: typing.Any) -> list[Object]:
    """
    Every Object in the scene that has the given component type, e.g.
      enemies = find_objects_with_component(Enemy)
    """
def get_all_objects() -> list[Object]:
    """
    Every Object currently in the scene. Useful for linear searches instead of maintaining your own registry, e.g.
      enemies = [o for o in get_all_objects() if o.has_component(Enemy)]
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
    Load a scene from a res:// path, replacing the current live scene, e.g.
      load_scene('res://levels/level_2.fscene')
    """
FluidVsRigid: CollisionType  # value = <CollisionType.FluidVsRigid: 5>
FluidVsSoft: CollisionType  # value = <CollisionType.FluidVsSoft: 6>
RigidVsRigid: CollisionType  # value = <CollisionType.RigidVsRigid: 0>
RigidVsSoft: CollisionType  # value = <CollisionType.RigidVsSoft: 3>
RigidVsStatic: CollisionType  # value = <CollisionType.RigidVsStatic: 1>
SoftVsSoft: CollisionType  # value = <CollisionType.SoftVsSoft: 4>
StaticVsStatic: CollisionType  # value = <CollisionType.StaticVsStatic: 2>
