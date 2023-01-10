#!/bin/bash

DEFAULT_MAJOR_MINOR_VERSION=0.0
DEFAULT_BUILD_VERSION=0

CURRENT_VERSION_REPO=$(cat version.txt 2> /dev/null)
if [ $? -ne 0 ]; then
    echo "File 'version.txt' not found."
fi

## Getting version info from branch
# RegEx to identify major and minor version from the version file.
re="([0-9]+\.[0-9]+).*"
if [[ $CURRENT_VERSION_REPO =~ $re ]]; then
    MAJOR_MINOR_VERSION=${BASH_REMATCH[1]}
else
    MAJOR_MINOR_VERSION=${DEFAULT_MAJOR_MINOR_VERSION}
fi
echo "Current major and minor version: ${MAJOR_MINOR_VERSION}"

## Getting version info from Git Tag
HASH=$(git rev-parse HEAD)
version_git_tag=$(git describe --match ${MAJOR_MINOR_VERSION}.* 2> /dev/null)
if [ $? -eq 0 ]; then
    echo "Version found in Git: ${version_git_tag}"
    re="[0-9]+\.[0-9]+\.([0-9]+)"
    [[ $version_git_tag =~ $re ]]
    build=$((BASH_REMATCH[1]+1))
    VERSION=${MAJOR_MINOR_VERSION}.${build}
else
    echo "Major and minor version not found in Git. Creating new version tag..."
    VERSION=${MAJOR_MINOR_VERSION}.${DEFAULT_BUILD_VERSION}
fi
echo "Setting version to ${VERSION} with hash ${HASH}"

curl --data '{"tag_name": "${VERSION}",
                "target_commitish": "master",
                "name": "${VERSION}",
                "body": "Release of version ${VERSION}",
                "draft": false,
                "prerelease": false}' \
    --request POST \
    https://api.github.com/repos/${{ github.repository }}/releases?access_token=$BOT_TOKEN