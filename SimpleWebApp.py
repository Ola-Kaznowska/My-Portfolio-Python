import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.core.wsgi import get_wsgi_application
from django.utils.html import escape

# Django configuration
settings.configure(
    DEBUG=True,
    SECRET_KEY='secretkey',
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["*"],
    MIDDLEWARE=[],
    TEMPLATES=[{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
    }],
)

# In-memory "database"
ITEMS = []
LOGGED_IN_IPS = set()

# Forms
class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class AddItemForm(forms.Form):
    name = forms.CharField(label="Item Name")

# Authentication check
def is_authenticated(request):
    return request.META["REMOTE_ADDR"] in LOGGED_IN_IPS

# Views
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["username"] == "admin" and form.cleaned_data["password"] == "secret":
                LOGGED_IN_IPS.add(request.META["REMOTE_ADDR"])
                return HttpResponseRedirect("/items")
            else:
                return HttpResponse("❌ Invalid login or password", status=401)
    else:
        form = LoginForm()
    return HttpResponse(f"""
        <h2>🔐 Login</h2>
        <form method="post">
            {form.as_p()}
            <button type="submit">Login</button>
        </form>
    """)

def items_view(request):
    if not is_authenticated(request):
        return HttpResponseRedirect("/login")

    items_html = "".join(f"<li>{escape(item)}</li>" for item in ITEMS)
    return HttpResponse(f"""
        <h2>📦 Item List</h2>
        <ul>{items_html}</ul>
        <a href="/add">➕ Add New Item</a>
    """)

def add_item_view(request):
    if not is_authenticated(request):
        return HttpResponseRedirect("/login")

    if request.method == "POST":
        form = AddItemForm(request.POST)
        if form.is_valid():
            ITEMS.append(form.cleaned_data["name"])
            return HttpResponseRedirect("/items")
    else:
        form = AddItemForm()
    return HttpResponse(f"""
        <h2>➕ Add Item</h2>
        <form method="post">
            {form.as_p()}
            <button type="submit">Add</button>
        </form>
    """)

# URL patterns
urlpatterns = [
    path("login", login_view),
    path("items", items_view),
    path("add", add_item_view),
]

# WSGI app
application = get_wsgi_application()

# Run server
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], "runserver", "8000"])



