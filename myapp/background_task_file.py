from background_task import background

from django.core.mail import send_mail
from django.conf import settings
from myapp.models import Todo
from django.contrib.auth.models import User
from myapp.serializers import UserSerializer, TodoSerializer, RegistrationSerializer


@background(schedule=10)
def task_notifier():
    print("Hello World!")
    try:
        queryset = Todo.objects.get(scheduled_at = datetime.now()+timedelta(seconds=300))
        for task in queryset:
            message = "Your scheduled task," + task.description + " is about to start."
            send_mail("Reminder", message, "Sahil Singla", ['ss74966@gmail.com',task.owner.email])
    except :
        print("except")
        pass


@background(schedule=6000)
def task_report():
    print("task task_report!")
    all_users = User.objects.all()
    try:
        for user in all_users:
            queryset = Todo.objects.get(owner = user, scheduled_at__gt = datetime.now()-timedelta(minutes=600), scheduled_at__lt = datetime.now())
            serializer = TodoSerializer(queryset, many=True)
            send_mail("Reminder", serializer, "Sahil Singla", ['ss74966@gmail.com',user.email])
    except :
        print("except")
        pass