from django.db.models import Q
from rest_framework import status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.db import DatabaseError, transaction
from django.core.exceptions import ValidationError
from rest_framework.views import APIView
from library.general.error_log import ErrorLogClass as ErrorLog 
from library.general.responses import JsonResponseMessage
from .serializers import *
from library.models.bbicore import *
from library.models.apps_vendor_management import *
from library.modules.bbi_token.views import *
from library.models.apps_plm import *
from datetime import time, datetime, timedelta
from apps_svc.settings import MEDIA_ROOT, MEDIA_URL, SERVER_HOST
from django.utils import timezone
import random
import requests
from apps_svc.settings_env import BBI_HOST_BBINOTIFICATION, BBI_TOKEN_BBINOTIFICATION, API_NOTIF_CREATE, SERVER_HOST, API_NOTIF_SEND
MOD_CODE    = 'Book Room'
DB_NAME  = 'db_book_room'
rsp  = JsonResponseMessage()


class FormMethods(object):
    
    def get_data(self, data):
        msg = None
        isValidationErr = False
        try:
            view_all = data.get('view_all')
            room_id = data.get('room_id')
            id = data.get('id')
            if data.get('for') =='calendar':
                objData = RoomBook.objects.all()
            else : 
                if id:
                    objData = RoomBook.objects.filter(id=id)
                    return objData
                else:
                # print('test',view_all)
                    date = data.get('date')
                    if view_all == True:
                        objData = RoomBook.objects.all()
                    else:
                        # print('test',view_all)
                        objData = RoomBook.objects.filter(status=True)
                    if room_id and date is not None:
                        objData = objData.filter(Q(room_id=room_id) & Q(start_at__date=date))
                
                    else:
                        objData = objData.filter(Q(start_at__date=date))
            return objData.order_by('start_at')
        except Exception as ex:
            msg = 'Fail get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)
 
    def get_available_room(self, data):
        msg = None
        isValidationErr = False
        try:
            room_id = data.get('room_id')  # Room ID
            date_str = data.get('date')     # Date as string (e.g., "2024-10-02")
            available_slots = []
            # Convert date string to a naive datetime object (just date)
            date = datetime.strptime(date_str, "%Y-%m-%d")

            # Define working hours (e.g., 8:00 AM to 5:00 PM)
            start_of_day = time(8, 0)  # 8:00 AM
            end_of_day = time(17, 0)   # 5:00 PM
            if room_id is not None: 
                roomData = RoomMasterRoom.objects.filter(id=room_id)
            else:
                roomData = RoomMasterRoom.objects.all()
            
            # Get all bookings for the specified room and date
            for room in roomData:
                
                bookings = RoomBook.objects.filter(
                    room_id=room.id,
                    start_at__date=date,  # Use the naive date for filtering
                    end_at__date=date,
                    status=True
                ).order_by('start_at')

                # Suggest available time slots
                
                current_time = datetime.combine(date, start_of_day)  # Start from 8:00 AM (naive datetime)
                # print(current_time, bookings.first().start_at.replace(tzinfo=None) +  timedelta(hours=7))
                # Check if there's available time before the first booking
                if bookings.exists() and (current_time < (bookings.first().start_at.replace(tzinfo=None) +  timedelta(hours=7))):
                    # print("masuk")
                    first_booking_start = bookings.first().start_at.replace(tzinfo=None)
                    available_start = current_time   # Add 7 hours
                    available_end = (first_booking_start - timedelta(minutes=1)) + timedelta(hours=7)  # Add 7 hours
                    # print(available_start, available_end)
                    if available_end > available_start:  # Ensure valid slot
                        available_slots.append({
                            'room_id': room.id,
                            'start': available_start.strftime("%Y-%m-%d %H:%M:%S"),
                            'end': available_end.strftime("%Y-%m-%d %H:%M:%S"),
                            'duration': (available_end - available_start).total_seconds() / 60  # Duration in minutes
                        })

                # Loop through each booking to find gaps
                for booking in bookings:
                    # Ensure booking start and end times are naive
                    booking_start_naive = booking.start_at.replace(tzinfo=None)  # Convert to naive
                    booking_end_naive = booking.end_at.replace(tzinfo=None)      # Convert to naive

                    # Check if there's a gap between the current time and the start of the next booking
                    if current_time < booking_start_naive:
    # Calculate available slot from current_time to the start of the booking
                        available_start = current_time + timedelta(hours=7)  # Add 7 hours
                        available_end = (booking_start_naive - timedelta(minutes=1)) + timedelta(hours=7)  # Add 7 hours

                        if available_end > available_start:  # Ensure valid slot
                            # Check if available_end already exists in available_slots
                            if not any(slot['end'] == available_end.strftime("%Y-%m-%d %H:%M:%S") for slot in available_slots):
                                available_slots.append({
                                    'room_id': room.id,
                                    'start': available_start.strftime("%Y-%m-%d %H:%M:%S"),
                                    'end': available_end.strftime("%Y-%m-%d %H:%M:%S"),
                                    'duration': (available_end - available_start).total_seconds() / 60  # Duration in minutes
                                })

                    # Move current_time to 1 minute after the current booking ends
                    current_time = booking_end_naive + timedelta(minutes=1)

                # After the last booking, check if there's time until the end of the day
                end_of_day_naive = datetime.combine(date, end_of_day)  # Naive end of day
                if current_time < end_of_day_naive:
                    if bookings.exists():
                        available_start = current_time + timedelta(hours=7)  # Add 7 hours
                    else:
                        available_start = current_time
                    available_end = end_of_day_naive  # End of the day

                    if available_end > available_start:  # Ensure valid slot
                        available_slots.append({
                            'room_id': room.id,
                            'start': available_start.strftime("%Y-%m-%d %H:%M:%S"),
                            'end': available_end.strftime("%Y-%m-%d %H:%M:%S"),
                            'duration': (available_end - available_start).total_seconds() / 60  # Duration in minutes
                        })
            available_slots = sorted(available_slots, key=lambda x: x['start'])
            return available_slots

        except Exception as ex:
            msg = 'Fail to get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)


    def post_data(self, data, FILES):
        # print(data)
        msg = None
        isValidationErr = False
        try:
            room_id = data.get('room_id')
            start_at = data.get('start_at')
            end_at = data.get('end_at')
            code = FormMethods.generate_unique_code()
            # Ensure the meeting time range is valid
            # print(start_at, end_at)
            if start_at >= end_at:
                raise ValidationError("End time must be after the start time.")
            location = RoomMasterRoom.objects.filter(id=room_id).first().room_name
            # Check for overlapping bookings
            overlapping_bookings = RoomBook.objects.filter(
                room_id=room_id,
                start_at__lte=end_at,   # Existing booking starts before the new at ends
                end_at__gte=start_at    # Existing booking ends after the new meeting starts
            )

            if overlapping_bookings.exists():
                raise ValidationError("The selected time conflicts with an existing booking.")
            user_nik = data.get('user_nik')
            user_nik_number = user_nik.split('-')[0]
            user_name = user_nik.split('-')[1]
            # print(user_nik_number) 
            # Create new booking within a transaction
            with transaction.atomic():
                new_booking = RoomBook(
                    code = code,
                    room_id=room_id,
                    title = data.get('title'),
                    user_nik = user_nik_number,
                    user_data = data.get('user_data'),
                    user_mail = data.get('user_mail'),
                    dept_name = data.get('dept_name'),
                    desc = data.get('desc'),
                    start_at=start_at,
                    end_at=end_at, 
                    status=True
                )
                new_booking.save()
                if data.get('send_mail') == 'yes':
                        # Send email notification
                    self.send_email(data, FILES, location, user_name)
            return new_booking
        
        except Exception as ex:
            msg = 'Fail get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)
            
    def send_email(self, data, FILES, location, organizer):
        
        schedule_at = timezone.now()
        profile_name_notif = 'mail_bbi_apparel'
        template_name_notif = 'email_book_room_meeting' 
        title_notif = 'Book Room Meeting'
        EmailTo = data.get('to')
        EmailCc = data.get('cc')
        objSenderMail                    = '"Meeting Notification"'+" <apps.mailer@bbi-apparel.com>"
        content_mail                     = {}
        file  = FILES.get('file_upload')
        # print(file)
        file_src = None
        validationFiles = False
        if file is not None and file.size > 0:
            # Remove all spaces from the file name
            cleaned_file_name = file.name.replace(' ', '')

            # Create the full path for the file in MEDIA_ROOT
            save_file_path = MEDIA_ROOT + '/' + cleaned_file_name
            file_src = SERVER_HOST + 'media/'+cleaned_file_name
            # Save the file
            with open(save_file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            validationFiles = True
            print(save_file_path)
        start_at = data.get('start_at')
        end_at = data.get('end_at')
        start_datetime = datetime.strptime(start_at, '%Y-%m-%dT%H:%M:%S')
        end_datetime = datetime.strptime(end_at, '%Y-%m-%dT%H:%M:%S')
        date = start_datetime.strftime('%d %b %Y') 
        start_time = start_datetime.strftime('%H:%M')
        end_time = end_datetime.strftime('%H:%M')
        title_notif = 'Book Room Meeting'
        content_mail['scheduled_at']     = str(schedule_at)
        content_mail['profile_name']     = profile_name_notif
        content_mail['template_name']    = template_name_notif
        content_mail['title']            = title_notif
        if validationFiles:
            content_mail['file_directory']  = file_src
        content_mail['is_attached']     = validationFiles
        content_mail['to']               = EmailTo
        content_mail['cc']               = EmailCc
        # content_mail['file']            = file.file
        content_mail['date'] = date
        content_mail['start_meeting'] = start_time
        content_mail['end_meeting'] = end_time
        content_mail['desc'] = data.get('desc')
        content_mail['location'] = location
        content_mail['sender']           = objSenderMail
        content_mail['organizer'] = organizer
        
        url = BBI_HOST_BBINOTIFICATION + API_NOTIF_CREATE
        auth_token= BBI_TOKEN_BBINOTIFICATION
        hed = {'Authorization': 'Bearer ' + auth_token , 'Content-Type': 'application/json', 'Accept': 'application/json'}
        myobj = content_mail
        # print(myobj)
        objNotif = requests.post(url, json = myobj, headers=hed, verify=False)
    def put_data(self, data, FILES):
        msg = None
        isValidationErr = False
        try:
            booking_id = data.get('item_id')  # Get the ID of the booking to update
            room_id = data.get('room_id')
            start_at = data.get('start_at')
            end_at = data.get('end_at')
            location = RoomMasterRoom.objects.filter(id=room_id).first().room_name
            # Ensure the meeting time range is valid
            if start_at >= end_at:
                raise ValidationError("End time must be after the start time.")

            # Fetch the booking to update
            booking = RoomBook.objects.get(id=booking_id)

            # Check for overlapping bookings (excluding the current booking)
            overlapping_bookings = RoomBook.objects.filter(
                room_id=room_id,
                start_at__lte=end_at,
                end_at__gte=start_at
            ).exclude(id=booking_id)  # Exclude the current booking

            if overlapping_bookings.exists():
                raise ValidationError("The selected time conflicts with an existing booking.")
            user_nik = data.get('user_nik')
            user_nik_number = user_nik.split('-')[0]
            user_name = user_nik.split('-')[1]
            # Update booking fields
            with transaction.atomic():
                booking.room_id = room_id
                booking.updated_by = data.get('updated_by')
                booking.updated_at = timezone.now()
                booking.user_mail = data.get('user_mail')
                booking.start_at = start_at
                booking.end_at = end_at
                booking.desc = data.get('desc', booking.desc)  # Keep old desc if not updated
                booking.save()
                if data.get('send_mail') == 'yes':
                    # Send email notification
                    self.send_email(data, FILES, location, user_name)
            return booking
        
        except RoomBook.DoesNotExist:
            msg = 'Booking not found.'
        except Exception as ex:
            msg = 'Fail to update data, %s' % (str(ex))

        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)
    def generate_unique_code():
        while True:
            code = str(random.randint(1000, 9999))
            existing_codes = RoomBook.objects.filter(code=code)
            if len(existing_codes) == 0:
                return code
