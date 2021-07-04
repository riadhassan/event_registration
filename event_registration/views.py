from django.http import HttpRequest
from django.shortcuts import render
from storage.data_store import Ticket
from event_registration.forms import reg_info


def event_registration(request: HttpRequest):
    form = reg_info()
    success = False
    if request.method == "POST":
        # errors = {}
        fields = ["name", "email", "phone", "check"]
        info = {field: request.POST.get(field) for field in fields}
        # if info["check"]:
        #     if len(info["name"].strip()) == 0:
        #         errors["name"] = "Enter Your Name"
        #     if len(info["email"].strip()) == 0:
        #         errors["email"] = "Enter Your Email"
        #     if len(info["phone"].strip()) != 11:
        #         errors["phone"] = "Enter a valid phone number"
        # else:
        #     errors["check"] = "Please agree with our terms and conditions"
        form = reg_info(data=request.POST)

    if form.is_valid():
        success = True
        ticket = Ticket(
            info["name"].strip(),
            info["email"].strip(),
            info["phone"].strip()
        )
        ticket.save()
    else:
        ticket = None
        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' is-danger'
    return render(request, "index.html", {
        "success": success,
        "ticket": ticket,
        'form': form
    })
