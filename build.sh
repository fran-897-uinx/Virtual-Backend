echo "Building the project..."
pip install -r requirements.txt
python manage.py collectstatic --noinput

echo "migration database..."
python manage.py makemigrations
python manage.py migrate

echo "Build completed."