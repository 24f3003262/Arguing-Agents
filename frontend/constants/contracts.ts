export const DEALS_CONTRACT_ADDRESS='0x';

export const DEALS_ABI = [
  {
    "name": "createDeal",
    "type": "function",
    "stateMutability": "nonpayable",
    "inputs": [
      { "name": "_buyer", "type": "address" },
      { "name": "_seller", "type": "address" },
      { "name": "_price", "type": "uint256" },
      { "name": "_item", "type": "string" }
    ],
    "outputs": []
  }

]