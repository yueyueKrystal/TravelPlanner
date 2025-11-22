import os
from langchain_community.chat_models import ChatSparkLLM
from langchain_classic.chains import llm
from dotenv import load_dotenv

load_dotenv()

# AI model API
my_llm = ChatSparkLLM(
    request_timeout=180,
    spark_api_url=os.getenv('IFLYTEK_SPARK_API_URL'),
    spark_llm_domain=os.getenv("IFLYTEK_SPARK_API_MODEL"),
    spark_app_id=os.getenv("IFLYTEK_SPARK_APP_ID"),
    spark_api_key=os.getenv("IFLYTEK_SPARK_API_KEY"),
    spark_api_secret=os.getenv("IFLYTEK_SPARK_API_SECRET")
)


