# Getting Started

## Requirements

- **Windows.** Fusion Engine currently only supports Windows — there's no
  macOS or Linux build.
- **Visual Studio**, but only if you're building from source. The project is
  maintained as a Visual Studio solution and isn't currently set up for
  other IDEs or build systems.
- **Python 3.11** is the version the engine's virtual environments are built
  against. Later 3.x versions are also expected to work, but 3.11 is the
  tested baseline.

## Installing the engine

You have two options: grab a compiled build, or build the engine yourself.

### Option 1 — Official release (recommended)

1. Go to the [Releases](https://github.com/DevPhusion/FusionEngine/releases)
   page.
2. Download the latest `.zip` archive.
3. Extract it to a folder of your choice.
4. Run `FusionApp.exe` to launch the editor.

No additional build tools are required for this path.

### Option 2 — Build from source

1. Clone the repository:

   ```
   git clone https://github.com/DevPhusion/FusionEngine.git
   ```

2. Open the cloned folder in Visual Studio.
3. Build the solution.
4. Run the resulting executable to launch the editor.

## Creating a project

When you create a new Fusion project, the editor sets up a few things for
you alongside your resources folder:

- A **Python virtual environment**, scoped to that project.
- A compiled Python module (`.pyd`) that links the C++ engine core into that
  venv as the `fusion` package (plus `fusionRL`/`fusion_gym` if the RL
  package is enabled — see below).
- A `.pyi` stub file, generated via `pybind-stubgen`, written into a
  `typings/` folder in your project.
- VS Code settings, written automatically, that point VS Code's interpreter
  and stub path at that venv and `typings/` folder — so autocomplete and
  syntax highlighting for the entire engine API work out of the box in any
  script you open.

Two file types make up a project on disk:

| Extension | Description |
|---|---|
| `.fusion` | Project save file — settings and the main scene path |
| `.fscene` | A serialized scene — its objects and components |

Resources (scripts, scenes, textures, etc.) are referenced internally using
`res://` virtual paths rather than absolute filesystem paths, so a project
stays portable across machines. `File.virtual_to_absolute()` and
`File.absolute_to_virtual()` convert between the two when a script needs a
real path — see the [Scripting Guide](scripting-guide.md#files-and-resources).

### Installing extra Python packages

Because each project gets its own venv, you can `pip install` whatever you
need directly into it — NumPy, PyTorch, or anything else your scripts import
— the same way you would for any other Python project.

### Enabling reinforcement learning

RL support ships as an installable package rather than being baked into the
base engine. Turning it on from the project configuration screen does two
things:

- Pulls the required Python libraries (NumPy, PyTorch, Gymnasium,
  Stable-Baselines3) into the project's venv.
- Exposes the engine-side `fusion.RL` API (`AgentComponent`,
  `fusion.RL.Environment`) and adds the training-related editor windows
  (the headless training monitor and live-view toggle).

Installed/selected packages are synced automatically in the background
whenever you open the project, so you generally don't need to manage this
by hand after the initial toggle.

## Your first script

1. Right-click in the resource browser and choose **New Script**.
2. Attach it to an object as a component (drag it onto the object, or use
   the inspector's "Add Component" and pick the script).
3. Double-click it to open it in your editor — with the `typings/` stub in
   place, you get full autocomplete against the real engine API.

Every script is a class inheriting from `Script`, and every script starts
with a wildcard import from the `fusion` package:

```python
from fusion import *


class Mover(Script):
    speed = export(3.0)

    def OnStart(self):
        self.transform = self.get_component(TransformComponent)

    def Process(self, delta):
        self.transform.world_position += Vector3(self.speed * delta, 0, 0)
```

A couple of things worth knowing right away:

- **Lifecycle.** When an object (and its scripts) enters the scene, the
  engine runs a *load* pass over the new objects followed by a *start*
  pass — `OnStart(self)` runs once, during the start pass. `Process(self,
  delta)` then runs once per frame, with `delta` being the elapsed time in
  seconds.
- **Auto-registration.** You don't need to manually register `Mover` as a
  component type anywhere. The first time it's used with
  `get_component()`/`add_component()`/`has_component()` (including the
  `Mover(...)` you attach in the editor), the engine registers it against
  its `res://` file path automatically.
- **Exports.** `speed = export(3.0)` is both a normal Python class attribute
  *and* an inspector field — see
  [Exporting properties](scripting-guide.md#exporting-properties-to-the-inspector)
  for the full set of export widgets.

From here, the [Scripting Guide](scripting-guide.md) covers components,
physics, input, and (if you've enabled it) the RL agent API in detail.