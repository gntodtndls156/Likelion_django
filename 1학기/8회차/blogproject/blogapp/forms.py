class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'email', 'birth']