import os
from wand import image

target_width = 40
target_height = 80
part_width = 20

dir = "cards"
files = [f for f in os.listdir(os.path.join(dir, "input")) if os.path.isfile(os.path.join(dir, "input", f))]

gfx_text = "spriteTypes = {"

for file in files:
    with image.Image(filename=os.path.join(dir, "input", file)) as img:
        clear_name = file.replace("_of", "").replace(".png", "")

        img.compression = 'no'

        if img.width != target_width or img.height != target_height:
            img.resize(target_width, target_height)

        img.save(filename=os.path.join(dir, "output", "icon_" + clear_name + ".dds"))

        gfx_text += "\n\tspriteType = {\n"\
                    f"\t\tname = \"GFX_icon_{clear_name}\"\n"\
                    f"\t\ttexturefile = \"gfx//interface//icon_{clear_name}.dds\"\n"\
                    "\t\tloadType = \"INGAME\"\n"\
                    "\t}\n"

        img.crop(0, 0, part_width, target_height)
        img.save(filename=os.path.join(dir, "output", "icon_" + clear_name + "_part.dds"))
        gfx_text += "\n\tspriteType = {\n"\
                    f"\t\tname = \"GFX_icon_{clear_name}_part\"\n"\
                    f"\t\ttexturefile = \"gfx//interface//icon_{clear_name}_part.dds\"\n"\
                    "\t\tloadType = \"INGAME\"\n"\
                    "\t}\n"


gfx_text += "}"
f = open(os.path.join(dir, "cards.gfx"), 'w', encoding="cp1252")
f.write(gfx_text)
f.close()
