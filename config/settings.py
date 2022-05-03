from decouple import config as env_config

DEBUG=True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_PORT=env_config("SERVER_PORT")
SERVER_HOST=env_config("SERVER_HOST")


# CELERY_BROKER_URL = env_config("CELERY_BROKER_URL")
# CELERY_RESULT_BACKEND = env_config("CELERY_RESULT_BACKEND")
# CELERY_ACCEPT_CONTENT = ["json"]
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_CREATE_MISSING_QUEUES = True
# CELERY_REDIS_MAX_CONNECTIONS = 15
# CELERY_IGNORE_RESULT=True
# CELERY_STORE_ERRORS_EVEN_IF_IGNORED=True


# ## defining queus, exchanges and routes
# CELERY_QUEUES = {
#         "account": {
#             "exchange": "account",
#             "exchange_type": "topic",
#             "binding_key": "account.#"
#         },

#         "content": {
#             "exchange": "content",
#             "exchange_type": "topic",
#             "binding_key": "content.#"
#         },

#         "analysis": {
#             "exchange": "analysis",
#             "exchange_type": "topic",
#             "binding_key": "analysis.#"
#         },
#         "twitter": {
#             "exchange": "twitter",
#             "exchange_type": "topic",
#             "binding_key": "twitter.#"
#         },
        
# }







# MINUTE_CRON_JOB = {"minute":"*/15"}


# CELERYBEAT_SCHEDULE = {
#         "twitter.celery_start_twitter_bot": {
#             "task": "twitterbot.tasks.twitter.celery_start_twitter_bot",
#             "schedule": crontab(**MINUTE_CRON_JOB),
#             "options": {"queue" : "twitter"},
#             # "args": ({"parallel": PARALLELIZE_EXTRACTION, "batch_id": 1},)
#         }
#     }

