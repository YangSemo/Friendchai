from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


# class RegistrationForm(UserCreationForm):
#     email = forms.EmailField(max_length=60, help_text='유효한 이메일을 입력해주세요')
#
#     class Meta:
#         model = Account
#         fields = ("email", 'username', 'password1', 'password2')
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email').lower()
#         try:
#             account = Account.objects.get(email=email)
#         except Exception as e:
#             return email
#         raise forms.ValidationError("이미 사용중인 이메일입니다.")
#
#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         try:
#             account = Account.objects.get(username=username)
#         except Exception as e:
#             return username
#         raise forms.ValidationError(f"이미 사용중인 이름입니다.")
#
#
# class AccountAuthenticationForm(forms.ModelForm):
#     password = forms.CharField(label='password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = Account
#         # fields = ('username', 'password')
#         fields = ('email', 'password')
#
#     def clean(self):
#         if self.is_valid():
#             # username = self.cleaned_data.get('username')
#             email = self.cleaned_data.get('email')
#             password = self.cleaned_data.get('password')
#
#             # if not authenticate(username=username, password=password):
#             if not authenticate(email=email, password=password):
#                 raise forms.ValidationError('Invalid Login')

# class AccountUpdateform(forms.ModelForm):
#     """
#       Updating User Info
#     """
#     class Meta:
#         model  = Account
#         fields = ('email', 'username')
#         widgets = {
#                    'email':forms.TextInput(attrs={'class':'form-control'}),
#                    'password':forms.TextInput(attrs={'class':'form-control'}),
#         }
#
#     def __init__(self, *args, **kwargs):
#         """
#           specifying styles to fields
#         """
#         super(AccountUpdateform, self).__init__(*args, **kwargs)
#         for field in (self.fields['email'],self.fields['username']):
#             field.widget.attrs.update({'class': 'form-control '})
#
#     def clean_email(self):
#         if self.is_valid():
#             email = self.cleaned_data['email']
#             try:
#                 account = Account.objects.exclude(pk = self.instance.pk).get(email=email)
#             except Account.DoesNotExist:
#                 return email
#             raise forms.ValidationError("Email '%s' already in use." %email)
#     def clean_username(self):
#         if self.is_valid():
#             username = self.cleaned_data['username']
#             try:
#                 account = Account.objects.exclude(pk = self.instance.pk).get(username=username)
#             except Account.DoesNotExist:
#                 return username
#             raise forms.ValidationError("Username '%s' already in use." % username)
