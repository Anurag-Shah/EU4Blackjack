import os
from wand import image
import numpy as np

target_width = 110
target_height = 166
part_width = 20
top_padding = 20

dir = "cards"
files = [f for f in os.listdir(os.path.join(dir, "input")) if os.path.isfile(os.path.join(dir, "input", f))]

padding_fill = np.zeros((top_padding, target_width, 4), dtype='uint8')

gfx_text = "spriteTypes = {"

for file in files:
    with image.Image(filename=os.path.join(dir, "input", file)) as img:
        clear_name = file.replace("_of", "").replace(".png", "")
        img.compression = 'no'
        
        if img.width != target_width or img.height != target_height:
            img.resize(target_width, target_height)

        # add padding at top for better matching with lines
        if np.array(img).shape[2] != 4:
            # No alpha channel, add
            img_with_alpha = np.concatenate((np.array(img), np.ones((target_height, target_width, 1), dtype='uint8') * 255), axis=2)
            img = image.Image.from_array(img_with_alpha)
            img.compression = 'no'

        padded_img_data = np.concatenate((padding_fill, np.array(img)))
        img = image.Image.from_array(padded_img_data)
        img.compression = 'no'

        img.save(filename=os.path.join(dir, "output", "icon_" + clear_name + ".dds"))

        gfx_text += "\n\tspriteType = {\n"\
                    f"\t\tname = \"GFX_icon_{clear_name}\"\n"\
                    f"\t\ttexturefile = \"gfx//interface//icon_{clear_name}.dds\"\n"\
                    "\t\tloadType = \"INGAME\"\n"\
                    "\t}\n"

        img.crop(0, 0, part_width, target_height + top_padding)
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
