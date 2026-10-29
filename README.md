# Fusion Engine Documentation

This is the repository for the documentation website of [Fusion Engine](https://github.com/DevPhusion/FusionEngine), a custom 2D game engine designed for building lightweight reinforcement learning (RL) training environments. The site contains the Python scripting API reference and guides for getting started, scripting, and RL training. It is built with MkDocs and the Material theme, and versioned with mike.

**Live site:** [https://devphusion.github.io/FusionEngineDocumentation/](https://devphusion.github.io/FusionEngineDocumentation/)

## Table of Contents

- [What's Covered](#whats-covered)
- [Repository Structure](#repository-structure)
- [Libraries](#libraries)
- [Building Locally](#building-locally)
- [API Reference](#api-reference)
- [Versioning Guide](#versioning-guide)
  - [Adding a New Docs Version](#adding-a-new-docs-version-eg-030)
  - [Rules to Remember](#rules-to-remember)
  - [Fixing an Already-Published Version](#fixing-an-already-published-version)
  - [Removing a Version](#removing-a-version)
- [Contributing](#contributing)
- [Contact](#contact)

## What's Covered

| Section | Description |
|---|---|
| Getting Started | Installing the engine and setting up a project. |
| Scripting Guide | Writing script components and using the Python API. |
| API Reference | Generated reference for the math types, `Object`, every component, physics, input, console, file, render, scene, export markers, and the `fusionRL` reinforcement learning API. |
| Design Document | Link to the engine's full design document. |

## Repository Structure

```
FusionEngineDocumentation/
├── .github/workflows/     # GitHub Actions for building and deploying the docs
├── docs/                  # Markdown content (guides, api/ pages, stubs/)
├── mkdocs.yml             # Site config, navigation, theme, and plugins
└── requirements-docs.txt  # Python dependencies for building the site
```

## Libraries

| Library | Purpose |
|---|---|
| [MkDocs](https://www.mkdocs.org/) | Static site generator. |
| [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) | Site theme, navigation, and search. |
| [mkdocstrings](https://mkdocstrings.github.io/) | Generates the API reference from the Python stub file. |
| [mike](https://github.com/jimporter/mike) | Manages multiple documentation versions. |

## Building Locally

Building the docs does not need the engine or Windows, only Python.

```
git clone https://github.com/DevPhusion/FusionEngineDocumentation.git
cd FusionEngineDocumentation
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-docs.txt
mkdocs serve
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000). Use `mkdocs build` to generate the static site into `site/`.

## API Reference

The API pages are generated from the engine's `.pyi` stub file (produced by `pybind-stubgen`), which lives in `docs/stubs/`. mkdocstrings reads it statically and never imports the compiled engine module, since that would need a live engine and OpenGL context. If something in the API reference is wrong or missing, update the stub file or its docstrings rather than the Markdown page.

## Versioning Guide

Each engine release has its own docs version, managed with mike and stored on the `gh-pages` branch. The `dev` version tracks `main`, and `latest` points at the newest release.

### Adding a New Docs Version (e.g. 0.3.0)

#### 1. Update the docs on `main`

- Update `docs/` Markdown to match the new engine version.
- Replace the stubs in `docs/stubs/` with the ones generated from the new build, since the API pages come from these.
- Fix any anchor or nav warnings.

```powershell
git add .
git commit -m "Update docs for v0.3.0"
git push
```

Pushing to `main` triggers the Action, which publishes `dev`. Check the **dev** version on the site first to confirm everything renders correctly.

#### 2. Publish the release version

**Option A: GitHub Actions (recommended)**

1. Go to **Actions → Deploy docs → Run workflow**.
2. Enter the version (e.g. `0.3.0`, no `v` prefix).
3. Leave "Make this version the default/latest" checked.
4. Run it.

**Option B: locally**

Run from `Documents` with the venv active:

```powershell
git fetch origin gh-pages
git branch -f gh-pages origin/gh-pages
mike deploy --push --update-aliases 0.3.0 latest
mike set-default --push latest
```

The `git branch -f` line matters. It syncs your local `gh-pages` with the remote, which avoids the "rejected (fetch first)" error caused by the Action's `dev` deploys.

#### 3. Verify

```powershell
mike list
```

Expected result:

```
0.3.0 [latest]
0.2.1
0.2
0.1
dev
```

Then check [versions.json](https://devphusion.github.io/FusionEngineDocumentation/versions.json), wait 1 to 3 minutes for the Pages build, and hard-refresh with **Ctrl+Shift+R**.

### Rules to Remember

| Do | Don't |
|---|---|
| Use `--update-aliases <version> latest` so `latest` moves to the new release | Pass `latest` when backfilling old versions |
| Use plain version numbers (`0.3.0`) | Use `mkdocs gh-deploy`, which wipes all versions |
| Sync local `gh-pages` before any local deploy | Force-push `gh-pages`, which deletes every published version |
| Keep the `extra.version` block in `mkdocs.yml` | Remove `mike` from `requirements-docs.txt` |

### Fixing an Already-Published Version

To correct a typo in a published version (say `0.2.1`), deploy it again with the same version number. Mike overwrites just that folder:

```powershell
mike deploy --push 0.2.1
```

To keep `latest` pointing at it, use `mike deploy --push --update-aliases 0.2.1 latest`.

### Removing a Version

```powershell
mike delete --push 0.1
```

## Contributing

Fixes and improvements to the docs are welcome. Fork the repo, edit the files in `docs/`, preview with `mkdocs serve`, and open a pull request. Engine bugs and feature requests belong in the [Fusion Engine repository](https://github.com/DevPhusion/FusionEngine/issues).

## Contact

- **Email:** devphusion@gmail.com
- **Discord:** devphusion
