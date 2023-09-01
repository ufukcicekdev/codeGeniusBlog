import os
import boto3
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token, csrf_exempt
from django_editorjs.fields import EditorJsField
from dotenv import load_dotenv

load_dotenv()

@csrf_exempt
def upload_blog_image(request,slug):
    if request.method == 'POST' and request.FILES.get('image'):
        f = request.FILES['image']

        # Dosyayı Spaces'e veya S3'e yükleyin
        session = boto3.session.Session()
        s3_client = session.client(
            's3',
            endpoint_url=os.getenv('AWS_S3_ENDPOINT_URL'),
            region_name=os.getenv('AWS_S3_REGION_NAME'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
        img_path = os.getenv('AWS_STORAGE_BLOG_CKEEDITOR_PATH')
        cleaned_filename = str(f).strip()
        filename, ext = cleaned_filename.split('.')

        try:
            s3_client.upload_fileobj(
                f,
                bucket_name,
                img_path + filename + '.' + ext,
                ExtraArgs={'ACL': 'public-read'}
            )
        except Exception as e:
            return JsonResponse({'error': str(e)})

        # Spaces'e yüklenen dosyanın URL'sini oluşturun
        file_url = f'https://{bucket_name}.fra1.digitaloceanspaces.com/{img_path}{filename}.{ext}'

        # JSON yanıtı oluşturun
        response_data = {
            'success': 1,
            'file': {
                'url': file_url,
                'name': f.name,
                'size': f.size,
            }
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'})
@csrf_exempt
def upload_blog_file(request,slug):
    if request.method == 'POST' and request.FILES.get('file'):
        f = request.FILES['file']

        # Dosyayı Spaces'e veya S3'e yükleyin
        session = boto3.session.Session()
        s3_client = session.client(
            's3',
            endpoint_url=os.getenv('AWS_S3_ENDPOINT_URL'),
            region_name=os.getenv('AWS_S3_REGION_NAME'),
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
        )

        bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
        img_path = os.getenv('AWS_STORAGE_BLOG_CKEEDITOR_PATH')
        cleaned_filename = str(f).strip()
        filename, ext = cleaned_filename.split('.')

        try:
            s3_client.upload_fileobj(
                f,
                bucket_name,
                img_path + filename + '.' + ext,
                ExtraArgs={'ACL': 'public-read'}
            )
        except Exception as e:
            return JsonResponse({'error': str(e)})

        # Spaces'e yüklenen dosyanın URL'sini oluşturun
        file_url = f'https://{bucket_name}.fra1.digitaloceanspaces.com/{img_path}{filename}.{ext}'

        # JSON yanıtı oluşturun
        response_data = {
            'success': 1,
            'file': {
                'url': file_url,
                'name': f.name,
                'size': f.size,
            }
        }
        return JsonResponse(response_data)

    return JsonResponse({'error': 'Invalid request'})