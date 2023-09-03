import os
import boto3
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import ensure_csrf_cookie, requires_csrf_token, csrf_exempt
import logging
from django.conf import settings
from django_editorjs.fields import EditorJsField
from dotenv import load_dotenv
import uuid

load_dotenv()

db_logger = logging.getLogger('db')


@csrf_exempt
def editorjs_image_upload(request):
    try:
        if request.method == 'POST' and request.FILES.get('image'):
            f = request.FILES['image']
            fs = FileSystemStorage()

            # Dosyayı benzersiz bir isimle kaydetme
            unique_filename = generate_unique_filename(f.name)
            filename = fs.save(unique_filename, f)

            # Dosyayı yerel depolamadan alın
            file_name = os.path.join(settings.MEDIA_ROOT, unique_filename)
            print("file_name",file_name)
            with open(file_name, 'rb') as local_file:
                session = boto3.session.Session()

                # AWS istemci oluşturma
                s3_client = session.client(
                    's3',
                    endpoint_url=os.getenv('AWS_S3_ENDPOINT_URL'),
                    region_name=os.getenv('AWS_S3_REGION_NAME'),
                    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
                )

                bucket_name = os.getenv('AWS_STORAGE_BUCKET_NAME')
                img_path = os.getenv('AWS_STORAGE_BLOG_CKEEDITOR_PATH')
                cleaned_filename = str(filename).strip()
                filename, ext = cleaned_filename.split('.')

                try:
                    print("Dosyayı uzak depolamaya yükleme")
                    print(file_name,
                        bucket_name, img_path)
                    s3_client.upload_file(
                        file_name,
                        bucket_name,
                        img_path + filename + '.' + ext,
                        ExtraArgs={'ACL': 'public-read'}
                    )
                except Exception as e:
                    return JsonResponse({'error': str(e)})

            # Dosyayı yerel depolamadan silme
            os.remove(file_name)

            # Uzak depolama URL'sini oluşturma
            file_url = f'https://{bucket_name}.fra1.digitaloceanspaces.com/{img_path}{filename}.{ext}'

            # JSON yanıtı oluşturma
            response_data = {
                'success': 1,
                'file': {
                    'url': file_url,
                    'name': unique_filename,
                    'size': f.size,
                }
            }
            return JsonResponse({'success': 1, 'file': {'url': file_url}})

    except Exception as e:
        return JsonResponse({'error': str(e)})
    

@csrf_exempt
def editorjs_file_upload(request):
    try:
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
            return JsonResponse({'success':1,'file':{'url':file_url,'name':str(f.name),'size':f.size}})

        return JsonResponse({'error': 'Invalid request'})
    except Exception as e:
        db_logger.exception(e)



def generate_unique_filename(filename):
    ext = filename.split('.')[-1]
    unique_filename = f"{uuid.uuid4().hex}.{ext}"
    return unique_filename