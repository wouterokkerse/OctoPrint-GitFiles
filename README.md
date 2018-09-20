# OctoPrint-GitFiles

With this plugin, you can use a github repository for keeping your OctoPrint Files collection up-to-date. Publish your sliced files from a local repository on your workstation, then select to pull the latest from this github repository.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OutsourcedGuru/OctoPrint-GitFiles/archive/master.zip

To prepare for this, you'll need a public github repository which stores a `master` branch of your latest sliced files. You'll need its URL to put this in the Settings area of the plugin.

## Configuration

When you first install the plugin, it will be necessary to add your repository's URL into the Settings interface.

![github repository creation](https://user-images.githubusercontent.com/15971213/45719691-396fa600-bb56-11e8-9e71-d0d51c58ce4a.png)

![settings](https://user-images.githubusercontent.com/15971213/45835939-45777700-bcc0-11e8-80c6-2bc31e08f3ec.png)

![button](https://user-images.githubusercontent.com/15971213/45836320-5c6a9900-bcc1-11e8-92eb-3b0b20292e54.png)

## Possible Complications

If you use this plugin and you also use OctoPrint's interface to upload files, you must be careful not to upload files into the `github` subfolder. This would cause merge problems when you next pull from your repository.

|Description|Version|Author|Last Update|
|:---|:---|:---|:---|
|OctoPrint-GitFiles|v1.0.1|OutsourcedGuru|September 20, 2018|

|Donate||Cryptocurrency|
|:-----:|---|:--------:|
| ![eth-receive](https://user-images.githubusercontent.com/15971213/40564950-932d4d10-601f-11e8-90f0-459f8b32f01c.png) || ![btc-receive](https://user-images.githubusercontent.com/15971213/40564971-a2826002-601f-11e8-8d5e-eeb35ab53300.png) |
|Ethereum||Bitcoin|