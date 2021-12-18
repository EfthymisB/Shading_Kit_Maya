

# ![V1.2](https://img.shields.io/badge/Shading_Kit_for_Maya-V1.2-white)


## ![V1.2](https://img.shields.io/badge/New_Features-7aaf00)

- New `Bump` layer option.
- The entire Shading Network is being selected after creation.
- A new option `Use TX Textures` has been added in the `File formats menu`. When enabled, the `.tx` file will be loaded into the file node (if there is one)

![maya_iI4AuHaI9H](https://user-images.githubusercontent.com/87680516/146624775-7d7dc461-bba4-4381-a120-c775a2ea2ed9.png)

---
## ![V1.2](https://img.shields.io/badge/Changes-blue)
- Shader's name is now a suffix on every node.
- The file node of the `Normal` map is now being connected to an `aiNormalMap`
- If both `Normal` and `Bump` layers are enabled, the `aiBump2d` will connected to the `NormalCamera` of the shader and the `aiNormalMap` will be connected to the `Normal` input of the `aiBump2d`

![bump_and_normal](https://user-images.githubusercontent.com/87680516/146624738-44c1470b-42b7-41de-aa29-99d0de3c18f6.png)

- Updated licenses.
- Added Release Notes file.
- Added `About` tab with useful links.

---
## ![V1.2](https://img.shields.io/badge/Bug_Fixes-orange)

- Due to a bug, AOVs didn't work on the Python2 version. It is fixed now.

---
## ![V1.2](https://img.shields.io/badge/Removed-red)

- Transmission layer button has been removed.
- Transmission AOV button has been removed.

---
# ![V1.1](https://img.shields.io/badge/Shading_Kit_for_Maya-V1.1-white)

First version of Shading Kit for Maya
