# ������  **YaMDb**

������  **YaMDb**  ��������  **������**  (Review) ������������� ��  **������������**  (Titles). ������������ ������� �� ���������: ������, ��������, �������. ������  **���������**  (Category) ����� ���� �������� ���������������.

���� ������������ �  **YaMDb**  �� ��������.

� ������ ��������� ����  **������������**. 

������������ ����� ���� ��������  **����**  �� ������ �����������������. ����� ����� ����� ��������� ������ �������������.

������������ ��������� � ������������� ���������  **������**  � ������ ������������ ������ � ��������� �� ������ �� ������ (����� �����); �� ���������������� ������ ����������� ����������� ������ ������������ �  **�������**  (����� �����). �� ���� ������������ ������������ ����� �������� ������ ���� �����.

## �������� ����������� �������������

1.  ������������ ���������� POST-������ �� ���������� ������ ������������ � ����������� `email` � `username` �� �������� `/api/v1/auth/signup/`.
2.  **YaMDB** ���������� ������ � ����� ������������� (`confirmation_code`) �� ����� `email`.
3.  ������������ ���������� POST-������ � ����������� `username` � `confirmation_code` �� �������� `/api/v1/auth/token/`, � ������ �� ������ ��� �������� `token` (JWT-�����).
4.  ��� ������� ������������ ���������� PATCH-������ �� �������� `/api/v1/users/me/` � ��������� ���� � ���� �������� (�������� ����� � � ������������).

### ���������������� ����

-   **������**  � ����� ������������� �������� ������������, ������ ������ � �����������.
-   **������������������� ������������ (**`user`**)**  � ����� ������ ��, ��� �  **������**, ����� ����������� ������ � ������� ������ �������������, ����� �������������� ������; ����� ������������� � ������� ���� ������ � �����������, ������������� ���� ������ ������������. ��� ���� ������������� �� ��������� ������� ������ ������������.
-   **��������� (**`moderator`**)**  � �� �� �����, ��� � �  **�������������������� ������������**, ���� ����� ������� � �������������  **�����**  ������ � �����������.
-   **������������� (**`admin`**)**  � ������ ����� �� ���������� ���� ��������� �������. ����� ��������� � ������� ������������, ��������� � �����. ����� ��������� ���� �������������.
-   **��������� Django**  ������ ������ �������� ������� ��������������, ������������ � �������  `admin`. ���� ���� �������� ���������������� ���� ���������� � ��� �� ����� ��� ���� ��������������. ��������� � ������ �������������, �� ������������� � �� ����������� ���������.

### �������� ������������ ���������������

������������ ����� ������� ������������� � ����� �����-���� ����� ��� ����� POST-������ �� ����������� ��������  `api/v1/users/`  (�������� ����� ������� ��� ����� ������ � � ������������). � ���� ������ ������ � ����� ������������� ������������ ���������� �� �����.

����� ����� ������������ ������ �������������� ��������� ����  `email` � `username`  �� ��������  `/api/v1/auth/signup/`  , � ����� ��� ������ ������ ������ � ����� �������������.

����� ������������ ���������� POST-������ � ����������� `username` � `confirmation_code` �� �������� `/api/v1/auth/token/`, � ������ �� ������ ��� �������� `token` (JWT-�����), ��� � ��� ��������������� �����������.

### ������� API  **YaMDb**

-   ������  **auth:**  ��������������.
-   ������  **users:**  ������������.
-   ������  **titles:**  ������������, � ������� ����� ������ (����������� �����, ����� ��� �������).
-   ������  **categories:**  ��������� (����) ������������ (��������, ������, �������).
-   ������  **genres**: ����� ������������. ���� ������������ ����� ���� ��������� � ���������� ������.
-   ������  **reviews:**  ������ �� ������������. ����� �������� � ������������ ������������.
-   ������  **comments:**  ����������� � �������. ����������� �������� � ������������ ������.

������ ������ ����� �������� ������ � ������������ �� ������ http://127.0.0.1:8000/redoc/ 
������� ��������� (������, �� ������� ����� ������� ������), ����������� ���� ��������, ����� ������� � �������������� ���������.

### ������������ ����������    

 - Python       
 - Django REST framework
 - Git
 - SQLite3
 - Simple JWT

### ��������� �������

C������ � ������������ ����������� ���������:


    python -m venv env

    source env/Scripts/activate
    
    python -m pip install --upgrade pip

���������� ����������� �� ����� requirements.txt:

    pip install -r requirements.txt

������� � �������� �����:

    cd api_yamdb

����������� � ��������� ��������:

    python manage.py makemigrations
    python manage.py migrate

��������� �������� ������ (��� �������������):

    python load_csv.py

��������� ������:

    python manage.py runserver


## ������ ������� ������������� � �� ���� ���������������

-   **������ �����������** - ����������� ����� (https://github.com/zrivkoren).  ��� �����, ���������� ���������� �������������� (*Auth*  �  *Users*): ������� ����������� � ��������������, ����� �������, ������ � �������, ������� ������������� ����� e-mail.
-   **������ �����������** - ������ ������ (https://github.com/Peshkov-Matvei). ���������� ��������� (*Categories*), ����� (***Genres***) � ������������ (*Titles*): ������, ������������� � ��������� ��� ���.
-   **������ �����������** - ���������� �������� (https://github.com/vovainfo) ���������� �������� ������� (*Review*) � ������������ (*Comments*): ������ ������, �������������, �������� ���������, ��������� ����� ������� ��� ��������, � ����� ������ �������� ������������.



