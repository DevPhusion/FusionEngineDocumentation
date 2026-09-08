# Fusion Engine

Fusion Engine is a 2D game engine built specifically for creating reinforcement
learning (RL) training environments, scripted entirely in Python. Its
component model is inspired by Unity and its nested-scene model by Godot, but
unlike either of those, the engine's whole purpose is producing lightweight,
fast-stepping environments to train RL agents in — not shipping games.

!!! note "Platform support"
    Fusion Engine currently only runs on **Windows**. There is no macOS or
    Linux support at this time.

This site covers the **Python scripting API** — the surface you write scripts
against. For the engine's internal architecture (the rendering pipeline, the
three physics solvers, the ECS, the editor, and the export pipeline) see the
[design document (PDF)](https://github.com/DevPhusion/FusionEngine/blob/master/Fusion_Engine_Design_Document.pdf).

## Where to start

- **New to Fusion?** Start with [Getting Started](getting-started.md) — install
  the engine, create a project, and attach your first script.
- **Writing scripts?** See the [Scripting Guide](scripting-guide.md) for the
  full Python API: components, exports, physics, input, and RL agents.
- **Looking up a class or function?** Jump into the
  [API Reference](api/index.md).

## How the engine fits together

| System | Responsibility |
|---|---|
| Rendering Engine | OpenGL-based rasterization renderer |
| Physics Engine | Rigid body (PGS), soft body (XPBD), and fluid (PBF) simulation, unified through a shared impulse-based coupling layer |
| Object and Component Manager | Manages entities and their components (ECS) |
| Editor | ImGui-based editor UI, windows, and gizmos |
| File and Project Manager | Project/scene serialization, resource paths (`res://`), and export |
| Script Manager | The C++ ↔ Python bridge (pybind11) and script lifecycle |

Reinforcement learning support (the `fusion.RL` module, the `AgentComponent`,
headless training, and the training monitor) is an **optional package**, not
part of the base engine — you enable it from the project configuration
screen, and it's what pulls in Gymnasium, Stable-Baselines3, NumPy, and
PyTorch into your project's virtual environment.

## Quick example

Every Fusion script starts with `from fusion import *`, so the engine's
classes and functions (`Script`, `Vector3`, `export`, component types, and so
on) are available unqualified:

```python
from fusion import *


class Enemy(Script):
    speed = export(3.0)

    def OnStart(self):
        self.transform = self.get_component(TransformComponent)

    def Process(self, delta):
        self.transform.world_position += Vector3(self.speed * delta, 0, 0)
```

`speed` here is an **exported property** — `export(3.0)` makes it show up as
an editable field in the inspector, defaulting to `3.0`, while still working
as a normal Python attribute in code. See
[Exporting properties](scripting-guide.md#exporting-properties-to-the-inspector)
for the full set of export widgets (ranges, drag fields, color pickers, file
pickers, and collapsible sections).