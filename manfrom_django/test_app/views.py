import datetime

from django.shortcuts import render
from test_app.models import Worker
from main import main


def to_datatime(string):
    print(string)
    try:
        datetime_object = datetime.datetime.strptime(string, '%Y-%m-%d %H:%M:%S')
        return datetime_object
    except ValueError:
        datetime_object = datetime.datetime.strptime('1939-02-24 04:00:00', '%Y-%m-%d %H:%M:%S')
        return datetime_object


def to_int(string):
    if string == '' or string == ' None':
        return -1
    else:
        return int(string)


def to_float(string):
    if string == '' or string == ' None':
        return -1.0
    else:
        return float(string)


def index_page(request):
    data = main()

    for person in data:
        if not Worker.objects.filter(customers_id=(int(person["customers_id"]))):
            temp_data = Worker()
            temp_data.customers_id = int(person["customers_id"])
            temp_data.customers_cid = to_int(person["customers_cid"])
            temp_data.customers_vat_id = person["customers_vat_id"]
            temp_data.customers_vat_status = bool(person["customers_vat_id_status"])
            temp_data.customers_warning = person["customers_warning"]
            temp_data.customers_status = int(person["customers_status"])
            temp_data.customers_gender = person["customers_gender"]
            temp_data.customers_firstname = person["customers_firstname"]
            temp_data.customers_secondname = person["customers_secondname"]
            temp_data.customers_lastname = person["customers_lastname"]
            temp_data.customers_dob = to_datatime(person["customers_dob"])
            temp_data.customers_email_address = person["customers_email_address"]
            temp_data.customers_default_address_id = to_int(person["customers_default_address_id"])
            temp_data.customers_telephone = person["customers_telephone"]
            temp_data.customers_fax = person["customers_fax"]
            temp_data.customers_password = person["customers_password"]
            temp_data.customers_newsletter = bool(person["customers_newsletter"])
            temp_data.customers_newsletter_mode = to_int(person["customers_newsletter_mode"])
            temp_data.member_flag = to_int(person["member_flag"])
            temp_data.delete_user = bool(person["delete_user"])
            temp_data.account_type = to_int(person["account_type"])
            temp_data.password_request_key = person["password_request_key"]
            temp_data.payment_unallowed = bool(person["payment_unallowed"])
            temp_data.shipping_unallowed = bool(person["shipping_unallowed"])
            temp_data.refferers_id = to_int(person["refferers_id"])
            temp_data.customers_date_added = to_datatime(person["customers_date_added"])
            temp_data.customers_last_modified = to_datatime(person["customers_last_modified"])
            temp_data.orig_reference = person["orig_reference"]
            temp_data.login_reference = person["login_reference"]
            temp_data.login_tries = to_int(person["login_tries"])
            temp_data.login_time = to_datatime(person["login_time"])
            temp_data.customers_username = person["customers_username"]
            temp_data.customers_fid = to_int(person["customers_fid"])
            temp_data.customers_sid = to_int(person["customers_sid"])
            temp_data.customers_personal_discount = to_float(person["customers_personal_discount"])
            temp_data.save()

    workers = Worker.objects.all()
    context = {
        'keys': data[0].keys(),
        'worker': workers
    }

    return render(request, 'index.html', context)