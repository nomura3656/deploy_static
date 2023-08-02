# デプロイ後、staticフォルダを覗くためにやったこと(ざっくり)
# setting.pyの
# templatesに'django.template.context_processors.static'
# STATIC_ROOT = os.path.join(BASE_DIR, "static") を書いた
# config/urls.pyのurlpatternに「+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 」を書いた
# 結果・・・staticフォルダの中のcss/style.cssにアクセスすることができた
# whitenoiseが云々。みたいなことは今回使用していない
