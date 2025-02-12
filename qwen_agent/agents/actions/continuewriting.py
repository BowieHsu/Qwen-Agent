from qwen_agent.agents.actions.base import Action

PROMPT_TEMPLATE_CN = """
你是一个写作助手，请依据参考资料，根据给定的前置文本续写合适的内容。
#参考资料：
{ref_doc}

#前置文本：
{user_request}

保证续写内容和前置文本保持连贯，请开始续写：

"""

PROMPT_TEMPLATE_EN_COT = """
You are a writing assistant, please follow the reference materials and continue to write appropriate content based on the given previous text.

# References:
{ref_doc}

# Previous text:
{user_request}

Please start writing directly, output only the continued text, do not repeat the previous text, do not say irrelevant words, and ensure that the continued content and the previous text remain consistent.

Use the following format:
Thought: you should always think about what to do
Summariz: extracted relevant text
Final Answer: the continuation of previous text

"""

PROMPT_TEMPLATE_EN = """
You are a writing assistant, please follow the reference materials and continue to write appropriate content based on the given previous text.

# References:
{ref_doc}

# Previous text:
{user_request}

Please start writing directly, output only the continued text, do not repeat the previous text, do not say irrelevant words, and ensure that the continued content and the previous text remain consistent.
"""


class ContinueWriting(Action):
    def __init__(self, llm=None, stream=False):
        super().__init__(llm=llm, stream=stream)

    def run(self, ref_doc, user_request, messages=None, prompt_lan='CN'):
        if prompt_lan == 'CN':
            prompt = PROMPT_TEMPLATE_CN.format(
                ref_doc=ref_doc,
                user_request=user_request,
            )
        elif prompt_lan == 'EN':
            prompt = PROMPT_TEMPLATE_EN.format(
                ref_doc=ref_doc,
                user_request=user_request,
            )

        return self._run(prompt, messages=messages)
