# OctoPrint-GitFiles

With this plugin, you can use a github repository for keeping your OctoPrint Files collection up-to-date. Publish your sliced files from a local repository on your workstation, then select to pull the latest from this github repository.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OutsourcedGuru/OctoPrint-GitFiles/archive/master.zip

To prepare for this, you'll need a public github repository which stores a `master` branch of your latest sliced files. You'll need its URL to put this in the Settings area of the plugin.

It's important not to use spaces in your GCODE filenames since OctoPrint will normally rename them in place (using underscores). This will likely cause problems which can easily be avoided if you not use spaces.

## Configuration

When you first install the plugin, it will be necessary to add your repository's URL into the Settings interface.

![github repository creation](https://user-images.githubusercontent.com/15971213/45719691-396fa600-bb56-11e8-9e71-d0d51c58ce4a.png)

![settings](https://user-images.githubusercontent.com/15971213/45835939-45777700-bcc0-11e8-80c6-2bc31e08f3ec.png)

![button](https://user-images.githubusercontent.com/15971213/45836320-5c6a9900-bcc1-11e8-92eb-3b0b20292e54.png)

## Possible Complications

If you use this plugin and you also use OctoPrint's interface to upload files, you must be careful not to upload files into the `github` subfolder. This would cause merge problems when you next pull from your repository.

Upon upload, OctoPrint will rename files, replacing spaces with underscores. If you've included space characters in your GCODE files they will be renamed-in-place which will then cause problems during the next pull. (Don't use spaces in your repository's filenames.)

## Failure to Edit Settings -> URL
If you don't adjust the Settings -> GitFiles -> URL from the default, you should see something like this in the `octoprint.log` file:

```
2018-09-20 11:52:39,136 - octoprint.plugins.gitfiles - INFO - Problem with setup. Please visit Settings -> GitFiles and adjust the URL
```

## Successfully Initialization
If everything worked, you should see something like this in the `octoprint.log` file:

```
2018-09-20 11:55:06,253 - octoprint.plugins.gitfiles - INFO - `git pull`
2018-09-20 11:55:06,258 - octoprint.plugins.gitfiles - INFO - /home/pi/.octoprint/uploads/github
2018-09-20 11:55:06,262 - octoprint.plugins.gitfiles - INFO - Not initialized
2018-09-20 11:55:06,263 - octoprint.plugins.gitfiles - INFO - Creating the gitfiles folder...
2018-09-20 11:55:06,311 - octoprint.plugins.gitfiles - INFO - 0
2018-09-20 11:55:06,314 - octoprint.plugins.gitfiles - INFO - Initializing the uploads folder...
2018-09-20 11:55:06,489 - octoprint.plugins.gitfiles - INFO - 0
2018-09-20 11:55:08,226 - octoprint.plugins.gitfiles - INFO - Setting up the remote origin for master...
2018-09-20 11:55:08,291 - octoprint.plugins.gitfiles - INFO - 0
2018-09-20 11:55:08,294 - octoprint.plugins.gitfiles - INFO - Creating the symlink...
2018-09-20 11:55:08,346 - octoprint.plugins.gitfiles - INFO - 0
2018-09-20 11:55:08,348 - octoprint.plugins.gitfiles - INFO - -- git pull origin master ---------------------------------------------------
2018-09-20 11:55:11,104 - octoprint.plugins.gitfiles - INFO - git returned: 0
2018-09-20 11:55:11,106 - octoprint.plugins.gitfiles - INFO - -- (end of git pull) --------------------------------------------------------
```

|Description|Version|Author|Last Update|
|:---|:---|:---|:---|
|OctoPrint-GitFiles|v1.1.2|OutsourcedGuru|October 1, 2018|

|Donate||Cryptocurrency|
|:-----:|---|:--------:|
| ![eth-receive](https://user-images.githubusercontent.com/15971213/40564950-932d4d10-601f-11e8-90f0-459f8b32f01c.png) || ![btc-receive](https://user-images.githubusercontent.com/15971213/40564971-a2826002-601f-11e8-8d5e-eeb35ab53300.png) |
|Ethereum||Bitcoin|