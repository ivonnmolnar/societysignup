from django.shortcuts import render
from .models import Members, Courses
from .forms import MembershipForm, Courses
from .helper import write_gogle

from django.http import HttpResponse
def index(request):
    context_dict = {}
    if request.method == 'POST':
        membership_form = MembershipForm(request.POST)
        if membership_form.is_valid():
            membership_form.save()
            write_gogle(request.POST['firstname'], request.POST['lastname'], request.POST['email'])
            print(Members.objects.all())
            context_dict['message'] = "Everything went okie dokie"

        else:
            context_dict['message'] = "Yikes, sth went wrong"

        return render(request, 'membershipform/index.html', context=context_dict)

    else:
        context_dict['membershipform'] = MembershipForm()
        return render(request, 'membershipform/index.html', context=context_dict)
