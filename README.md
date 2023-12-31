![Rehopper Icon](assets/rehopper_icon_200x200.png)
# Rehopper v1.1.0
###### A Grasshopper plugin to reload canvas.

[![Build_CI](https://github.com/NoDoubtsKleve/rehopper/actions/workflows/build_ci.yml/badge.svg)](https://github.com/NoDoubtsKleve/rehopper/actions/workflows/build_ci.yml)
[![release)](https://img.shields.io/github/v/release/NoDoubtsKleve/rehopper?include_prereleases)](https://github.com/NoDoubtsKleve/rehopper/releases/latest)
[![License](https://img.shields.io/github/license/NoDoubtsKleve/rehopper)](https://github.com/NoDoubtsKleve/rehopper/blob/main/LICENSE)

## 🚀 Features

* Utility tool for Grasshopper-Python `.ghpy` plugin development.
* Caches all currently open (and saved) Grasshopper (`.gh` / `.ghx`) files.
* Unloads `Grasshopper.dll` from Rhino.
* Reloads `Grasshopper.dll` and restores files from cache.
* Provides a fancy button on the `CanvasToolbar`.

![Rehopper in Action - Win](assets/rehopper_in_action.gif)

![Rehopper in Action - Mac](assets/rehopper_in_action_mac.gif)
## 📦 Get Rehopper

Download the latest version from the [Yak PackageManager](https://developer.rhino3d.com/guides/yak/what-is-yak/) or from the [releases](https://github.com/NoDoubtsKleve/rehopper/releases/latest) page.
> Paste Command in your Rhino Console
```shell
_-PackageManager Search Rehopper
```

![Rehopper from Package Manager](assets/rehopper_package_manager.png)

## 🕹️ Basic Usage

![Rehopper Toolbar Button](assets/rehopper_toolbar_button.png)

## 🎛️ Advanced Usage

1. Download the [reload_grasshopper.py](src/reload_grasshopper.py) file, and add it to the `scripts` folder
   
    ```shell
    %AppData%\McNeel\Rhinoceros\7.0\scripts
    ``` 

2. Use the following command to reload grasshopper assemblies.

    ```shell
    _-RunPythonScript "reload_grasshopper.py"
    ```

3. [Create a toolbar button](https://docs.mcneel.com/rhino/5/help/en-us/toolbarsandmenus/toolbar_button_editor.htm), and save this Command.

## ❌ Limitations
Users cannot cherry-pick modules / plugins to ignore while reloading.
## 🌱 License
The scripts and documentation in this project are released under the MIT License
