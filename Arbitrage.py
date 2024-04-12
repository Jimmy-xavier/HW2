# Define the liquidity in each pool
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}


# Append the reverse pair
inverted_liquidity = {(token2, token1): (val2, val1) for (token1, token2), (val1, val2) in liquidity.items()}
liquidity.update(inverted_liquidity)


# define the function that can calculate the swap process
def singleTrade(tokenIn, amountIn, tokenOut):
  lqd = liquidity[(tokenIn,tokenOut)]
  k=lqd[0]*lqd[1]
  y_new=round(k/(lqd[0]+amountIn),6)
  amountOut=lqd[1]-y_new
  # suppose we just swap 1 round, so we don't need to update liquidity here
  # liquidity[(token1,token2)]=(lqd[0]+amountIn, y_new)
  # liquidity[(token2,token1)]=(y_new, lqd[0]+amountIn)
  
  ## Show the AmoutIn and AmountOut in each swap
  # print(tokenIn, "->", tokenOut, ":") 
  # print(tokenIn, "AmountIn:", amountIn)
  # print(tokenOut, "AmountOut", amountOut)
  return amountOut
  


# Calculate the all permutation (Here, we assume that the swap process occurs four times)
from itertools import permutations
path_list = ["tokenA", "tokenC", "tokenD", "tokenE"]
all_permutations = list(permutations(path_list))


# Execute the all possible until tokenB balance>20
for path in all_permutations:
  path_order=[("tokenB", path[0]), (path[0], path[1]), (path[1], path[2]), (path[2], path[3]), (path[3], "tokenB")]
  current=5
  for trade in path_order:
    input_token, output_token = trade
    current = singleTrade(input_token, current, output_token)
  if current >20:
    break


# Print the path and the final balance
trade_path = "->".join([trade[0] for trade in path_order]) + "->" + path_order[-1][1]
print(f"path: {trade_path}, tokenB balance={current}")
