from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'year', 'image', 'repository', 'skill']

        widgets = {
'name': forms. TextInput(attrs={'placeholder' : 'Project Name'}),

'description': forms. Textarea

}