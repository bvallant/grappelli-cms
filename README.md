Grappelli CMS
=============

This is a fork of [divio's]((http://github.com/divio/django-cms/) [django-cms](http://www.django-cms.org) to be used with [django-grappelli](http://code.google.com/p/django-grappelli/). This is a first basically working version, in some parts a bit hacky...

The main issues were:

* adjusting the CMS' HTML admin templates to grappelli's template structure, mainly renaming css classes
* modifying the admin CSS files to fit the grappelli's color scheme
* making all the javascript's work - using the jquery file provided by grappelli with its name space
* furthermore I added some fields I considered useful to the included plugins

I'm no heavy user of the CMS' extended permission and moderation features, so there might be some issues left with that, feel free to report them here.

Installation
------------

Installation should work exactly similar as with the original version of django-cms. See the instructions (here)[http://django-cms.readthedocs.org/installation.html].

To have the text widget have the grappelli skin you need to install (django-tinymce)[http://code.google.com/p/django-tinymce/] in the first step. Then you need to configure it to use the grappelli theme, therefore add the following to your settings.py:

    # url path to your tinymce javascript (usually comes with grappelli
    # should be something like the following
    TINYMCE_JS_URL = MEDIA_URL + 'admin/tinymce/jscripts/tiny_mce/tiny_mce.js'
    # file system path to the files
    TINYMCE_JS_ROOT = os.path.join(MEDIA_ROOT, "admin","tinymce", "jscripts", "tiny_mce")
    TINYMCE_FILEBROWSER = True # if you have installed  django-filebrower
    TINYMCE_DEFAULT_CONFIG = {
        'relative_urls'     : False,
        'height'            : 400,
        'width'             : 640,
        'mode'              : "textareas",
        'theme'				: "advanced",
        'language'			: "en",
        'skin'				: "grappelli",
        'browsers'			: "gecko, safari"
	}

This should make it basically working. Of course there are a lot of other options to configure for the editor, see for example (grappelli's complete editor setup)[https://code.google.com/p/django-grappelli/source/browse/trunk/grappelli/media/tinymce_setup/tinymce_setup.js] as an example to start with.



