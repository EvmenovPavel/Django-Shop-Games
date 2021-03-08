from django.template import Library
import re

from django import template

# register = template.Library()


register = Library()


@register.simple_tag
def active(request, pattern):
    if re.search(pattern, request.path):
        return "active"
    return ""


@register.tag
def my_tag(request, pattern):
    pass


@register.filter()
def twitter_date(value):
    import datetime
    split_date = value.split()
    del split_date[0], split_date[-2]
    value = ' '.join(split_date)  # Fri Nov 07 17:57:59 +0000 2014 is the format
    return datetime.datetime.strptime(value, '%b %d %H:%M:%S %Y')


@register.filter()
def urlize_tweet_text(tweet):
    """ Turn #hashtag and @username in status text to Twitter hyperlinks,
        similar to the ``urlize()`` function in Django.
    """
    try:
        from urllib import quote
    except ImportError:
        from urllib.parse import quote
    hashtag_url = '<a href="https://twitter.com/search?q=%%23%s" target="_blank">#%s</a>'
    user_url = '<a href="https://twitter.com/%s" target="_blank">@%s</a>'
    text = tweet.text
    for hash in tweet.hashtags:
        text = text.replace('#%s' % hash.text, hashtag_url % (quote(hash.text.encode("utf-8")), hash.text))
    for mention in tweet.user_mentions:
        text = text.replace('@%s' % mention.screen_name, user_url % (quote(mention.screen_name), mention.screen_name))
    return text


@register.filter()
def expand_tweet_urls(tweet):
    """ Replace shortened URLs with long URLs in the twitter status
        Should be used before urlize_tweet
    """
    text = tweet.text
    urls = tweet.urls
    for url in urls:
        text = text.replace(url.url, '<a href="%s" target="_blank">%s</a>' % (url.expanded_url, url.url))
    tweet.SetText(text)
    return tweet


def deepzoom_js(parser, token):
    try:
        tag_name, deepzoom_object, deepzoom_div_id = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "The %r tag requires two arguments: 'Deep Zoom object' and 'Deep Zoom div ID'." % token.contents.split()[0])
    if (deepzoom_object[0] == deepzoom_object[-1] and deepzoom_object[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "The %r tag's 'Deep Zoom object' argument should not be in quotes." % tag_name)
    if not (deepzoom_div_id[0] == deepzoom_div_id[-1] and deepzoom_div_id[0] in ('"', "'")):
        raise template.TemplateSyntaxError("The %r tag's 'Deep Zoom div ID' argument should be in quotes." % tag_name)
    return DeepZoom_JSNode(deepzoom_object, deepzoom_div_id[1:-1])


class DeepZoom_JSNode(template.Node):
    def __init__(self, deepzoom_object, deepzoom_div_id):
        self.deepzoom_object = template.Variable(deepzoom_object)
        self.deepzoom_div_id = deepzoom_div_id

    def render(self, context):
        try:
            dz_object = self.deepzoom_object.resolve(context)
            t = template.loader.get_template('deepzoom/deepzoom_js.html')
            return t.render(template.Context({'deepzoom_object': dz_object,
                                              'deepzoom_div_id': self.deepzoom_div_id},
                                             autoescape=context.autoescape))
        except template.VariableDoesNotExist:
            return ''


register.tag('deepzoom_js', deepzoom_js)
