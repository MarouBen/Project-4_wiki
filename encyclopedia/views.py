from django.shortcuts import render,redirect
import markdown2
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def page(request, page):
    entry = util.get_entry(page)
    if entry is None:
        return render(request, "encyclopedia/not_found.html",{
            "Title": page
        })
    else:
        return render(request, "encyclopedia/pages.html",{
                      "data": markdown2.markdown(entry),
                      "Title": page
                      })
        
def search(request):
    search = request.GET.get("q","")
    if util.get_entry(search) is not None:
        return redirect(f"wiki/{search}")
    else:
        return render(request, "encyclopedia/not_found.html",{
            "Title": search
        })


    