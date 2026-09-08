# Scripting Guide

Every script starts with:

```python
from fusion import *
```

This is a deliberate convention, not just a style choice — it's what makes
`Script`, `Vector3`, `export`, component classes, `Input`, `Console`, and
everything else in this guide available unqualified in your scripts.

Every script is a class inheriting from `Script`:

```python
from fusion import *


class Enemy(Script):
    def OnStart(self):
        ...

    def Process(self, delta):
        ...
```

- **`OnStart(self)`** runs once, during the "start" pass the engine runs
  over newly added objects (after an initial "load" pass has already run).
- **`Process(self, delta)`** runs once per frame. `delta` is elapsed time in
  seconds.

## Talking to the rest of the object

`Script`, and every component class, share the same small set of mixin
methods for navigating the object they're attached to:

| Method / property | What it does |
|---|---|
| `self.owner` / `self.get_owner()` | The `Object` this script/component is attached to |
| `self.get_component(ComponentClass)` | Look up a component on the owning object, or `None` |
| `self.has_component(ComponentClass)` | Check for a component without fetching it |
| `self.add_component(ComponentClass)` | Attach a new component to the owning object; raises if one already exists |
| `self.remove_component(ComponentClass)` | Remove a component from the owning object |
| `self.add_object(obj, parent=None)` | Insert a freshly created (not-yet-added) `Object` into the scene |
| `self.add_child(obj)` | Insert `obj` into the scene as a child of the owning object |
| `self.remove_object(obj)` | Remove an object from the scene |

```python
class Enemy(Script):
    def OnStart(self):
        self.transform = self.get_component(TransformComponent)
        self.render = self.get_component(RenderComponent)

        if not self.has_component(RigidBodyComponent):
            self.add_component(RigidBodyComponent)
```

`ComponentClass` can be any built-in component (`TransformComponent`,
`RenderComponent`, ...) or any of your own `Script` subclasses — script
classes are auto-registered as component types the first time they're used
this way, as long as they're importable from a real `res://` file path.

## Exporting properties to the inspector

`export()` and its variants mark a script attribute as editable in the
editor's inspector. They're used as class-level assignments:

```python
from fusion import *


class Enemy(Script):
    name = export("Goblin")
    hp = export_range(100, 0, 999, suffix=" hp")
    speed = export_drag(200.0, 0.0, 500.0)
    facing = export_angle_slider(0.0)
    tint = export_color_edit(Vector4(1, 1, 1, 1))
    icon = export_file("", "*.png;*.jpg;*.jpeg")
```

| Function | Accepts | Notes |
|---|---|---|
| `export(value)` | anything | Default inspector widget for the value's type |
| `export_range(value, min=-inf, max=inf, slider=False, prefix="", suffix="")` | `int`, `float`, `Vector2`, `Vector3`, `Vector4` | Bounded slider by default; `slider=False` gives a plain bounded input field |
| `export_drag(value, min=0.0, max=0.0, prefix="", suffix="")` | `int`, `float`, `Vector2`, `Vector3`, `Vector4` | Click-and-drag field; `min == max == 0` (the default) means unbounded |
| `export_angle_slider(value, min_degrees=-360, max_degrees=360)` | `float` (stored in **radians**) | Displayed as a degree slider |
| `export_color_edit(value)` | `Vector3`, `Vector4` | Swatch that opens a picker popup |
| `export_color_picker(value)` | `Vector3`, `Vector4` | Full picker shown inline |
| `export_file(value, extension="*.*")` | `str` | File picker storing a `res://` path; `extension` is a `;`-separated glob filter, e.g. `"*.png;*.jpg"` |
| `export_scene(value)` | `str` | Same as `export_file`, restricted to `*.fscene` |
| `export_section(name)` | — | Collapsible inspector section; used as a bare statement, groups everything below it until the next section/sub-section marker |
| `export_sub_section(name)` | — | Same, nested inside the current section |

```python
class Enemy(Script):
    export_section("Movement")
    speed = export(5.0)
    export_sub_section("Advanced")
    acceleration_curve = export(1.0)

    export_section("Visuals")
    tint = export_color_edit(Vector4(1, 1, 1, 1))
```

### Loading scripts dynamically

```python
::: fusion.get_script
```

