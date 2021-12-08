## Shading_Kit_Maya
 Shading Kit for Maya by Efthymis B.

---

## Python2 - (**Maya 2018 / 2019 / 2020**)

>1. Download the [files](archive/refs/heads/main.zip).  
>2. Copy the folder `ShadingKit_python2` to `C:\Users\<UserName>\Documents\maya\scripts` or in your custom script directory.
>3. Create a shelf button and add the following code in the `Command/Python` tab:
>```
>try:
>   reload(runUI)
>except NameError:
>   from ShadingKit_python2 import runUI
> ```
> *(or copy the code in the Script Editor, highlight everything and then **Click, Drag and Drop** it in the shelf)*
---

## Python3 -  (**Maya 2022+**)

>1. Download the [files](archive/refs/heads/main.zip).
>2. Copy the folder `ShadingKit_python3` to `C:\Users\<UserName>\Documents\maya\scripts` or in your custom script directory.
>3. Create a shelf button and add the following code in the `Command/Python` tab:
>```
>import importlib
>try:
>   importlib.reload(runUI)
>except NameError:
>   from ShadingKit_python3 import runUI
> ```
> *(or copy the code in the Script Editor, highlight everything and then **Click, Drag and Drop** it in the shelf)*
---

Contact: **[efthymisb.vfx@gmail.com](mailto:efthymisb.vfx@gmail.com)**
