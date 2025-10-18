### Time Complexity
- O(n)

### Pattern
- For Loop

#### Notes
- Set min price as prices[0]
- move along each price in the list to find the max_profit (prices[i] - min_price), if the the current price is lower than min_price,
set current_price to be the new min_price
