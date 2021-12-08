##Shading Kit Manual

---
### 1. Shading Tab 

![shading_tab](https://user-images.githubusercontent.com/87680516/145152365-03e64384-db43-4bfc-936b-351332928623.png)

---
### 2. Settings Tab

![settings_tab](https://user-images.githubusercontent.com/87680516/145152364-6c84732d-f3fb-4c05-aaa4-8911bc1ddb05.png)

---
### 3. Map/Utility Selections

>A. (**Left** Click) Select / Deselect all the maps
> 
>B. (**Right** Click) Select / Deselect all the utilities
> 
>C. (**Right** Click) Select / Deselect all utilities for current map

![Select_deselect_all_maps](https://user-images.githubusercontent.com/87680516/145152357-038d0990-7696-49c7-b288-ce9f92514fac.gif)
![select_deselect_all_utilities](https://user-images.githubusercontent.com/87680516/145152360-efa7a155-229c-4ce1-81c4-db005004173f.gif)
![Select_specific_utilities](https://user-images.githubusercontent.com/87680516/145152362-8647c4b7-ddbc-4b5f-a88e-5e30f220bfc9.gif)

---
### 4. AOV Options
    
> Expand / Shrink AOV options

> **All** = Select all
>
> **None** = Deselect all
> 
>**Match** = Match selection from maps
 

![Expand_shrink](https://user-images.githubusercontent.com/87680516/145152355-5a62efc0-64e7-4f74-8bf1-1ada0fc446ad.gif)
![Create_AOVs](https://user-images.githubusercontent.com/87680516/145152348-844053fd-6480-47f3-b235-b3263a254c9d.gif)
---
### 5. Create Shading Network

> Creates Shading Network with the given name. If empty, it uses the default name.
> 
> Not that:
>> A. **BaseColor** weight is set to **1.0**
> >
> >B. **Displacement** mid point is set to **0.5**
> >
> >C. **All file** nodes share the same **place2dtexture** node.

![Create_shading_network](https://user-images.githubusercontent.com/87680516/145152351-909234de-24dd-4bda-86eb-467f39b401d3.gif)

---
### 6. Auto texture assignment

> > Automatically assign textures from given directory.
>
> > **Right** Click on the folder icon to open the file format window.
> >
> >Select the formats you want to script to take into account.
>
> > Enable the `Use Directory` button.
> 
> >The script will iterate through each file in the given directory and if it finds any [Aliases](MANUAL.md#8-file-name-aliases) on the filename, it will load the corresponding file.


![use_directory](https://user-images.githubusercontent.com/87680516/145152367-0bc687f4-aaaa-4bee-85d2-00df9a72a64a.png)
![file_formats](https://user-images.githubusercontent.com/87680516/145152356-12b3365e-58f5-4cf6-a2a4-585661b0215f.gif)

---
### 7. Delete Shading Network

> If exists, deletes the Shader with the given name, otherwise it shows a window to select which shader to delete (could be more than one)
 
![Delete_shading_network](https://user-images.githubusercontent.com/87680516/145152352-24802aad-f949-455c-8a09-2c6ccb51a03c.gif)

---
### 8. File name Aliases

>Base Color
>>`basecolor`, `diffuse`, `albedo`, `base_color`, `base color`
> 
>Specular Roughness
>>`spec`, `roughness`
> 
>Metalness
>>`metal`, `metalness`, `metallic`
> 
>Displacement
>>`height`, `displace`
> 
>Normal
>>`normal`, `bump`
> 
>Coat Roughness
>>`coat`
> 
>Sub-surface scattering
>>`sss`, `subsurface`
> 
>Transmission
>>`transmission`, `transmissionweight`, `transmission_weight`, `transmission weight`
> 
>Opacity
>>`opacity`
#
>Example:
> 
> `woodenTable_diffuse.1001.exr`
> 
> Since `diffuse` is in the file name and it's an alias for **Base Color**, it will connect that file into the base color of the shader.

 