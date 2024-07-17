#!/bin/bash

# Location of the svg files
input_dir="/storage/emulated/0/GitHub/Repos/Dsyutil-lib/materialdesignicons-webfont"

# Location of the new png files
output_dir="/storage/emulated/0/GitHub/Repos/Dsyutil-lib/kivymd_icons"

# make directory
mkdir -p "$output_dir"

# Search for .svg files in the input folder
for svg_file in "$input_dir"/*.svg; do
    # Get basename of the .svg file
    filename=$(basename "$svg_file" .svg)

    # Using InkScape for the conversion to PNG
    inkscape --export-type=png --export-width=256 --export-height=256 --export-filename="$output_dir/$filename.png" "$svg_file"

    echo "Converted: $svg_file -> $output_dir/$filename.png"
done

echo "Process completed successfully."