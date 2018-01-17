from django.conf.urls import url

from lesson.views import HelloView, AnsibleLessonView, HelloSuperView, HelloAnsibleView

urlpatterns = [
    url('^hello/$', HelloView.as_view(), name="helle_view"),
    url('^ansible/$', AnsibleLessonView.as_view(), name="ansible_view"),
    url('^hello/ansible/$', HelloAnsibleView.as_view(), name="hello_ansible_view"),
    url('^hello/hhh/$', HelloSuperView.as_view(), name="hello_super_view"),
]
