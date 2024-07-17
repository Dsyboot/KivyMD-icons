from PIL import Image
import os, platform

def erase():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    #end if
#end def

def getMaxItems(folder: str, ext: str) -> int:
    count = 0

    # get max count of files with "-outline"
    for filename in os.listdir(folder):
        if filename.endswith(ext):
            count += 1
        #end if
    #end for
    
    return count
#end def

# Folder with the images
folder_path = "kivymd-icons-white"

# Iterate folder with the images
ct = 0
count = getMaxItems(folder_path, ".png")
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        filepath = os.path.join(folder_path, filename)
        
        # Convert image in RGBA
        image = Image.open(filepath).convert('RGBA')
        image_data = image.getdata()
        
        # Process pixels of image
        new_image_data = []
        for item in image_data:
            # Modify black pixels (RGB = 0,0,0) to white (RGB = 255,255,255)
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                new_image_data.append((255, 255, 255, item[3]))  # Keep transparency
            else:
                new_image_data.append(item)
            #end if
        #end for
        
        # Save the modified image
        image.putdata(new_image_data)
        image.save(filepath)
        
        # Show a counter
        erase()
        print(f"Modifying and painting files ({ct} / {count})")
        print(f"{round((ct / count) * 100, 2)}% / 100.00%")
        ct += 1
    #end if
#end for

erase()
print("Files painted and modified successfully!")