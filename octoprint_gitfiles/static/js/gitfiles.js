/*
 * View model for OctoPrint-GitFiles
 *
 * Author: OutsourcedGuru
 * License: MIT
 */
$(function() {
    function GitfilesViewModel(parameters) {
        var self = this;

        self.onStartup = function() {
            console.log('gitfiles.onStartup()');
            var element = $("#files_wrapper").find("div").find(".refresh-trigger");
            if (element.length) {
                element.before("<div class=\"gitfiles-trigger accordian-heading-button btn-group\" data-bind=\"visible: $root.filesListVisible\"><a href=\"#\" data-bind=\"click: function() { alert(\'here\');}\" title=\"{{ _(\'Get latest from github\') }}\"><i class=\"fa fa-github fa-2\"></i></a></div>");
                //element.after("<div class='refresh-trigger accordian-heading-button btn-group' data-bind='visible: $root.filesListVisible'><a href='#' data-bind='click: function() { $root.requestData({force: true});}' title='Get latest from Github'><i class='fa fa-refresh'></i></a></div>");
            }
        };
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({construct: GitfilesViewModel, dependencies: [], elements: []});    
});
