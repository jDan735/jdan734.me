#!/bin/sh
# author: Kacper Kasper <kacperkasper@gmail.com>
# adapted from Haiku's build system
# usage: build.sh <arch>

repositoryDir=$1
repoInfo="jdan734.info"

packageDir="$repositoryDir/packages"
#mkdir -p "$packageDir"

#packageListFile="$repositoryDir/package.links"
#packageList=""
#echo "<table>" > $packageListFile
#for packageFile in "$packageDir"/*.hpkg; do
#	packageList="$packageList $packageFile"
#	packageFileNoDir=`package info -f "%fileName%" "$packageFile"`
#	packageName=`package info -f "%name%" "$packageFile"`
#	packageVersion=`package info -f "%version%" "$packageFile"`
#	echo "<tr><td><a href=\"packages/$packageFileNoDir\">$packageName</a></td><td>$packageVersion</td></tr>" >> $packageListFile
#done
#echo "</table>" >> $packageListFile

#indexHtml="$repositoryDir/index.html"
#indexTemplate="$repositoryDir/index.tmpl.html"
#cp -f $indexTemplate $indexHtml
#sed "/TABLEHERE/ {
#	r $packageListFile
#	d
# }" $indexTemplate > $indexHtml
#rm $packageListFile

#echo "build the repo file"
# build the repository file
#package_repo create "$repositoryDir/repo.info" "$packageDir"/*.hpkg

# create the checksum file
sha256sum "x86_gcc2/" sed -r 's,([^[:space:]]*).*,\1,' > "$repositoryDir/jdan734.sha256"
		# The sed part is only necessary for sha256sum, but it doesn't harm for
		# sha256 either.
