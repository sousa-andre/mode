from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active_namespace(context, namespace):
    request_namespace = context['request'].resolver_match.namespace
    if ':' in request_namespace:
        request_namespace = request_namespace.split(':')[0]
    if request_namespace == namespace:
        return 'active'
    return ''


@register.simple_tag(takes_context=True)
def active_view(context, view_name):
    print(context['request'].resolver_match.url_name, view_name)
    if context['request'].resolver_match.url_name == view_name:
        return 'active'
    return ''
