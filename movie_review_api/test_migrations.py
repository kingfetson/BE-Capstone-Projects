import os
import django
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_review_api.settings')
django.setup()

try:
    from django.db.migrations.loader import MigrationLoader
    print("✓ MigrationLoader imported successfully")
    
    loader = MigrationLoader(None, ignore_no_migrations=True)
    print("✓ MigrationLoader initialized")
    
    call_command('makemigrations', 'users', verbosity=3)
    print("✓ makemigrations users completed")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
