/*
 * View model for OctoPrint-GitFiles
 *
 * Author: OutsourcedGuru
 * License: MIT
 */

$(function() {
    function GitfilesViewModel(parameters) {
        var self = this;

        gitPull = function() {
            $.ajax({
                url:         "/api/plugin/gitfiles",
                type:        "POST",
                contentType: "application/json",
                dataType:    "json",
                headers:     {"X-Api-Key": UI_API_KEY},
                data:        JSON.stringify({"command": "git", "arg1": "pull"}),
                complete: function () {
                    var a = $("#files_wrapper").find("div").find(".refresh-trigger").find("a");
                    if (a.length) {
                        a.click();
                    }
                }
            });
        };

        self.onStartupComplete = function() {
            var element = $("div.gcode_files")
                        .find("div.scroll-wrapper > div.entry")
                        .find("div.internal > span")
                        .filter(function(){ return $(this).text() == 'gitfiles'; }) /* TODO: Make this able to note a changed subfolder */
                        .parent()
                        .siblings("div.btn-group.action-buttons")
                        .find("div.btn.btn-mini");
            if (element.length) {
                element.hide();
            }

        }

        self.onStartup = function() {
            var element = $("#files_wrapper").find("div").find(".refresh-trigger");
            if (element.length) {
                element.before("<div class=\"gitfiles-trigger accordian-heading-button btn-group\" " +
                    "data-bind=\"visible: $root.filesListVisible\"><a href=\"#\" " +
                    "data-bind=\"click: gitPull\" " +
                    "title=\"Get latest from github\"><i class=\"fa fa-github fa-2\"></i></a></div>");
            }
        };
    }

    OCTOPRINT_VIEWMODELS.push({construct: GitfilesViewModel, dependencies: ["printerStateViewModel"], elements: []});    
});
