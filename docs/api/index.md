# API Reference

Auto-generated from the engine's `fusion.pyi` stub, which is itself
generated from the docstrings written directly into the C++ bindings — so
this reference stays in sync with the engine without hand-copying anything.

## Components

| Component | Purpose |
|---|---|
| [RenderComponent](render-component.md) | Shape, color, texture, z-index |
| [TransformComponent](transform-component.md) | Position, rotation, scale |
| [RigidBodyComponent](rigidbody-component.md) | Rigid body simulation |
| [CollisionComponent](collision-component.md) | Collision shapes, layers, callbacks |
| [SoftBodyComponent](softbody-component.md) | XPBD soft body simulation |
| [FluidComponent](fluid-component.md) | PBF fluid simulation |
| [GasComponent](gas-component.md) | PBF extended for gas simulation |
| [ConstraintComponent](constraint-component.md) | Joints between objects |
| [FractureComponent](fracture-component.md) | Voronoi fracture on impact |
| [CameraComponent](camera-component.md) | Camera range, main camera |
| [AudioComponent](audio-component.md) | Audio, SFX |
| [AgentComponent](agent-component.md) | RL observations/rewards/actions |

## Other modules

- [Math (Vector2/3/4)](math.md)
- [Object](object.md)
- [Physics & Constraints](physics.md)
- [Input](input.md)
- [Console](console.md)
- [File](file.md)
- [Render (debug draw)](render-module.md)
- [Scene](scene.md)
- [Export markers](export.md)
- [Reinforcement Learning](rl.md) — requires the `rl` package
