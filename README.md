# ControlVolume
### پیاده سازی پروژه کنترل کردن صدای سیستم با حرکات انگشتان دست(نمونه ساده ای از کاربرد **Computer Vision** و کتابخانه های مرتبط با آن)
### ابتدا کتابخانه های زیر را نصب کنید

``` pip install opencv-python ```  
``` pip install mediapipe ``` \
``` pip install pyautogui ```



# نکته: برنامه نیاز به دسترسی **webcam** سیستم شما دارد.
## ابتدا سعی می شود تا با خواندن اطلاعات تصویر از **webcam** دستگاه شما، حرکات دست شما تشخیص داده شود و سپس با کمک کتابخانه **pyautogui** صدای سیستم تغییر کند.
### تحوه عملکرد برنامه به شرح زیر است:
1- اگر هر یک از انگشتان دست خود را به سمت بالا بگیرید، صدای سیستم کم می شود.
2- اگر هر یک از انگشتان دست خود را به سمت پایین بگیرید، صدای سیتم کم می شود.
3- اگر انگشت کوچک خود را به شمت بالا بگیرید، صدای سیستم **mute/unmute** می شود.







