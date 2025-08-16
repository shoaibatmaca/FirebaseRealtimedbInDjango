# userinfo/views.py

from django.shortcuts import render, redirect
from .firebase import database_ref

# Function to add user to Firebase Realtime Database
def add_user_to_firebase(name, email):
    user_ref = database_ref.child('users').push({
        'name': name,
        'email': email
    })
    return user_ref

# Function to retrieve users from Firebase Realtime Database
def get_users_from_firebase():
    users_ref = database_ref.child('users')
    users = users_ref.get()
    return users

# View to handle adding a user
def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        add_user_to_firebase(name, email)
        return redirect('list_users')  # Redirect to the list_users view
    return render(request, 'add_user.html')

# View to handle listing users
def list_users(request):
    users = get_users_from_firebase()
    return render(request, 'list_users.html', {'users': users})
