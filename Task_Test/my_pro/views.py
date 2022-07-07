from django.http import HttpResponse
from citate.models import Quote
from django.template.loader import render_to_string

def author_view(request):
    # html_string = f''' <h1>  My favorite citates  </>'''

    citate_objjs = Quote.objects.all()
    citate_object = Quote.objects.get(id=1)
    context = {"list_of_words": citate_objjs,
                "text": citate_object.text,
               "quote_author": citate_object.quote_author}
    html_string = render_to_string("author_view.html", context)
    return HttpResponse(html_string)