# views.py
from django.shortcuts import render, redirect
from .forms import ImageUploadForm

def upload_image(request):
    try:
        # Your image upload code here
        # Example: image = request.FILES['image']
        # Save the image to the folder

        # Redirect to the success page upon successful upload
        if request.method == 'POST':
            form = ImageUploadForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'success.html')  # 'success' is the name of your success view
        else:
            form = ImageUploadForm()
        return render(request, 'upload.html', {'form': form})
    except Exception as e:
        # Log the exception for debugging purposes
        print(str(e))
    return render(request, 'upload.html')

def success(request):
    return render(request, 'success.html')