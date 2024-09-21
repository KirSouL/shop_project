Проект интернет магазина на Django

Перед работай с проектом рекомендовано произвести настройки в PostgreSQL сервере,
а именно в файле pg_hba.conf настроить параметры аутентификации для сервера своей
машины. Согласно примеру ниже.

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             all                                     trust
# IPv4 local connections:
host    all             all             127.0.0.1/32            trust
# IPv6 local connections:
host    all             all             ::1/128                 trust
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     trust
host    replication     all             127.0.0.1/32            trust
host    replication     all             ::1/128                 trust

После настройки подключения к базе данных локального сервера ввод пароля не требуется.

Кастомная команда позволяет заполнять базу данных на основе ранее сохраннего файла json
полученного с помощью фикстуры dumpdata.

При добавлении новой категории или нового продукта в базу данных (через админку, через shell)
необходимо обновить файл catalog_data.json.
Путем ввода в терминале команды: python -Xutf8 manage.py dumpdata catalog > catalog/data/catalog_data.json
Если выше приведенная команда не выполнится, введите следующую строку:
python -Xutf8 manage.py dumpdata --exclude auth.permission --exclude auth.user --exclude admin.logentry
--exclude contenttypes.contenttype --exclude sessions.session -o catalog/data/catalog_data.json 

Для работы с админкой создайте нового администратора. В терминале пропишите команду: python manage.py createsuperuser
И укажите имя админа и пароль.

Для перехода на страницу с конкретным товаром необходимо:
1. Запустить сервер;
2. К http://127.0.0.1:8000/ в конце добавить запись product/"id_продукта"/. К примеру, http://127.0.0.1:8000/product/5/

Магазин расширен разделом "Блог". В котором можно создавать, обновлять, удалять блог.
Аналогино доступно и в разделе продуктов.
