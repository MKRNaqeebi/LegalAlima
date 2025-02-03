# pylint: disable=C0301
"""
This module contains the prompts used in the interface for the task "Convert Unstructured Text to JSON".
"""

MAIN_PROMPT = """
**Task:** You are an AI assistant specializing in extracting structured data from unstructured text. Your task is to convert the provided text into a JSON object, mapping specific pieces of information to predefined keys.

**Input:**

*   **Text:** "[TEXT]"
*   **Keys:** ```[KEYS]```

**Instructions:**

1.  Analyze the provided text and identify the information corresponding to each key.
2.  Create a valid JSON object where each key from the "Keys" list is a top-level property.
3.  Assign the extracted information as the value for the corresponding key.
4.  If a piece of information for a key is not found in the text, assign the value `null` to that key.
5.  If there are multiple instances of a key's information in the text (e.g., multiple phone numbers), store the values as a JSON array.
6.  Maintain the original data types as much as possible (e.g., numbers should be represented as numbers, not strings).
7.  Ensure the output is valid JSON and can be parsed by a JSON parser.

**Example:**

**Input:**

*   **Text:** "Create a crypto token with the following parameters: Token Name: EtherToken, Token Symbol: ETHER, Total Supply: 1000000, Decimals: 18, Network: Ethereum, Contract Standard: ERC20, Liquidity Allocation: 50%, Staking Rewards: 20%, Governance Mechanism: DAO, Transaction Fees: 1%, Burn Mechanism: Deflationary, Deflationary or Inflationary: Deflationary, Team Marketing Allocation: 5%, Vesting Schedules: Yes, Utility Use Cases: Yes"
*   **Keys:** ```name, symbol, total_supply, decimals, network, contract_standard, liquidity_allocation, staking_rewards, governance_mechanism, transaction_fees, burn_mechanism, deflationary_or_inflationary, team_marketing_allocation, vesting_schedules, utility_use_cases```

**Expected Output:**

```json
{
    "name": "EtherToken",
    "symbol": "ETHER",
    "total_supply": 1000000,
    "decimals": 18,
    "network": "ethereum",
    "contract_standard": "ERC20",
    "liquidity_allocation": 50,
    "staking_rewards": 20,
    "governance_mechanism": "DAO",
    "transaction_fees": 1,
    "burn_mechanism": "Deflationary",
    "deflationary_or_inflationary": "Deflationary",
    "team_marketing_allocation": 5,
    "vesting_schedules": "Yes",
    "utility_use_cases": "Yes"
}
```
"""

CONTRACT_SOURCE_CODE = """
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "node_modules/@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor() ERC20("MyToken", "MT") {
        _mint(msg.sender, 100000 * 10 ** decimals());
    }
}
"""