For normal use you should just `import` a script class directly (e.g.
`from scripts.enemy import Enemy`); `get_script(path)` is only for genuinely
data-driven loading, where the class to instantiate isn't known until
runtime.

## Math types

`Vector2`, `Vector3`, and `Vector4` all support the arithmetic you'd expect:
`+`, `-`, componentwise `*`, `* float`, `/ float`, unary `-`, `==`, `!=`,
indexing (`v[0]`), and `len(v)`.

```python
a = Vector3(1, 0, 0)
b = Vector3(0, 1, 0)
c = a + b * 2.0
d = a.dot(b)
n = a.cross(b)          # Vector3 only
mid = Vector3.lerp(a, b, 0.5)
```

A quirk worth knowing: `Vector2` calls its unit-length method
**`normalize()`**, while `Vector3` and `Vector4` call it **`normalized()`**.
On all three it returns a *new* vector rather than mutating in place, so the
`Vector2` name is a bit of a misnomer — just something to remember when you
switch between vector types.

`Vector4` additionally exposes `.r/.g/.b/.a` as aliases for `.x/.y/.z/.w`
for color use.

There's also a free function for plain floats:

```python
t = lerp(0.0, 10.0, 0.25)  # 2.5
```

## Console output

```python
Console.Print("hello")
Console.PrintWarning("something looks off")
Console.PrintError("something broke")
```

These write to the editor's Console window, tagged Info/Warning/Error.

## Input

```python
class PlayerController(Script):
    def OnStart(self):
        self.on_jump_id = Input.on_key_just_pressed(Key.SPACE, self.jump)

    def Process(self, delta):
        if Input.is_key_pressed(Key.D):
            ...  # held every frame

    def jump(self):
        ...
```

| Method | Fires |
|---|---|
| `Input.is_key_pressed(key)` | Every frame the key is held |
| `Input.is_key_just_pressed(key)` | Only the frame the key was pressed |
| `Input.is_key_released(key)` | Only the frame the key was released |
| `Input.is_mouse_button_pressed/just_pressed/released(button)` | Same, for mouse buttons |

Each `is_*` check also has an `on_*` callback registration
(`on_key_pressed`, `on_key_just_pressed`, `on_key_released`,
`on_mouse_button_pressed`, `on_mouse_button_just_pressed`,
`on_mouse_button_released`) — each returns an id you pass to the matching
`remove_*_callback()` to unregister it later.

`Key` and `Mouse` are submodules of key/button constants:
`Key.SPACE`, `Key.ENTER`, `Key.ESCAPE`, `Key.LEFT_SHIFT`, `Key.LEFT_CONTROL`,
`Key.LEFT_ALT`, `Key.UP/DOWN/LEFT/RIGHT`, `Key.A`–`Key.Z`, `Key.NUM_0`–
`Key.NUM_9`, and `Mouse.LEFT/RIGHT/MIDDLE`.

## Objects and scenes

```python
enemy = Object()               # not yet in the scene
self.add_object(enemy)         # or self.add_child(enemy) to parent it to self.owner

for o in get_all_objects():
    ...

goblins = find_objects_with_component(Enemy)
```

An `Object` has `name`, `hidden`, a readonly `id`, `parent`/`parent_id`, and
`children`, plus `get_component`/`add_component`/`has_component`/
`remove_component` and `add_object`/`add_child`/`remove_object`, matching
the mixin methods above.

Loading scenes:

```python
load_scene("res://levels/level_2.fscene")   # replaces the current scene

enemy = add_scene("res://enemy.fscene", self.owner)   # adds as a child, runs its scripts
enemy.get_component(TransformComponent).world_position = spawn_point
```

## Files and resources

Resources are addressed by `res://` virtual paths internally. Convert
between those and real filesystem paths when you need to:

```python
abs_path = File.virtual_to_absolute(self.icon)      # res:// -> real path
virtual_path = File.absolute_to_virtual(abs_path)    # real path -> res://
```

## Components

Every built-in component follows the same shape as scripts: it has
`get_component`/`has_component`/`add_component`/`remove_component`/`owner`,
plus an `enable` property and `set_enable(bool)`.

### TransformComponent

