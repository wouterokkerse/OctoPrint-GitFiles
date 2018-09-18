# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin

class GitfilesPlugin(octoprint.plugin.SettingsPlugin,
                     octoprint.plugin.AssetPlugin,
                     octoprint.plugin.TemplatePlugin):

	def get_settings_defaults(self):
		return dict(url="https://github.com/YourGithubUsername/YourRepository.git")

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
