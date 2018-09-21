# coding=utf-8
from __future__ import absolute_import
from subprocess import check_output
from subprocess import call
from octoprint.settings import settings, valid_boolean_trues
import octoprint.plugin
import os

class GitfilesPlugin(octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin,
										 octoprint.plugin.SimpleApiPlugin,
                     octoprint.plugin.TemplatePlugin):

	def get_settings_defaults(self):
		return dict(url="https://github.com/YourGithubUsername/YourRepository.git",initialized=False)

	def get_template_vars(self):
		return dict(url=self._settings.get(["url"]))

	def get_template_configs(self):
		return [dict(type="settings", custom_bindings=False)]

	def get_assets(self):
		return dict(
			js=["js/gitfiles.js"],
			css=["css/gitfiles.css"],
			less=["less/gitfiles.less"]
		)

	def get_api_commands(self):
		return dict(
			git=["arg1"]
		)

	def on_api_command(self, command, data):
		import flask
		if command == "git":
			if self._settings.get(["url"]) == "https://github.com/YourGithubUsername/YourRepository.git":
				self._logger.info("Problem with setup. Please visit Settings -> GitFiles and adjust the URL")
				return

			self._logger.info("`git {arg1}`".format(**data))
			uploads = self._settings.global_get_basefolder("uploads")
			head, tail = os.path.split(uploads)
			gitfilesFolder = head + "/gitfiles"
			self._logger.info(gitfilesFolder)
			if not self._settings.get(["initialized"]):
				self._logger.info("Not initialized")
				# These run if it's not been initialized before this
				try:
					self._logger.info("Creating the gitfiles folder...")
					os.mkdir(gitfilesFolder, 0755)
					self._logger.info("Created gitfiles folder")
				except OSError as e:
					self._logger.info("gitfiles folder creation failed")
				try:
					self._logger.info("Initializing the uploads folder...")
					output =  call(["git", "init"], cwd=gitfilesFolder)
					self._logger.info(output)
					self._settings.setBoolean(["plugins", "gitfiles", "initialized"], True)
					self._settings.save()
				except OSError as e:
					self._logger.info("git init failed")
				try:
					self._logger.info("Setting up the remote origin for master...")
					output =  call(["git", "remote", "add", "origin", self._settings.get(["url"])], cwd=gitfilesFolder)
					self._logger.info(output)
				except OSError as e:
					self._logger.info("git add remote origin failed")
				try:
					self._logger.info("Creating the symlink...")
					os.symlink(gitfilesFolder, uploads + "/github")
					self._logger.info("Created symlink")
				except OSError as e:
					self._logger.info("Creation of symlink failed")
			# This one runs regardless of whether or not it's been previously initialized
			try:
				self._logger.info("-- git pull origin master ---------------------------------------------------")
				output =  call(["git", "pull", "origin", "master"], cwd=gitfilesFolder)
				self._logger.info("git returned: " + str(output))
				self._logger.info("-- (end of git pull) --------------------------------------------------------")
			except OSError as e:
				self._logger.info("git pull failed")

	def get_update_information(self):
		return dict(
			gitfiles=dict(
				displayName="Gitfiles Plugin",
				displayVersion=self._plugin_version,
				type="github_release",
				user="OutsourcedGuru",
				repo="OctoPrint-GitFiles",
				current=self._plugin_version,
				pip="https://github.com/OutsourcedGuru/OctoPrint-GitFiles/archive/{target_version}.zip"
			)
		)

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = GitfilesPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}
