from django.shortcuts import render

from .forms import UserRegistrationForm, UserProfileRegistrationForm

# Create your views here.
def index(request):
	return render(request, 'dcoin_app/index.html')

def register(request):
	userform = UserRegistrationForm()
	profileform = UserProfileRegistrationForm()
	registered = False

	if request.method == 'POST':
		userform = UserRegistrationForm(data=request.POST)
		profileform = UserProfileRegistrationForm(request.POST)

		if userform.is_valid() and profileform.is_valid():
			user = userform.save()
			user.set_password(user.password)
			userform.save()

			profile = profileform.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profileform.save()
			registered = True
		else:
			print(userform.errors, profileform.errors)

	context = {'userform' : userform,
			   'profileform' : profileform,
			   'registered' : registered}

	return render(request, 'dcoin_app/register.html', context)