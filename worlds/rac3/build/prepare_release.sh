#!/bin/bash

SCRIPT_DIR=$(cd `dirname $0` && pwd)
cd $SCRIPT_DIR
mkdir -p ./rac3/images/maps
mkdir -p ./rac3/maps
mkdir -p ./rac3/locations
cp -r ./rac3-ap-poptracker/maps ./rac3/
cp -r ./rac3-ap-poptracker/images/maps ./rac3/images/
cp -r ./rac3-ap-poptracker/locations ./rac3/
zip -qo -r ./rac3.apworld ./rac3

OUTPUT=rac3jp_ap
rm -rf $OUTPUT $OUTPUT.zip
mkdir -p $OUTPUT
cp -f ./rac3.apworld ${OUTPUT}
zip -r ./rac3-ap-poptracker{.zip,}
mv rac3-ap-poptracker.zip $OUTPUT
zip -r $OUTPUT{.zip,}

rm -rf ./rac3/maps
rm -rf ./rac3/images/
rm -rf ./rac3/locations
