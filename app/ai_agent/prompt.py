from langchain_core.prompts import PromptTemplate
 
#Prompt template
prompt = PromptTemplate(
    input_variables=["user_input"],
    template="你是一个AI旅程规划App，请根据用户的输入信息规划行程，以下是旅程的输入信息：" \
        "旅行目的地是:{destination}，" \
        "游玩天数:{days}天。" \
        "请根据以上信息输出一个详细的行程规划，包括景点、交通、住宿等信息." \
        "直接返回行程规划结果，不要回问问题。"
)