class BookView(APIView):
    def post(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        # print(request.data)
        actions = request.data.get('action')
        if actions == 'get':
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = FormMethods()
                objGetForm = objFormMethods.get_data(request.data)
                # Serialize data
                serialized_data = RoomBookSerializer(objGetForm, many=True).data
                # Lakukan sesuatu dengan data yang diambil, seperti mengembalikan atau memproses lebih lanjut
                isSuccess = True
                jsonPayload = {"data": serialized_data}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to get data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been get', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
        else :
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = FormMethods()
                objGetForm = objFormMethods.post_data(request.data, request.FILES)
                isSuccess = True
                jsonPayload = {"creator": request.data.get('created_by')}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to create data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))
            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been created', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)

    # def post(self, request):
    #     pass

    def put(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        try:
            # Mengambil semua data dari model V_VendorServiceType
            objFormMethods = FormMethods()
            objGetForm = objFormMethods.put_data(request.data, request.FILES)
            isSuccess = True
            jsonPayload = {"creator": request.data.get('updated_by')}
            
        except ValidationError as ex:
            print(str(ex))
            ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
            return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to update data: {str(ex)}')
            
        except Exception as ex:
            ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
            return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

        if isSuccess:
            return rsp.RESPONSE_200_OK(msg='Data has been updated', payload=jsonPayload)
        # print('masuk')
        return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)

