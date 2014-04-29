var $ = django.jQuery;

$(document).ready(function() {
    tinymce.init({
        selector: 'textarea',
//        height : 600,
        content_css : '/static/css/admin.css',
        plugins: 'code'
    });
});