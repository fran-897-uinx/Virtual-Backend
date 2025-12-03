echo "Building the project..."
pip install -r requirements.txt
python manage.py collectstatic --noinput

echo "migration database..."
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser..."
export $(grep -v '^#' .env.local | xargs)
bash create_ad.sh


echo "Build completed."
echo "You can now run the server using: python manage.py runserver"