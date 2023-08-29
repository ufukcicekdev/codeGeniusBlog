from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        uploaded_file = request.FILES['upload']
        
        # Geçici olarak yüklenecek dosyanın yolu
        temp_file_path = os.path.join('/tmp', uploaded_file.name)
        
        with open(temp_file_path, 'wb+') as temp_file:
            for chunk in uploaded_file.chunks():
                temp_file.write(chunk)
        
        # DigitalOcean Spaces kimlik doğrulama bilgileri
        bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
        img_path = os.getenv('AWS_STORAGE_BLOG_CKEEDITOR_PATH') 
        
        # Dosyayı DigitalOcean Spaces'e yükleme
        session = boto3.session.Session()
        s3_client = session.client('s3',
                            endpoint_url=os.getenv('AWS_S3_ENDPOINT_URL'),
                            region_name=os.getenv('AWS_S3_REGION_NAME'),
                            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'))
        
        try:
            with open(temp_file_path, 'rb') as file_data:
                s3_client.upload_fileobj(file_data, bucket_name, img_path + uploaded_file.name, ExtraArgs={'ACL': 'public-read'})
        except Exception as e:
            return JsonResponse({'error': str(e)})

        # Geçici dosyayı sil
        os.remove(temp_file_path)

        # CKEditor'e cevap gönder
        response_data = {
            'uploaded': 1,
            'fileName': uploaded_file.name,
            'url': f'https://{bucket_name}.fra1.digitaloceanspaces.com/{img_path}{uploaded_file.name}'
        }
        print("response_data", response_data)
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'})
