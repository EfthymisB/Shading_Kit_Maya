## Shading_Kit_Maya
 Shading Kit for Maya by Efthymis B.

---

## Python2:

>1. Download: `ShadkingKit_python2` (**Maya 2018 / 2019 / 2020**)
>2. Extract folder in `C:\Users\<UserName>\Documents\maya\scripts` or in your custom script directory.
>3. Create a shelf button and add the following in the `Command/Python` tab:
>```
>try:
>   reload(runUI)
>except NameError:
>   from ShadkingKit_python2 import runUI
> ```
> *(or copy the code in the Script Editor, highlight everything and **Click, Drag and Drop** it in the shelf)*
---

## Python3:

>1. Download: `ShadkingKit_python3` (**Maya 2022+**)
>2. Extract folder in `C:\Users\<UserName>\Documents\maya\scripts` or in your custom script directory.
>3. Create a shelf button and add the following in the `Command/Python` tab:
>```
>import importlib
>try:
>   importlib.reload(runUI)
>except NameError:
>   from ShadkingKit_python3 import runUI
> ```
> *(or copy the code in the Script Editor, highlight everything and **Click, Drag and Drop** it in the shelf)*
---

Contact: **[efthymisb.vfx@gmail.com]()**
