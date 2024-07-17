from PIL import Image
import os, platform

def erase():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")
    #end if
#end def

def getMaxItems(folder_path: str, ext: str) -> int:
    count = 0
    
    for item in os.listdir(folder_path):
        if item.endswith(ext):
            count += 1
        #end if
    #end for
    
    return count
#end def

# Folder with the images
folder_path = "kivymd-icons-white"

# Vars for iteration
damaged_files = []
ct, damaged = 0, 0
count = getMaxItems(folder_path, ".png")

# Iterate the folder and check if the files are damaged
for filename in os.listdir(folder_path):
    if filename.endswith(".png"):
        filepath = os.path.join(folder_path, filename)
        
        try:
            # Convert image in RGBA
            image = Image.open(filepath).convert('RGBA')
            image_data = image.getdata()
            
            # Process image pixels
            new_image_data = []
            for item in image_data:
                # Don't modify anything
                new_image_data.append(item)
            #end for
            
            # Save the modify image
            image.putdata(new_image_data)
            image.save(filepath)
        except:
            damaged_files.append(filepath)
            damaged += 1
        #end try
        
        # Show a counter
        erase()
        print(f"Checked files ({ct} / {count})")
        print(f"Damaged files: {damaged}")
        print(f"{round((ct / count) * 100, 2)}% / 100.00%")
        ct += 1
    #end if
#end for

erase()
print("Files checked successfully!")
print(f"Damaged files: {damaged}")

if damaged > 0:
    print("Location of damaged files: \n")
    
    for index, item in enumerate(damaged_files):
        print(f"{index + 1} >> {item}")
    #end for
#end if