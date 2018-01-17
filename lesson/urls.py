from django.conf.urls import url

from lesson.views import HelloView, AnsibleLessonView, HelloAnsibleView, HelloSuperView

urlpatterns = [
    url('^hello/$', HelloView.as_view(), name="helle_view"),
    url('^ansible/$', AnsibleLessonView.as_view(), name="ansible_view"),
    url('^hello/ansible/$', HelloAnsibleVietpuw.as_view(), name="hello_ansible_view"),
    url('^hello/super/$', HelloSuperView.as_view(), name="hello_super_view"),
]