`world_position` (`Vector3`), `rotation` (radians), `rotation_degrees`,
`size` (`Vector3` scale), and `to_local_coordinates(world_point)` /
`to_world_coordinates(local_point)`.

### RenderComponent

`color` (`Vector4`), `z_index` (`int`), `shape` (a `RectangleShape`,
`CircleShape`, or `PolygonShape`), `set_shape(shape)`, and
`set_texture(virtual_path)` — pass `""` to clear the texture.

### RigidBodyComponent

Rigid-body dynamics driven by the PGS solver:

```python
rb = self.get_component(RigidBodyComponent)
rb.velocity = Vector3(0, -2, 0)
rb.add_force(Vector2(0, 50))
rb.mass = 2.0
```

`velocity` (`Vector3`), `angular_velocity`/`angular_acceleration` (`float`),
`acceleration`/`net_force` (`Vector2` — note these two are 2D even though
`velocity` is a `Vector3`), `torque`, `mass`/`inverse_mass`,
`inertia`/`inverse_inertia` (plus `recalculate_inertia()` after resizing a
shape), `linear_damping`/`angular_damping`, and `add_force(force)` /
`add_force_at_world_point(force, point)` / `add_force_at_local_point(force,
point)`.

### CollisionComponent

Can hold multiple named shapes, only one of which is the *resolution
shape* — the one physics actually resolves against; the rest stay usable
for detection only.

```python
col = self.get_component(CollisionComponent)
detector_id = col.add_shape(CircleShape(Vector3(0, 0, 0), 3.0), "Aggro Radius")
col.set_resolution_shape_id(-1)   # detect on every shape, resolve on none

def on_enter(data: CollisionEventData):
    Console.Print(f"hit {data.other.name}")

col.add_collision_enter_callback(on_enter)
```

Key members: `is_static`, `collision_layer`/`collision_mask`
(`CollisionLayer`/`CollisionMask` bit flags — combine with `|`),
`sync_with_render_component`, `shape`/`set_shape(shape)` (applies to the
resolution shape), `add_shape(shape, name="")` → shape id,
`remove_shape(shape_id)`, `get_shape_ids()`, `get_shape(shape_id)`/
`set_shape(shape_id, shape)`, `get_shape_name`/`set_shape_name`,
`get_shape_id(name)` (-1 if not found), `get_shape_center`/`get_shape_area`,
`resolution_shape_id` (-1 = detection-only, nothing resolved),
`is_grounded(probe_length=0.15)`, and three pairs of collision callbacks —
`add_collision_callback` (fires every physics substep two shapes overlap),
`add_collision_enter_callback` (fires once when a collision begins), and
`add_collision_exit_callback` (fires once when it ends) — each with a
matching `remove_*_callback(id)`.

### SoftBodyComponent

XPBD-based soft bodies made of point masses:

```python
sb = self.get_component(SoftBodyComponent)
sb.stiffness = 200.0
sb.add_force(Vector3(0, -9.8, 0))
center = sb.center_point_mass
```

`mass`/`inverse_mass`, `velocity`, `acceleration` (readonly, center point
mass), `stiffness`, `damping`, `gas_pressure_enabled`/`gas_amount` (for
inflatable objects modeled with the ideal gas law), `point_mass_count`,
`get_point_mass(index)` (index `size - 1` is always the center),
`mass_aggregate` (all point masses, center last), `center_point_mass`,
`add_force(force)` (uniform across every point mass),
`add_force_at_center(force)`, `add_force_at_world_point`/
`add_force_at_local_point(force, point)` (distributed across the nearest
point masses), and `add_point_mass(local_point)`.

Each `PointMass` has `index`, `is_center`, `soft_body` (its owning
`SoftBodyComponent`), `point_radius`, `local_pos` (readonly rest position),
`world_pos`/`update_world_position(pos)` (moves it immediately, bypassing
springs), `velocity`, `acceleration` (readonly total), `base_acceleration`
(persistent, e.g. gravity), and `mass`/`inverse_mass`.

### FluidComponent

Position Based Fluids:

```python
fluid = self.get_component(FluidComponent)
fluid.desired_particle_count = 500       # re-seeds the whole fluid
fluid.add_particle(Vector3(0, 3, 0))     # add one extra particle on top
```

