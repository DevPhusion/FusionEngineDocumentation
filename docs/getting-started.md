# Getting Started

!!! note
    This page is hand-written — edit it directly in `docs/getting-started.md`.
    It won't be touched by the automatic stub regeneration.

## Installing the engine

1. Download the latest release from the [Releases page](https://github.com/DevPhusion/FusionEngine/releases).
2. Extract the archive and run `FusionApp.exe`.
3. Create a new project. Fusion sets up a Python virtual environment for you
   alongside your project's resources folder.

## Your first script

Right-click in the resource browser, choose **New Script**, and attach it to
an object. See the [Scripting Guide](scripting-guide.md) for how scripts,
components, and exports fit together.

## Editor autocomplete

Fusion automatically generates a `.pyi` stub file into your project's
`typings/` folder and configures VS Code to use it, so you get full
autocomplete for the engine API as you write scripts.
