from .models import Post, Comment, User, SummerNote
from django import forms

from django.contrib.auth.forms import UserCreationForm

from django_summernote import fields as summer_fields

from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class CreateUserForm(UserCreationForm): # 내장 회원가입 폼을 상속받아서 확장한다.
    email = forms.EmailField(required=True) # 이메일 필드 추가

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True): # 저장하는 부분 오버라이딩
        user = super(CreateUserForm, self).save(commit=False) # 본인의 부모를 호출해서 저장하겠다.
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class PostForm_summernote(forms.ModelForm):
    #  fields = summer_fields.SummernoteTextFormField(error_messages={'required':(u'데이터를 입력해주세요'),})
    #  class Meta:
    #        model = SummerNote
    #        fields = ('fields', )
    class Meta:
        model = Post
        fields = {'title', 'text', }
    title = forms.CharField(required=True, max_length=300,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Title',
        })
    )
    text = forms.CharField(
        widget=SummernoteWidget(attrs={
            'placeholder': 'Content',
        })
    )
    

    

    
