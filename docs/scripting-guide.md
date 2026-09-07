# Scripting Guide

!!! note
    Hand-written page. Mix prose freely with `::: fusion.X` blocks like the
    one below — those blocks pull live signatures/docstrings from the stub.

Every script is a class inheriting from `fusion.Script`. Two lifecycle
methods matter most:

- `OnStart(self)` — called once when the script's object enters the scene.
- `Process(self, delta)` — called every frame.

## Exporting properties to the inspector

Use `export()` and friends to make a script attribute editable in the
editor's inspector panel:

```python
import fusion
from fusion import export, export_range, export_color_edit, Vector4

class Enemy(fusion.Script):
    name = export("Goblin")
    hp = export_range(100, 0, 999)
    tint = export_color_edit(Vector4(1, 1, 1, 1))
```

Full reference for every export function:

::: fusion.export
::: fusion.export_range
::: fusion.export_color_edit

## Components

Scripts talk to the rest of an object through components — see the
[Components section](api/index.md#components) of the API reference for the
full list (`RenderComponent`, `RigidBodyComponent`, `CollisionComponent`,
and so on).
