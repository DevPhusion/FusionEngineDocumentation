# Fusion Engine

Fusion Engine is a 2D game engine built for creating reinforcement learning
training environments, scripted entirely in Python.

This site covers the **Python scripting API**. For the engine's internal
architecture, math, and physics solvers, see the
[design document (PDF)](https://github.com/DevPhusion/FusionEngine/blob/main/Fusion_Engine_Design_Document.pdf).

## Where to start

- **New to Fusion?** Start with [Getting Started](getting-started.md).
- **Writing your first script?** See the [Scripting Guide](scripting-guide.md).
- **Looking up a class or function?** Jump straight into the
  [API Reference](api/index.md).

## Quick example

```python
import fusion
from fusion import Vector3, export


class Enemy(fusion.Script):
    speed = export(3.0)

    def OnStart(self):
        self.transform = self.get_component(fusion.TransformComponent)

    def Process(self, delta):
        self.transform.world_position += Vector3(self.speed * delta, 0, 0)
```
