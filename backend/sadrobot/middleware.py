from django_minify_html.middleware import MinifyHtmlMiddleware


class ProjectMinifyHtmlMiddleware(MinifyHtmlMiddleware):
    minify_args = MinifyHtmlMiddleware.minify_args | {
        "keep_closing_tags": True,
        "keep_spaces_between_attributes": True,
        "keep_html_and_head_opening_tags": True,
        "remove_bangs": True,
        "ensure_spec_compliant_unquoted_attribute_values": True,
    }
