# Arguing Agents: A Decentralized Negotiation Protocol
Arguing Agents is a marketplace concept where the friction of human haggling is replaced by autonomous AI negotiation nodes. The system allows buyers and sellers to deploy specialized agents that interact within defined financial and behavioral boundaries, resolving deals through a logic-based "argument" that concludes with on-chain settlement.

## Core Mechanics
The platform moves away from static pricing by allowing both parties to define a personality and a set of hidden constraints for their respective agents.

- The Seller Agent: Established during asset registration, the seller provides a public starting price, a private minimum acceptable price, and a personality profile—such as Aggressive, Balanced, or Conservative—that dictates how stubbornly the agent defends its profit margins.

- The Buyer Agent: Activated when a user expresses interest in an asset, the buyer sets an opening bid, a maximum budget, and a corresponding personality that determines how incrementally they are willing to increase their offers.

- The Negotiation Loop: Once both agents are initialized, they engage in a multi-round exchange. The backend acts as a referee, processing each counter-offer and concession until the agents either find a mathematical overlap or reach a stalemate.

## Technical Implementation
The project is built as a full-stack decentralized application, integrating high-level reasoning with blockchain execution.

- Frontend: Developed using Nuxt 3 and Vue.js, the interface provides a terminal-style environment for monitoring the live negotiation history.

- Backend: A FastAPI server manages the negotiation sessions and maintains a persistent ledger of marketplace assets using a local JSON-based storage system.

- Blockchain: Custom Solidity smart contracts handle the financial finality. When an agreement is reached, the frontend utilizes Wagmi and Viem to trigger a transaction that moves the negotiated amount from the buyer's wallet to the seller.

- AI Integration: The system leverages multiple models, including Gemini and GPT-5.0, to generate the reactive dialogue and logical decision-making required for the agents to defend their positions.


## Strategic Setup for Multi-round interaction
To ensure the agents engage in a meaningful negotiation during a demonstration, the marketplace is configured with specific information asymmetry:

1. Price Anchoring: The public starting price is typically set higher than the buyer's maximum budget, forcing the buyer to initiate the dialogue with a lower counter-offer.

2. Private Overlap: While the public bids remain far apart, a deal is only possible if the seller's secret minimum floor is lower than the buyer's secret maximum ceiling.

3. Initiative: The negotiation logic is structured so the seller must evaluate and respond to the buyer's opening bid, preventing an immediate acceptance and encouraging a multi-round debate.