# OctoPrint-GitFiles

With this plugin, you can use a github/gitlab repository for keeping your OctoPrint Files collection up-to-date. Publish your sliced files from a local repository on your workstation, then select to pull the latest from this remote repository.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/OutsourcedGuru/OctoPrint-GitFiles/archive/master.zip

To prepare for this, you'll need a public github/GitLab repository which stores a `master` branch of your latest sliced files. You'll need its URL to put this in the Settings area of the plugin.

It's important not to use spaces in your GCODE filenames since OctoPrint will normally rename them in place (using underscores). This will likely cause problems which can easily be avoided if you not use spaces.

## Configuration

When you first install the plugin, it will be necessary to add your repository's URL into the Settings interface.

![github repository creation](https://user-images.githubusercontent.com/15971213/45719691-396fa600-bb56-11e8-9e71-d0d51c58ce4a.png)

![settings](https://user-images.githubusercontent.com/15971213/49118353-c28f1180-f258-11e8-8c3a-612dad2ad2e1.png)

![button](https://user-images.githubusercontent.com/15971213/49118125-18af8500-f258-11e8-8e80-5eed2abf3dfa.png)

## Possible complications

If you use this plugin and you also use OctoPrint's interface to upload files, you must be careful not to upload files into the `gitfiles` or other indicated subfolder. This would cause merge problems when you next pull from your repository.

Upon upload, OctoPrint will rename files, replacing spaces with underscores. If you've included space characters in your GCODE files they will be renamed-in-place which will then cause problems during the next pull. (Don't use spaces in your repository's filenames.)

## Failure to edit settings -> URL
If you don't adjust the Settings -> GitFiles -> URL from the default, you should see something like this in the `octoprint.log` file:

```
2018-09-20 11:52:39,136 - octoprint.plugins.gitfiles - INFO - Problem with setup. Please visit Settings -> GitFiles and adjust the URL
```

## Successful initialization
If everything worked, you should see something like this in the `octoprint.log` file:

```
octoprint.plugins.gitfiles - INFO - Path: `/home/pi/.octoprint/uploads/gitfiles`
octoprint.plugins.gitfiles - INFO - Testing the indicated `/home/pi/.octoprint/uploads/gitfiles` folder...
octoprint.plugins.gitfiles - INFO - Indicated folder is not initialized yet
octoprint.plugins.gitfiles - INFO - Creating the new `/home/pi/.octoprint/uploads/gitfiles` subfolder...
octoprint.plugins.gitfiles - INFO - Created
octoprint.plugins.gitfiles - INFO - Initializing...
Initialized empty Git repository in /home/pi/.octoprint/uploads/gitfiles/.git/
octoprint.plugins.gitfiles - INFO - 0
octoprint.plugins.gitfiles - INFO - Setting up the remote origin for master...
octoprint.plugins.gitfiles - INFO - 0
octoprint.plugins.gitfiles - INFO - -- git pull origin master ---------------------------------------------------
remote: Enumerating objects: 17, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 17 (delta 2), reused 13 (delta 0), pack-reused 0
Unpacking objects: 100% (17/17), done.
From https://github.com/OutsourcedGuru/3d-files
 * branch            master     -> FETCH_HEAD
 * [new branch]      master     -> origin/master
octoprint.plugins.gitfiles - INFO - git returned: 0
octoprint.plugins.gitfiles - INFO - -- (end of git pull) --------------------------------------------------------
```

## Setup for private Github repository
Although I've not tested it directly with this plugin, there's a way of sending in your github/GitLab credentials as part of the URL in the plugin's Settings page.

```
https://YourGitHubID:YourPassword@github.com/YourGitHubID/3d-files.git
```

Prepend the hostname `github.com`, for example, with `YourUserID:YourPassword@` ensuring that your password doesn't *itself* contain either of the special symbols shown.

You can also use privately-hosted GitLab instances by replacing `github.com` with the hostname of your privately-hosted instance.

If you don't like the idea of your credentials being copied to OctoPrint's `config.yaml` then set it up normally in the Settings page. Next, it should be possible to then manually edit the `~/.octoprint/uploads/gitfiles/.git/config` or similar file under the `[remote origin]` section, adding the credentials as described above. In this way, your credentials will appear in the `config` file under a hidden `.git` directory rather than within OctoPrint's own configuration file.

## Setup using an SSH key for authentication

If you don't want to pass your credentials in your URL or to save them in your git `config`, you can use an SSH keypair for authenticating to your remote repository.

This requires that you generate an SSH keypair on your Raspberry Pi.  You'll want to remote into your Raspberry first with `ssh` and then issue the following command (after the $ sign below), accepting the defaults by pressing Enter each time:

```
pi@octopi:~ $ ssh-keygen -t rsa -C "pi@octopi"

Generating public/private rsa key pair.
Enter file in which to save the key (/home/pi/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/pi/.ssh/id_rsa.
Your public key has been saved in /home/pi/.ssh/id_rsa.pub.
```

Using the default settings should create the keys as `~/.ssh/id_rsa` (private key) and `~/.ssh/id_rsa.pub` (public key).  You need to open *id_rsa.pub* in a text editor and copy its contents.  *MAKE SURE YOU OPEN/COPY THE .PUB VERSION.*

In your github/GitLab account, go into your profile settings and open the section for SSH keys.  Click *New SSH Key* and paste in the contents of the public key you copied in the previous step.  This will allow you to authenticate using an SSH key yet not store your credentials anywhere.

![keys section](https://i.imgur.com/8E5hA83.png)

![new ssh key button](https://i.imgur.com/5gKul5A.png)

Once saved, you'll need to test this first on the Raspberry to accept the key.  Adjust the URL for SSH authentication, changing the protocol.  Instead of beginning with `https://host/`, you start the URL with `git@host:github.com:` and finishing with your case-sensitive ID and repository.

Example:
```
git@github.com:YourUserID/repo.git
```

So on the Raspberry, you'll want to do something like this to just test and accept the SSH key, (entering the commands after each $ sign):

```
pi@octopi:~ $ mkdir ~/tmp && cd ~/tmp
pi@octopi:~ $ git clone git@github.com:YourUserID/repo.git
Cloning into 'repo'...
The authenticity of host 'XXXX (X.X.X.X)' can't be established.
ECDSA key fingerprint is SHA256:1Pe176kN32iqaypIpAfQIwmEiUDFhwX3q/gI9J2+lPw.
Are you sure you want to continue connecting (yes/no)? yes
```

You must type yes to accept the key and to store it, so that later the plugin will be able to pull from your repository in the future.

After this is completed, you can simply configure the correct git@ URL in the plugin settings and you're ready to use SSH authentication.

Now that you've initially tested your keypair and you no longer need that temporary folder, you can remove it with (entering the commands after the $ sign):

```
pi@octopi:~ $ cd ~ && rm -rF tmp
```

---------------------------------------------

|Description|Version|Author|Last Update|
|:---|:---|:---|:---|
|OctoPrint-GitFiles|v1.1.4|OutsourcedGuru|November 27, 2018|

|Who|Role|
|:---|:---|
|OutsourcedGuru|Author|
|scottrini|Contributor - Docs & recent work with direct uploads functionality |

|Donate||Cryptocurrency|
|:-----:|---|:--------:|
| ![eth-receive](https://user-images.githubusercontent.com/15971213/40564950-932d4d10-601f-11e8-90f0-459f8b32f01c.png) || ![btc-receive](https://user-images.githubusercontent.com/15971213/40564971-a2826002-601f-11e8-8d5e-eeb35ab53300.png) |
|Ethereum||Bitcoin|