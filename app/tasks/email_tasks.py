from app.tasks.celery_app import celery_app
import logging
import time

logger = logging.getLogger(__name__)

@celery_app.task(name="app.tasks.email_tasks.send_welcome_email")
def send_welcome_email(user_email: str):
    logger.info("📧 Sending welcome email to %s", user_email)
    time.sleep(3)
    logger.info("✅ Email sent to %s", user_email)
    return f"Email sent to {user_email}"
