# blender-export-ply-sequence
Blender Add-on to export a sequence of .ply files


-------------------------------- HOW TO RUN ------------------------------------

!!! MAKE SURE YOU HAVE THE Import-Export: Stanford PLY format enabled !!!

Blender -> Edit -> Preferences -> Add-ons -> Install
After clicking Install, select the "export_ply_animation.py" file and then click
Install Add-on.

Stay in the Add-ons tab and after installation is completed, type "Export
multiple frames as .ply files" in the search box and find this name
in the list below. Now make sure that it is checked (enabled), if it isn't click
the empty box on the left side of the name to enable it, otherwise you won't be
able to access the Add-on.

Now that the Add-on is installed and enabled, you can use it in Blender.

The Add-on is going to export the frames that are between Start and End in the
timeline, so make sure that the sequence you want to export is in the
[Start, End].

After you have correctly selected the interval to be exported, press F3. This
should bring up a search tab. In the search tab type and look for "Export
multiple frames as PLY files - Ridu" and click it.

Blender will get stuck for some time while executing the code, butt fear not.
After it's done processing, the Add-on is going to create a folder called
"PLY_Animation_frames". It will be created in the same folder as the .blende
file of your project. You should be able to find all the exported frames in the
newly created folder.

Pwp, enjoy.
