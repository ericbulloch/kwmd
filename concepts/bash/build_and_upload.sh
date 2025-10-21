#!/bin/bash

# Script to build a react site and then upload to a server. The release.sh script gets run to release the site.
# The release script can be found at https://github.com/ericbulloch/kwmd/concepts/bash/release.sh
# This script is meant to be ran in the root directory of the React project.

echo "Building the site"
npm run build
echo "Done building the site"
echo "Zipping up the site"
zip -r build.zip build
echo "Done zipping up the site"
echo "Copying the site to the server"
scp build.zip my_username@server_address_goes_here:/home/user/react_new.zip
echo "Done copying the site to the server"
echo "Pushing the site"
ssh my_username@server_address_goes_here "bash -s" < ./release.sh
echo "Done pushing the site"
