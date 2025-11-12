from app.tasks.celery_app import celery_app

@celery_app.task(name="app.tasks.email_tasks.send_welcome_email")
def send_welcome_email(user_email: str):
    print(f"📧 Sending welcome email to {user_email}")
    import time; time.sleep(3)
    return f"Email sent to {user_email}"
