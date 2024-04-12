# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution
* my profitable path and final reward: 
    ![](https://hackmd.io/_uploads/SyOMZsUgA.png)

* the amountIn, amountOut value for each swap:
    ![](https://hackmd.io/_uploads/B1AtliUgC.png)


## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
* **Definition:** 
    Slippage refers to the difference between the expected price of a trade and the actuall price. (Before the trade is confirmed, the price may fluctuate )

* **When does slippage primarily happen?**
    The price of a trade is determined by the "constant product formula: x*y=k" in AMM. Thus, slippage primarily happens with a large trade or a shallow liquidity pool. 

* **How Uniswap address the problem?**
    1. Providing Sufficient Liquidity: The more the lequidity there is, the less price fluctuation. 
    2. Slippage Tolerance Settings: Users can set a maximum slippage percentage when making a trade. If the expected slippage exceeds the user's threshold, the transaction will not be executed.



## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
The rationale behind this design is to prevent providing insufficient liquidity, ensuring the stability and efficiency of the liquidity pool.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution
1. Ensuring the accuracy of token pricing mechanisms during trades, thereby enhancing market stability and predictability.
2. By ensuring the constant product, Uniswap offers a stable and reliable market environment, allowing liquidity providers to participate without worrying about drastic market fluctuations.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
* **Definition:** 
    Sandwich attack targets pending transactions initiated by users, also known as transactions in the MemPool, where attackers profit by inserting their own transactions before and after the target transaction.

* **How does sandwich attack works?**
    1. **Monitoring Phase**: Attackers monitor the transaction pool (MemPool) to identify large transactions that could have a significant impact on token prices once executed.
    2. **Front-Running**: Upon identifying a target transaction, attackers swiftly initiate a "front-running" transaction, purchasing the tokens involved in the target transaction, anticipating that the execution of the target transaction will drive up the token price.
    3. **Execution of Target Transaction**: Subsequently, the target transaction is executed, and due to its large size, it has the anticipated impact on the token price (usually an increase).
    4. **Back-Running**: Attackers then execute a "back-running" transaction, selling the tokens purchased earlier after the price increase, thereby profiting from the price difference.

* **Impact**:
    The actual execution price of the target transaction may be higher than expected, meaning users may complete transactions at a more unfavorable price.

