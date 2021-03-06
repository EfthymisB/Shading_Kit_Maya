# Shading Kit Manual

---
## 1. Shading Tab


![settings_tab2](https://user-images.githubusercontent.com/87680516/145273788-4e21b5cb-4054-4dbf-aeef-0d71ba758ac1.png)

---
## 2. Settings Tab

![settings_tab](https://user-images.githubusercontent.com/87680516/145152364-6c84732d-f3fb-4c05-aaa4-8911bc1ddb05.png)

---
## 3. Map/Utility Selections

>A. (**Left** Click) Select / Deselect all the maps
> 
>B. (**Right** Click) Select / Deselect all the utilities
> 
>C. (**Right** Click) Select / Deselect all utilities for current map

![Select_deselect_all_maps](https://user-images.githubusercontent.com/87680516/145152357-038d0990-7696-49c7-b288-ce9f92514fac.gif)
![select_deselect_all_utilities](https://user-images.githubusercontent.com/87680516/145152360-efa7a155-229c-4ce1-81c4-db005004173f.gif)
![Select_specific_utilities](https://user-images.githubusercontent.com/87680516/145152362-8647c4b7-ddbc-4b5f-a88e-5e30f220bfc9.gif)

---
## 4. AOV Options

> Expand / Shrink AOV options

> **All** = Select all
>
> **None** = Deselect all
> 
>**Match** = Match selection from maps
 

![Expand_shrink](https://user-images.githubusercontent.com/87680516/145152355-5a62efc0-64e7-4f74-8bf1-1ada0fc446ad.gif)

> > 1. Select a shader
> 
> > 2. Highlight the AOVs you want
> 
> > 3. Press `Create`
>
> It will create an AOV per layer, rendering the RAW maps. **_(currently not working properly for Opacity)_**

![Create_AOVs](https://user-images.githubusercontent.com/87680516/145152348-844053fd-6480-47f3-b235-b3263a254c9d.gif)

---
## 5. Create Shading Network


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
## 6. Auto texture assignment

> > Automatically assign textures from given directory.
>
> > **Right** Click on the folder icon to open the file format window.
> >
> >Select the formats you want to script to take into account.
>
> > Enable the `Use Directory` button.
> 
> >The script will iterate through each file in the given directory and if it finds any Aliases _(see section 8)_ on the filename, it will load the corresponding file.


![use_directory](https://user-images.githubusercontent.com/87680516/145152367-0bc687f4-aaaa-4bee-85d2-00df9a72a64a.png)
![file_formats](https://user-images.githubusercontent.com/87680516/145152356-12b3365e-58f5-4cf6-a2a4-585661b0215f.gif)
![Rb8cBdIXHu](https://user-images.githubusercontent.com/87680516/145270338-ff19c78d-e350-4e4b-bc17-0d3438529f4f.gif)

---
## 7. Delete Shading Network

> If exists, deletes the Shader (_the entire network_) with the given name, otherwise it shows a window to select which shader(s) to delete.
 
![Delete_shading_network](https://user-images.githubusercontent.com/87680516/145152352-24802aad-f949-455c-8a09-2c6ccb51a03c.gif)

---
## 8. File-name Aliases

 Below you can see the default aliases. You can always add/remove aliases by editing the `user_settings` file. There is also `Reset settings` option.

![aliases](https://user-images.githubusercontent.com/87680516/145581954-e2e018c0-ae19-43ab-ba11-2b91bee82041.png)

>Example:
> 
> `woodenTable_diffuse.1001.exr`
> 
> The String `diffuse` (which is set as an alias for the `Base Color` layer) is in the file name, therefore this file will be loaded in a file node the then connected to the `Base color` input of the shader.

### Table with the Aliases for every layer
| Base Color  | Sp. Roughness | Metalness | Displacement | Normal | Bump | Coat R. | SSS        | Opacity |
| ----------- | ------------- | --------- | ------------ | ------ | ---- | ------- | ---------- | ------- |
| `albedo`    | `spec`        |`metal`    |`height`      |`normal`|`bump`|`coat`   |`sss`       |`opacity`|
| `base color`| `roughness`   |`metalness`|`displace`    |        |      |         |`subsurface`|         |
| `base_color`|               |`metallic` |              |        |      |         |            |         |
| `basecolor` |               |           |              |        |      |         |            |         |
| `diffuse`   |               |           |              |        |      |         |            |         |

---
## 9. Limitations


* Only Arnold and the `aiStandardSurface` shader are currently supported.
* `Opacity` layer AOV will not render properly.
* Save reminder sound effects are currently available **only** for `Windows`.

