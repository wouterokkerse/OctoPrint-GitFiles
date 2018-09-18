# OctoPrint-GitFiles

With this plugin, you can use a github repository for keeping your OctoPrint Files collection up-to-date. Publish your sliced files from a local repository on your workstation, then select to pull the latest from this github repository.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OutsourcedGuru/OctoPrint-GitFiles/archive/master.zip

To prepare for this, you'll need a public github repository which stores a `master` branch of your latest sliced files. You'll need its URL to put this in the Settings area of the plugin.

## Configuration

When you first install the plugin, it will be necessary to add your repository's URL into the Settings interface. It's also a good idea to download & delete all of the existing files in your OctoPrint's Files area first so that you don't have do deal with merge-related issues.

## Possible Complications

If you use this plugin and you also use OctoPrint's interface to upload files, you must be careful about file naming and clashes which could occur as a result. If in doubt, delete the one you uploaded via the OctoPrint interface and then get the latest version from your repository.

|Description|Version|Author|Last Update|
|:---|:---|:---|:---|
|OctoPrint-GitFiles|v0.1.0|OutsourcedGuru|September 18, 2018|

|Donate||Cryptocurrency|
|:-----:|---|:--------:|
| ![eth-receive](https://user-images.githubusercontent.com/15971213/40564950-932d4d10-601f-11e8-90f0-459f8b32f01c.png) || ![btc-receive](https://user-images.githubusercontent.com/15971213/40564971-a2826002-601f-11e8-8d5e-eeb35ab53300.png) |
|Ethereum||Bitcoin|