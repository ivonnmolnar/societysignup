from django.shortcuts import render
from .models import Members, Courses
from .forms import MembershipForm, Courses
from .helper import write_gogle, write_info

from django.http import HttpResponse
def index(request):
    context_dict = {}
    if request.method == 'POST':
        membership_form = MembershipForm(request.POST)
        if membership_form.is_valid():
            membership_form.save()
            write_gogle(request.POST['firstname'], request.POST['lastname'], request.POST['email'])
            write_info(request.POST['firstname'], request.POST['lastname'], request.POST['email'], request.POST['studentID'], Courses.objects.get(pk=int(request.POST['subject'])).coursename, request.POST['year'])
            context_dict['message'] = "Everything went okie dokie."

        else:
            context_dict['message'] = "Yikes, something went wrong."

        return render(request, 'membershipform/index.html', context=context_dict)

    else:
        context_dict['membershipform'] = MembershipForm()
        return render(request, 'membershipform/index.html', context=context_dict)