`particle_radius`, `metaball_threshold`/`metaball_edge_soft`/
`outline_width_texels` (rendering), `desired_particle_count` (changing this
re-seeds the fluid on its source shape and discards any manually-added
particles), `collision_radius`, `smoothing_radius`, `epsilon`,
`particle_mass`, `rest_density`, `viscosity`, `vorticity_strength`,
`particle_count`/`particles` (readonly), `get_particle(index)`,
`add_particle(world_position)` (single particle) or `add_particle(shape,
particle_count)` (seed a shape), `remove_particle(particle)`, `reseed()`
(discard everything and refill per `desired_particle_count`), and
`update_collision_layer_mask()` to sync particles with the object's
`CollisionComponent`.

Each `FluidParticle` exposes `position`, `predicted_position` (readonly,
this substep's solver estimate), `velocity`, `collision_radius`, `mass`/
`inverse_mass`, `rest_density`, `density` (readonly, solver output),
`viscosity`, `smoothing_radius`, `epsilon`, `vorticity_strength`, and
`lambda` (readonly, the PBF constraint multiplier from the last substep).

### ConstraintComponent and Constraints

```python
cc = self.add_component(ConstraintComponent)
cc.add_constraint(DistanceConstraint(self.owner, target, distance=5.0))
```

`ConstraintComponent` holds `constraints` (owned as Object A) and
`mirrored_constraints` (readonly — constraints another object owns where
this object is Object B), plus `add_constraint`, `remove_constraint`
(by instance or index), and `get_constraint_count()`.

Every constraint type shares: `name` (readonly), `beta`, `draw_constraint`,
`object_a`/`object_b` (readonly, use `set_object_a`/`set_object_b` to
change), `use_center_a`/`use_center_b`, `attach_point_a`/`attach_point_b`
(local space; setting either disables the matching `use_center_*`), and
`get_attach_world_a()`/`get_attach_world_b()`.

| Constraint | Constructor (center-attached) | Also editable |
|---|---|---|
| `DistanceConstraint` | `(object_a, object_b=None, distance, extendable=False, retractable=False)` | `distance`, `extendable`, `retractable` |
| `SpringConstraint` | `(object_a, object_b=None, length, stiffness=15.0, damping=7.0)` | `length`, `stiffness`, `damping` |
| `RevoluteConstraint` | `(object_a, object_b=None)` | — |
| `WeldConstraint` | `(object_a, object_b=None, angular_offset=0.0)` | `angular_offset` |
| `PrismaticConstraint` | `(object_a, object_b=None, dir=Vector3(1,0,0))` | `dir` (readonly — use `relock_direction()`) |

Every constraint also has an overload taking explicit local-space
`attach_point_a`/`attach_point_b` instead of defaulting to each object's
center — e.g. `DistanceConstraint(object_a, object_b, attach_point_a,
attach_point_b, distance)`.

### FractureComponent

Voronoi-based fracture, driven by impulse:

```python
fc = self.get_component(FractureComponent)
fc.impulse_threshold = 50.0
fc.fracture_at_world_point(hit.point)
```

`fracturable`, `impulse_threshold`, `shard_count`, `min_fragment_area`,
`max_fracture_generations`, `generation` (readonly — how many times this
object, or its source ancestor, has already fractured), `rest_density`, and
`fracture()` / `fracture_at_world_point(point)` /
`fracture_at_local_point(point)`.

### CameraComponent

`range` / `get_range()` / `set_range(range)`, and `is_main` (setting `True`
on one camera does **not** automatically unset another camera's `is_main`).

## Shapes

```python
RectangleShape(center, width, height)
CircleShape(center, radius, segments=30, physics_segments=30)
PolygonShape([Vector3(0, 0, 0), Vector3(1, 0, 0), Vector3(0, 1, 0)])  # min 3 points
```

Used for both `RenderComponent.shape`/`CollisionComponent` shapes and shape
arguments elsewhere (e.g. `Physics.raycast`, `FluidComponent.add_particle`).

## Physics queries

```python
hit = Physics.raycast(pos, Vector3(0, -1, 0), 5.0,
                       CollisionMask.LAYER_1, [self.owner])
if hit:
    Console.Print(f"hit {hit.object.name} at {hit.distance}")

for h in Physics.raycast_all(pos, Vector3(1, 0, 0), 10.0):
    ...
```

`CollisionLayer`/`CollisionMask` are 16-bit flag enums (`LAYER_1`–
`LAYER_16`) combinable with `|`/`&`/`^`/`~`; `layer_overlap(layer_a, mask_a,
layer_b, mask_b)` checks whether two (layer, mask) pairs would collide.
`RayCastHit` is truthy exactly when `hit.hit` is `True`, and also exposes
`object`, `point`, `normal`, `distance`, `edge_index`, and `is_soft_body`.
`CollisionEventData` (passed to collision callbacks) has `type`
(`CollisionType.RigidVsRigid`, `RigidVsStatic`, `StaticVsStatic`,
`RigidVsSoft`, `SoftVsSoft`, `FluidVsRigid`, `FluidVsSoft`), `self`/`other`,
`shape_id`/`other_shape_id`, `point`, `normal`, and `penetration`.

## Debug drawing

Immediate-mode, one frame at a time — call every frame you want the line
visible:

```python
Render.draw_line(Vector3(0, 0, 0), Vector3(1, 1, 0), Vector4(1, 0, 0, 1))
Render.draw_arrow(pos, Vector3(0, 1, 0), 1.5, Vector4(0, 1, 0, 1))
Render.draw_circle(pos, 1.0, Vector4(1, 1, 0, 1))
Render.draw_filled_polygon(points, Vector4(1, 0, 0, 0.5), Vector4(1, 0, 0, 1))
```

## Reinforcement learning

Only available once the **RL package** is enabled for the project (see
[Getting Started](getting-started.md#enabling-reinforcement-learning)) —
this is what makes `AgentComponent` and `fusion.RL` importable.

Mark an object trainable by attaching an `AgentComponent`, then define its
action/observation spaces (any `gymnasium.spaces` type — `Discrete`,
`MultiDiscrete`, `Box`, `MultiBinary`; observations default to `Box` if you
never set one) and feed it observations/reward each step:

```python
from fusion import *
from gymnasium import spaces


class FlappyAgent(Script):
    def OnStart(self):
        self.agent = self.get_component(AgentComponent)
        self.agent.set_action_space(spaces.Discrete(2))  # flap or don't

    def Process(self, delta):
        self.agent.add_observation(self.velocity_y)
        self.agent.add_observation(self.distance_to_next_pipe)

        if self.agent.action == 1:
            self.flap()

        self.agent.add_reward(0.1)  # survived this tick

        if self.crashed:
            self.agent.set_reward(-1.0)
            self.agent.end_episode()
```

`AgentComponent` members: `add_observation(value)` (a single `float` or a
list of them), `set_observation(values)`, `clear_observation()`,
`add_reward(delta)`/`set_reward(value)`, `end_episode()`,
`set_action_space(space)`/`action_space` (readonly),
`set_observation_space(space)`/`observation_space` (readonly, optional —
otherwise a `Box` is inferred from accumulated observation length),
`action` (readonly — an `int` for `Discrete`, a `list` for
`Box`/`MultiDiscrete`/`MultiBinary`), and `agent_id` (readonly).

For custom stepping — e.g. driving training from your own loop instead of
the editor's built-in training UI — `fusion.RL.Environment` exposes the raw
env functions the engine implements: `get_action_space()`,
`get_observation_space()`, `step(action)` → `(observation, reward, done)`
(advances one physics tick), `reset()` → initial observation (reloads the
scene and runs one priming tick), and `get_snapshot(width=128, height=128)`
→ an `(height, width, 3)` `uint8` RGB array rendered off-screen, which works
even during headless training:

```python
frame = fusionRL.Environment.get_snapshot(84, 84)
self.agent.add_observation((frame.astype("float32") / 255.0).flatten().tolist())
```

Day-to-day training itself — picking an algorithm/policy, timesteps, save
location, and whether to resume from an existing model — is driven from the
editor's training UI and runs through Stable-Baselines3 headlessly (physics
and script updates keep running; rendering and the 60&nbsp;FPS cap don't).
You generally don't need to call the training internals directly.

## Components reference

For the exhaustive, auto-generated signature list of every class covered
above, see the [API Reference](api/index.md#components).