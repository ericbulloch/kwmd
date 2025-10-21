#!/bin/bash

# Script that will release a site that has been uploaded to the current directory as react_new.zip.

echo "Checking if the zip file is on the server"
if [ ! -f react_new.zip ]; then
    echo "This is odd"
    printf "\033[0;31mreact_new.zip not found. Aborting.\n\033[0m";
    exit;
fi
echo "Done checking if the zip file is on the server"
echo "Unzipping the file"
unzip react_new.zip
echo "Done unzipping the file"
echo "Creating site_new folder"
mv build site_new
echo "Done creating site_new folder"
echo "Removing the site_new folder in /var/www/html"
sudo rm -rf /var/www/html/site_new
echo "Done removing the site_new folder in /var/www/html"
echo "Moving site_new folder to /var/www/html"
sudo mv site_new /var/www/html/
echo "Done moving site_new folder to /var/www/html"
rm react_new.zip
echo "Changing directory to /var/www/html"
cd /var/www/html
echo "Done changing directory to /var/www/html"
echo "Removing the site_old folder in /var/www/html"
sudo rm -rf /var/www/html/site_old
echo "Done removing the site_old folder in /var/www/html"
echo "Backing up the old site"
sudo mv site site_old
echo "Done backing up the old site"
echo "Making the new site live"
sudo mv site_new site
echo "Done making the new site live"
