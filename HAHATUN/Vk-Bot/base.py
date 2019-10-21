#=======================================Import====================================================
import pyrebase
from config import db_config, vk_token
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
#=================================================================================================
#
#=========================================Tokens==================================================
vktoken = '12608dbd12d1a37e7dc4a19ff218849b5c123b431f2014fbec393e2e06b59a8baa623e225d5b53d8ddde1'
pyrebase_path = "C:\\TrashBox\\HAHATUN\\Vk-Bot\\edubot72-firebase-adminsdk-ga2lf-a12ce0d85e.json"
#=================================================================================================
#
#====================================Vk initialization============================================
def init_vk():
    vk_session = vk_api.VkApi(token = vk_token(vktoken))
    vk = vk_session.get_api()
    return vk
def init_longpoll():
    vk_session = vk_api.VkApi(token = vk_token(vktoken))
    longpoll = VkLongPoll(vk_session)
    return longpoll
#=================================================================================================
#
#===========================================Data Base=============================================
def init_db():
    firebase = pyrebase.initialize_app(db_config(pyrebase_path))
    auth = firebase.auth()
    db = firebase.database()
    return db


def get_user_info(id):
    info = db.child("users").child(id).get().val()
    return info


def get_test(exam, work): # Return task from exam
    test = {}             # Надо переделать структуру скорее всего, и подвести под адекватный вид
                          # Тут можно сразу словарём выдавать, смотри на get_user_info
    variants = db.child(exam).child(work).child("variants").get().val() + 1
    test['question'] = db.child(exam).child(work).child("que").get().val()
    for i in range(1,variants):
        test[str(i)] = db.child(exam).child(work).child(str(i)).get().val()
    test['answer'] = db.child(exam).child(work).child("ans").get().val()
    return test


db = init_db()

print(get_test("math","task1"))
#================================================================================================