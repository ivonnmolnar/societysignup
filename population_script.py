import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','societysignup.settings')
import django
django.setup()
from membershipform.models import Courses

def populate():
    with open("courses.txt", "r") as file:
        for course in file:
            Courses.objects.get_or_create(coursename=course)

if __name__ == '__main__':
    print("Starting population script...")
    populate()
