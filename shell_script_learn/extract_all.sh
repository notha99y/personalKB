#! /bin/bash
zip_files=`ls`
for zip_file in $zip_files
do
    if [[ "$zip_file"=*.zip.* ]];
    then
        echo "Extracting $zip_file"
        7z x $zip_file
    fi
done