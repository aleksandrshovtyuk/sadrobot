from django_minify_html.middleware import MinifyHtmlMiddleware


class ProjectMinifyHtmlMiddleware(MinifyHtmlMiddleware):
    minify_args = MinifyHtmlMiddleware.minify_args | {
        "keep_closing_tags": True,
    }
