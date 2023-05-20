cd sadko/


until nc -z -v -w30 $POSTGRES_HOST $POSTGRES_PORT; do
    echo "Ожидание доступности базы данных..."
    sleep 1
  done
  echo "База данных готова"


if ! python manage.py showmigrations --no-color | grep "\[ \]"; then
  exec gunicorn sadko.wsgi:application -b 0.0.0.0:8000
else
  python manage.py migrate
  exec gunicorn sadko.wsgi:application -b 0.0.0.0:8000
fi