class AvailableRoomView(APIView):
    def post(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        # print(request.data)
        actions = request.data.get('action')
        if actions == 'get':
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = FormMethods()
                objGetForm = objFormMethods.get_available_room(request.data)
                # Serialize data
                # serialized_data = BookSerializer(objGetForm, many=True).data
                # Lakukan sesuatu dengan data yang diambil, seperti mengembalikan atau memproses lebih lanjut
                isSuccess = True
                jsonPayload = {"data": objGetForm}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to get data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been get', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
        
class SwitchFormMethods(object):
    def get_data(self, data):
        msg = None
        isValidationErr = False
        try:
            view_all = data.get('view_all')
            room_id = data.get('room_id')
            # print('test',view_all)
            date = data.get('date')
            user_nik = data.get('user_nik')
            objDataInbox = RoomSwitchBook.objects.filter(requester_nik_to=user_nik, state=None)
            objDataSend = RoomSwitchBook.objects.filter(requester_nik=user_nik)

            return {'inbox':objDataInbox, 'send':objDataSend}
        except Exception as ex:
            msg = 'Fail get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)

    def post_data(self, data):
        msg = None
        isValidationErr = False
        try:
            url_data = data.get('url_data')
            code = self.generate_unique_code()
            book_id = data.get('book_id')
            objBook = RoomBook.objects.filter(id=book_id).first()
            location = RoomMasterRoom.objects.filter(id=objBook.room.id).first().room_name
            to = objBook.user_mail
            cc = None
            if objBook is None:
                raise ValidationError('Booking data not found')
            requester_nik = data.get('requester_data')
            requester_nik_number = requester_nik.split('-')[0]
            organizer = requester_nik.split('-')[1]
            objChkSwitch = RoomSwitchBook.objects.filter(Q(book_id=book_id) &Q(requester_nik=requester_nik_number)&Q(state=None))
            if objChkSwitch.exists():
                raise ValidationError('Data already exist')
            
            objSwitch = RoomSwitchBook.objects.create(
                code = code,
                title = data.get('title'),
                requester_nik = requester_nik_number,
                requester_data = data.get('requester_data'),
                requester_mail = data.get('requester_mail'),
                requester_nik_to = objBook.user_nik,
                requester_data_to = objBook.user_data,
                dept_name = data.get('dept_name'),
                to = data.get('to'),
                cc = data.get('cc'),
                desc = data.get('desc'),
                state = None,
                book_id=book_id,
                created_by = data.get('created_by'),                
            )
            desc = data.get('desc')
            if data.get('send_mail') == 'yes':
                pass
            self.send_mail_switch(objBook, location,organizer, to,cc, desc, url_data, status = '-')
            return objSwitch
        
        except Exception as ex:
            msg = 'Fail get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)

    def put_data(self, data):
        msg = None
        isValidationErr = False
        try:
            url_data = data.get('url_data')
            book_id = data.get('book_id')
            switch_id = data.get('switch_id')
            state = data.get('state')
            objBook = RoomBook.objects.filter(id=book_id).first()
            objSwitch = RoomSwitchBook.objects.filter(id=switch_id).first()
            location = RoomMasterRoom.objects.filter(id=objBook.room.id).first().room_name
            requester_nik = objSwitch.requester_data_to
            desc = objSwitch.desc
            requester_nik_number = requester_nik.split('-')[0]
            organizer = requester_nik.split('-')[1]
            to = objSwitch.requester_mail
            cc = objSwitch.cc
            desc = objSwitch.desc
            status = ''
            if objBook is None or objSwitch is None:
                raise ValidationError('Booking or Switch data not found')
            if state == 'REJECTED':
                objSwitch.state = 'REJECTED'
                self.send_mail_switch(objBook, location,organizer,to,cc, desc, url_data, status)
                status = 'REJECTED'
                objSwitch.save()
            if state == 'APPROVED':
                objSwitch.state = 'APPROVED'
                status = 'APPROVED'
                self.send_mail_switch(objBook, location,organizer,to, cc, desc, url_data, status)
                objSwitch.save()
                #update status booking
                requester_nik = objSwitch.requester_data
                requester_mail = objSwitch.requester_mail
                requester_nik_number = requester_nik.split('-')[0]
                objBook.title = objSwitch.title
                objBook.user_nik = requester_nik_number
                objBook.user_mail = requester_mail
                objBook.user_data = objSwitch.requester_data
                objBook.dept_name = objSwitch.dept_name
                objBook.desc = objSwitch.desc
                objBook.save()
                objSwitchExt = RoomSwitchBook.objects.exclude(id=switch_id).filter(Q(book_id=book_id) & Q(state__isnull=True))
                if objSwitchExt.count() > 0: #hapus data request jika approved
                    for data in objSwitchExt:
                        data.state = 'REJECTED'
                        to = data.to
                        cc = data.cc
                        desc = data.desc
                        status = 'REJECTED'
                        self.send_mail_switch(objBook, location,organizer,to,cc, desc, url_data, status)
                        data.save()
                
            return objSwitch
        
        except Exception as ex:
            msg = 'Fail get data, %s' % (str(ex))
        if msg is not None:
            if isValidationErr:
                raise ValidationError(msg)
            else:
                raise Exception(msg)
    
    def generate_unique_code(self):
        while True:
            code = str(random.randint(1000, 9999))
            existing_codes = RoomSwitchBook.objects.filter(code=code)
            if len(existing_codes) == 0:
                return code
            
    def send_mail_switch(self, data, location,organizer, to, cc, desc, url_data, status):
        scheduled_at = timezone.now()
        scheduled_at = str(scheduled_at)
        profile_name_notif = 'mail_bbi_apparel'
        template_name_notif = 'email_book_room_meeting_approval' 
        title_notif = 'Book Room Meeting'
        EmailTo = to
        EmailCc = cc
        objSenderMail                    = '"Meeting Notification"'+" <apps.mailer@bbi-apparel.com>"
        content_mail                     = {}
        # file  = FILES.get('file_upload')
        # # print(file)
        file_src = ''
        validationFiles = False
        # if file :
        #     # Remove all spaces from the file name
        #     cleaned_file_name = file.name.replace(' ', '')

        #     # Create the full path for the file in MEDIA_ROOT
        #     save_file_path = MEDIA_ROOT + '/' + cleaned_file_name
        #     file_src = SERVER_HOST + 'media/'+cleaned_file_name
        #     # Save the file
        #     with open(save_file_path, 'wb+') as destination:
        #         for chunk in file.chunks():
        #             destination.write(chunk)
        # print(data)
        #     validationFiles = True
        #     print(save_file_path)
        start_at = str(data.start_at)
        end_at = str(data.end_at)

        # Parse the datetime strings into datetime objects and ignore timezone
        start_datetime = datetime.strptime(start_at, '%Y-%m-%d %H:%M:%S%z').replace(tzinfo=None)
        end_datetime = datetime.strptime(end_at, '%Y-%m-%d %H:%M:%S%z').replace(tzinfo=None)
        # Add 7 hours to both start and end times
        start_datetime_plus_7 = start_datetime + timedelta(hours=7)
        end_datetime_plus_7 = end_datetime + timedelta(hours=7)
        # Format the updated datetime objects into date and time strings
        date = start_datetime_plus_7.strftime('%d %b %Y') 
        start_time = start_datetime_plus_7.strftime('%H:%M')
        end_time = end_datetime_plus_7.strftime('%H:%M')
        
        title_notif = 'Book Room Meeting'
        content_mail['scheduled_at']     = str(scheduled_at)
        content_mail['profile_name']     = profile_name_notif
        content_mail['template_name']    = template_name_notif
        content_mail['title']            = title_notif
        # content_mail['file_directory']   = file_src
        content_mail['is_attached']      = False
        content_mail['to']               = EmailTo
        content_mail['cc']               = EmailCc
        content_mail['status']           = status
        # content_mail['file']           = file.file
        content_mail['date']             = date
        content_mail['start_meeting']    = start_time
        content_mail['end_meeting']      = end_time
        content_mail['desc']             = desc
        content_mail['location']         = location
        content_mail['sender']           = objSenderMail
        content_mail['organizer']        = organizer
        # print(url_data)
        content_mail['url']              = url_data
        # print(content_mail)
        url = BBI_HOST_BBINOTIFICATION + API_NOTIF_CREATE
        auth_token= BBI_TOKEN_BBINOTIFICATION
        hed = {'Authorization': 'Bearer ' + auth_token , 'Content-Type': 'application/json', 'Accept': 'application/json'}
        myobj = content_mail
        # print(myobj)
        objNotif = requests.post(url, json = myobj, headers=hed, verify=False)
        
class SwitchBookView(APIView):
    def post(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        # print(request.data)
        actions = request.data.get('action')
        if actions == 'get':
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = SwitchFormMethods()
                objGetForm = objFormMethods.get_data(request.data)
                # Serialize data
                serialized_inbox = RoomSwitchBookSerializer(objGetForm['inbox'], many=True).data
                serialized_send = RoomSwitchBookSerializer(objGetForm['send'], many=True).data
                # Lakukan sesuatu dengan data yang diambil, seperti mengembalikan atau memproses lebih lanjut
                isSuccess = True
                jsonPayload = {"inbox": serialized_inbox, "send": serialized_send}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to get data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been get', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
        else :
            try:
                # Mengambil semua data dari model V_VendorServiceType
                objFormMethods = SwitchFormMethods()
                objGetForm = objFormMethods.post_data(request.data)
                isSuccess = True
                jsonPayload = {"creator": request.data.get('created_by')}
                
            except ValidationError as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to create data: {str(ex)}')
            
            except Exception as ex:
                ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
                return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))
            if isSuccess:
                return rsp.RESPONSE_200_OK(msg='Data has been created', payload=jsonPayload)

            return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
        
    def put(self, request):
        errMsg = ''
        isSuccess = False
        rsp = JsonResponseMessage()
        objProcessedTime = None
        jsonPayload = None
        try:
            # Mengambil semua data dari model V_VendorServiceType
            objFormMethods = SwitchFormMethods()
            objGetForm = objFormMethods.put_data(request.data)
            isSuccess = True
            jsonPayload = {"creator": request.data.get('updated_by')}
            
        except ValidationError as ex:
            print(str(ex))
            ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
            return rsp.RESPONSE_400_BAD_REQUEST(msg=f'Failed to update data: {str(ex)}')
            
        except Exception as ex:
            ErrorLog.createErrLog(self,'Master Room', str(ex), request.data, request.path)
            return rsp.RESPONSE_500_INTERNAL_SERVER_ERROR(MOD_CODE, str(ex))

        if isSuccess:
            return rsp.RESPONSE_200_OK(msg='Data has been updated', payload=jsonPayload)
        # print('masuk')
        return rsp.RESPONSE_400_BAD_REQUEST(MOD_CODE)
    
v_availableroom = AvailableRoomView.as_view()
v_book = BookView.as_view()
v_switch = SwitchBookView.as_view()