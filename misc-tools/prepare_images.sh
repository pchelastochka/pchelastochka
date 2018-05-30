#!/bin/bash

prefix="../common-web/main"
fullsize_dir="$prefix/img/gallery"
full_width="720"
thumbs_dir="$prefix/img/gallery/thumbs"
thumb_width="100"
gallery_file="$(find $prefix/_posts/ -type f -iname '*gallery*')"

for png in $(find $fullsize_dir -maxdepth 1 -type f -iname '*.png' -printf "%f\n"); do
	convert -background white -flatten $fullsize_dir/"$png" $fullsize_dir/"$png.jpg"
	rm $fullsize_dir/"$png"
done

fullsize_images=$(find $fullsize_dir -maxdepth 1 -type f -iname '*.jpg' -printf "%f\n")

for img in $fullsize_images; do
    # edit width
    convert -resize $full_width $fullsize_dir/"$img" $fullsize_dir/"$img"
    # crop to 4:3
    convert -gravity center -crop 720x405+0+0 $fullsize_dir/"$img" $fullsize_dir/"$img"
done
echo "Images optimized"

find $thumbs_dir -type f -delete
for img in $fullsize_images; do
    convert -resize $thumb_width $fullsize_dir/"$img" $thumbs_dir/"$img"
done
echo "Thumbnails created"

images_list="[ $(paste -d, -s <<< "$fullsize_images") ]"
sed -i "s/images:.*/images: $images_list/" "$gallery_file"
echo "Post edited"
