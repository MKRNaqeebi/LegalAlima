"""
utils.py
"""
import json

from openai import OpenAI

from interface.prompts import MAIN_PROMPT


def call_gpt_api(messages):
    """
    Call GPT API with messages and return response
        messages: list of dictionaries with role and content
        first prompt need to be with role system
        returns list of choices
    """
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )
    return response.choices[0].message.content

def messages_to_gpt_format(content):
    """
    Convert messages to GPT format
    """
    keys = 'name, symbol, total_supply, decimals, network, contract_standard, liquidity_allocation, staking_rewards, governance_mechanism, transaction_fees, burn_mechanism, deflationary_or_inflationary, team_marketing_allocation, vesting_schedules, utility_use_cases'
    messages = [{ 'role': 'user', 'content': MAIN_PROMPT.replace('[TEXT]', content).replace('[KEYS]', keys) }]
    response = call_gpt_api(messages)
    return json.loads(response[response.find('{'):response.rfind('}') + 1])
